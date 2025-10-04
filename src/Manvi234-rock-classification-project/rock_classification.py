# -*- coding: utf-8 -*-
"""
Prompt-Based Interactive Rock Classification Script

This script guides the user through a rock classification pipeline by asking
a series of questions in the terminal.
"""

# --- 1. Imports ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from pathlib import Path
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import PowerTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, StackingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, f1_score

warnings.filterwarnings('ignore')

# --- 2. Core Logic Functions (Data loading, preprocessing, evaluation) ---
# These functions contain the core analysis pipeline and are unchanged.

def load_and_combine_data(label_path, feature_path):
    """Loads and combines rock data."""
    print("\nStep 1: Loading and combining data...")
    if not Path(label_path).exists() or not Path(feature_path).exists():
        print(f"Error: One or more data files not found. Please check paths.")
        return None
    df_labels = pd.read_excel(label_path, names=['label'], usecols=[1], nrows=480, header=None)
    df_features = pd.read_csv(
        feature_path, delim_whitespace=True, header=None,
        usecols=[2] + list(range(3, 14)), nrows=480
    )
    df_features.columns = ["token_number"] + [f"feature_{i}" for i in range(1, 12)]
    combined_df = pd.concat([df_labels, df_features], axis=1)
    print("✅ Data loaded successfully.")
    return combined_df

def preprocess_and_split(df):
    """Applies transformation and splits data."""
    print("\nStep 2: Preprocessing and splitting data...")
    features = [f"feature_{i}" for i in range(1, 12)]
    X = df[features]
    pt = PowerTransformer(method='yeo-johnson')
    X_transformed = pt.fit_transform(X)
    X_transformed_df = pd.DataFrame(X_transformed, columns=features)
    transformed_df = pd.concat([df[['label', 'token_number']], X_transformed_df], axis=1)
    
    train_df = transformed_df[transformed_df['token_number'].between(1, 10)]
    val_df = transformed_df[transformed_df['token_number'].between(11, 13)]
    test_df = transformed_df[transformed_df['token_number'].between(14, 16)]

    X_train, y_train = train_df[features], train_df['label']
    X_val, y_val = val_df[features], val_df['label']
    X_test, y_test = test_df[features], test_df['label']
    
    print(f"✅ Data split complete: Train={len(X_train)}, Val={len(X_val)}, Test={len(X_test)}")
    return X_train, y_train, X_val, y_val, X_test, y_test, transformed_df

def evaluate_model(model, X, y_true, set_name="Set"):
    """Calculates and prints performance metrics."""
    y_pred = model.predict(X)
    print(f"--- Performance on {set_name} ---")
    print(f"Accuracy: {accuracy_score(y_true, y_pred):.4f}")
    print(f"F1 Score (weighted): {f1_score(y_true, y_pred, average='weighted'):.4f}\n")

def analyze_human_vs_model(best_model, full_feature_df, human_trial_path, save_plot=True, show_plot=True):
    """Compares the model's accuracy per rock with human accuracy."""
    print("\nFinal Step: Comparing Model vs. Human Performance...")
    if not Path(human_trial_path).exists():
        print(f"Error: Human trial data file not found at '{human_trial_path}'. Skipping comparison.")
        return

    human_df = pd.read_csv(human_trial_path)
    human_df = human_df[human_df['rocknumber'].between(1, 480)].dropna()
    human_accuracy_mean = human_df.groupby('rocknumber')['cat_correct'].mean()
    
    features = [f"feature_{i}" for i in range(1, 12)]
    all_X = full_feature_df[features]
    all_y = full_feature_df['label']
    predictions = best_model.predict(all_X)
    
    model_results = pd.DataFrame({'true_label': all_y, 'predicted_label': predictions})
    model_results['is_correct'] = (model_results['true_label'] == model_results['predicted_label']).astype(int)
    
    num_tokens_per_rock = 16
    rock_numbers = np.repeat(np.arange(1, (len(full_feature_df) // num_tokens_per_rock) + 1), num_tokens_per_rock)
    model_results['rocknumber'] = rock_numbers[:len(full_feature_df)]
    model_accuracy_per_rock = model_results.groupby('rocknumber')['is_correct'].mean()
    
    plt.figure(figsize=(12, 8))
    comparison_df = pd.DataFrame({
        'human_accuracy': human_accuracy_mean, 'model_accuracy': model_accuracy_per_rock
    }).dropna()
    plt.scatter(comparison_df['human_accuracy'], comparison_df['model_accuracy'], alpha=0.6, edgecolors='w')
    plt.plot([0, 1], [0, 1], 'r--', label='y=x (Perfect Correlation)')
    plt.title('Model Accuracy vs. Average Human Accuracy per Rock', fontsize=16)
    plt.xlabel('Average Human Accuracy', fontsize=12)
    plt.ylabel('Model Accuracy', fontsize=12)
    plt.grid(True); plt.legend(); plt.axis('equal'); plt.xlim(0, 1); plt.ylim(0, 1)
    
    if save_plot:
        plot_filename = 'human_vs_model_accuracy.png'
        plt.savefig(plot_filename)
        print(f"\n✅ Comparison plot saved as '{plot_filename}'")
    
    if show_plot:
        print("Displaying plot...")
        plt.show()

# --- 3. Interactive User Prompt Functions ---

def get_input_with_default(prompt, default):
    """Asks for user input, using a default if none is given."""
    user_input = input(f"{prompt} [{default}]: ")
    return user_input or default

def get_choice_from_user(prompt, options):
    """Asks the user to choose from a list of options."""
    print(prompt)
    for key, value in options.items():
        print(f"  {key}) {value}")
    
    while True:
        choice = input("Your choice: ").lower()
        if choice in options:
            return choice
        print("Invalid option, please try again.")

def get_yes_no(prompt):
    """Asks a yes/no question."""
    while True:
        choice = input(f"{prompt} (yes/no): ").lower()
        if choice in ['yes', 'y']:
            return True
        if choice in ['no', 'n']:
            return False
        print("Invalid answer. Please enter 'yes' or 'no'.")


# --- 4. Main Interactive Execution Block ---

def main():
    """Main function to run the interactive pipeline."""
    print("--- Welcome to the Interactive Rock Classification Script! ---")
    
    # 1. Get file paths from user
    label_file = get_input_with_default("Enter path to the label file", 'aggregateRockData.xlsx')
    feature_file = get_input_with_default("Enter path to the feature file", 'feature_presence540.txt')
    human_file = get_input_with_default("Enter path to the human trial data file", 'trialData.csv')
    
    # 2. Load data
    df_combined = load_and_combine_data(label_file, feature_file)
    if df_combined is None:
        return # Stop if data loading failed
        
    X_train, y_train, X_val, y_val, X_test, y_test, full_df = preprocess_and_split(df_combined)
    
    # 3. Get user's choice of model
    model_options = {
        'lr': 'Logistic Regression',
        'svm': 'Support Vector Machine (SVM)',
        'rf': 'Random Forest',
        'adaboost': 'AdaBoost with Random Forest (Recommended Best)',
        'all': 'Run all of the above'
    }
    model_choice = get_choice_from_user("\nStep 3: Which model would you like to run?", model_options)
    
    # 4. Ask about hyperparameter tuning
    use_tuning = get_yes_no("\nEnable hyperparameter tuning? (slower, but more accurate)")
    
    # 5. Train the selected model(s)
    print("\nStep 4: Training model(s)...")
    
    models_to_run = list(model_options.keys())[:-1] if model_choice == 'all' else [model_choice]
    best_model_for_plot = None

    for model_name in models_to_run:
        print(f"\n--- Training {model_options[model_name]} ---")
        
        # Define model and parameters
        if model_name == 'lr':
            estimator = LogisticRegression(multi_class='multinomial', solver='lbfgs', random_state=42)
            params = {'C': [0.01, 0.1, 1], 'max_iter': [200]}
        elif model_name == 'svm':
            estimator = SVC(probability=True, random_state=42)
            params = {'C': [1, 10], 'kernel': ['poly', 'rbf']}
        elif model_name == 'rf':
            estimator = RandomForestClassifier(random_state=42)
            params = {'n_estimators': [50, 100], 'max_depth': [20, 30]}
        elif model_name == 'adaboost':
            # AdaBoost uses a base model. We'll use a default RF.
            base_rf = RandomForestClassifier(n_estimators=100, max_depth=20, random_state=42)
            estimator = AdaBoostClassifier(estimator=base_rf, n_estimators=50, random_state=42)
            params = {} # No separate tuning for AdaBoost in this setup

        # Perform training
        if use_tuning and params:
            grid_search = GridSearchCV(estimator, params, cv=3, scoring='accuracy', n_jobs=-1)
            grid_search.fit(X_train, y_train)
            best_model = grid_search.best_estimator_
            print(f"Best Parameters found: {grid_search.best_params_}")
        else:
            estimator.fit(X_train, y_train)
            best_model = estimator
        
        # Evaluate and store the last trained model for the final plot
        evaluate_model(best_model, X_train, y_train, "Training Set")
        evaluate_model(best_model, X_val, y_val, "Validation Set")
        evaluate_model(best_model, X_test, y_test, "Test Set")
        best_model_for_plot = best_model

    # 6. Run the final comparison
    if best_model_for_plot:
        save = get_yes_no("\nDo you want to save the final comparison plot?")
        show = get_yes_no("Do you want to display the final comparison plot?")
        analyze_human_vs_model(best_model_for_plot, full_df, human_file, save_plot=save, show_plot=show)

    print("\n--- Script finished. ---")


if __name__ == "__main__":
    main()
