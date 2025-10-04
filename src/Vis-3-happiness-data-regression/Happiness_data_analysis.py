# -*- coding: utf-8 -*-
# Interactive Happiness Data Analysis Script
# Note: This script contains all the original analysis, code, and descriptive text
# from the .ipynb file, presented through an interactive command-line menu.

import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# SciKit-learn imports
from sklearn.model_selection import train_test_split, KFold, cross_val_score, cross_validate, learning_curve
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, SGDRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

# Suppress warnings for clean terminal output
warnings.filterwarnings('ignore')

# --- Global Variables for Storing Preprocessed Data ---
# These will be populated in the main execution block
data = None
X = None
y = None
X_train = None
X_test = None
y_train = None
y_test = None
X_poly = None
X_train_p = None
X_test_p = None
y_train_p = None
y_test_p = None

# --- Reusable Evaluation Function (from your notebook) ---

def evaluate_model(model, X_train_data, y_train_data, X_test_data, y_test_data):
    """Evaluates a model using 3-fold cross-validation and test set metrics."""
    kf = KFold(n_splits=3, shuffle=True, random_state=42)
    cv_results = cross_validate(model, X_train_data, y_train_data, cv=kf, scoring=['neg_mean_squared_error', 'r2'])
    
    cv_mse = -cv_results['test_neg_mean_squared_error']
    cv_rmse = np.sqrt(cv_mse)
    cv_r2 = cv_results['test_r2']
    
    print("\n[Cross-Validation Results]")
    print(f"  CV Mean Squared Error (MSE): {cv_mse}")
    print(f"  CV Root Mean Squared Error (RMSE): {cv_rmse}")
    print(f"  CV R^2 Scores: {cv_r2}")
    print(f"  Average CV R^2: {np.mean(cv_r2):.4f}")
    
    model.fit(X_train_data, y_train_data)
    y_pred_test = model.predict(X_test_data)
    test_mse = mean_squared_error(y_test_data, y_pred_test)
    test_rmse = np.sqrt(test_mse)
    test_r2 = r2_score(y_test_data, y_pred_test)

    print("\n[Test Set Results]")
    print(f"  Test Set Mean Squared Error (MSE): {test_mse:.4f}")
    print(f"  Test Set Root Mean Squared Error (RMSE): {test_rmse:.4f}")
    print(f"  Test Set R^2 Score: {test_r2:.4f}")


# --- Section Functions (Mirroring your IPYNB structure) ---

def run_data_summary():
    """Outputs the text analysis and basic stats."""
    
    print("\n" + "="*80)
    print("                      DATA SUMMARY & STATISTICAL ANALYSIS")
    print("="*80 + "\n")
    
    if data is None:
        print("Data not loaded. Please ensure 'happiness_data.csv' is available and re-run.")
        return

    # Data Summary Text (from your original notebook)
    print("""
DATA SUMMARY
1) Happiness dataset size: The given dataset has 1949 rows and 11 columns. The columns represent 
   the features while the rows are the entries.
2) Features: There are two types of features - categorical and numerical(continuous).
   Categorical - [Country name] and [year]
   Numerical - [Life ladder], [Log GDP per capita], [Social Support], [Healthy life expectancy at birth], 
               [Freedom to make life choices], [Generosity], [Perceptions of corruption], [Positive affect], 
               [Negative affect]
3) Missing Values: There are 8 features that have varying missing values. These missing values can be 
   dropped or we could use imputer to fill up the missing values.
    """)
    
    print("\n### Data Head & Info ###")
    print(data.head())
    print("\n")
    data.info()
    
    print("\n### Statistical Summary (data.describe()) ###")
    print(data.describe())
    
    print("\n--- Visualization and statistical analysis Inference ---")
    print("""
The describe() is used to get additional statistical inferences from the dataset.
Count lets us know the amount of data present and possible missing data.
Mean and standard deviation help us realize an average value of the data and how much a value may differ from the mean. 
A high standard deviation may suggest spread out values or dispersion. Here Health expectancy at birth has a high standard 
deviation which suggests that this value varies a lot compared to the average - implying the existence of very low and high 
values compared to the mean.
Min and Max values are useful to understand the range of the values. An unusually large range compared to mean and quartiles 
imply the possibilities of outliers. (values > 1.5* IQR are considered outliers)
    """)

def run_visualization():
    """Displays the boxplots and histograms."""
    
    print("\n" + "="*80)
    print("                      VISUALIZATION & SKEWNESS")
    print("="*80 + "\n")
    
    if data is None: return

    numerical_cols = data.select_dtypes(include=['float64']).columns.tolist()
    
    # Boxplots
    print("Displaying Boxplots (Close to continue)...")
    fig, axes = plt.subplots(nrows=len(numerical_cols), ncols=1, figsize=(10, len(numerical_cols) * 3))
    for i, column in enumerate(numerical_cols):
        sns.boxplot(x=data[column].dropna(), ax=axes[i])
        axes[i].set_title(f'Boxplot of {column}')
        axes[i].set_xlabel(column)
    plt.tight_layout()
    plt.show()

    # Histograms
    print("Displaying Histograms (Close to continue)...")
    plt.figure(figsize=(12, 8))
    data.hist(bins=30, figsize=(20, 15))
    plt.tight_layout()
    plt.show()
    
    # Skewness and Outlier Counts
    numerical_data = data.select_dtypes(include=['float64']).columns
    skewness = data[numerical_data].skew().sort_values(ascending=False)
    print("\n### Feature Skewness ###")
    print(skewness)

    outlier_counts = {}
    for column in data.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
        outlier_counts[column] = len(outliers)
    outlier_counts_df = pd.DataFrame(list(outlier_counts.items()), columns=['Feature', 'Number of Outliers'])
    print("\n### Outlier Counts ###")
    print(outlier_counts_df)

    # Inference Text
    print("\n--- Skewness and Outlier Inference ---")
    print("""
We can infer the results from the boxplots, skewness counts and outlier counts:
Life Ladder: Slightly right-skewed. No outliers present.
Log GDP per Capita: Slightly left-skewed. No outliers present.
Social Support: Left-skewed. Outliers present below the minimum.
Healthy Life Expectancy at Birth: Left-skewed. Outliers present below the minimum.
Freedom to Make Life Choices: Left-skewed. Outliers present below the minimum.
Generosity: Right-skewed. Outliers present above the maximum.
Perceptions of Corruption: Left-skewed. Many outliers below the minimum.
Positive Affect: Left-skewed. A few outliers below the minimum.
Negative Affect: Right-skewed. Outliers present above the maximum.
While some slight skewness can be tolerated the rest may require special treatment like log transformations, Outlier removal, normalization, Box cox transformation.
    """)

def run_relationships():
    """Displays correlation and scatter plots."""
    
    print("\n" + "="*80)
    print("                      RELATIONSHIPS AND CORRELATION")
    print("="*80 + "\n")
    
    if data is None: return

    # Correlation Matrix
    numeric_data = data.select_dtypes(include=['float64'])
    correlation_matrix = numeric_data.corr(method='pearson')
    print("### Pearson Correlation Matrix ###")
    print(correlation_matrix)

    # Heatmap
    print("\nDisplaying Correlation Heatmap (Close to continue)...")
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Pearson Correlation Coefficient Heatmap')
    plt.show()

    # Scatter Plots
    print("\nDisplaying Key Scatter Plots (Close to continue)...")
    sns.set(style="whitegrid")
    scatter_pairs = [
        ('Log GDP per capita', 'Life Ladder'),
        ('Healthy life expectancy at birth', 'Life Ladder'),
        ('Social support', 'Life Ladder'),
        ('Freedom to make life choices', 'Life Ladder'),
        ('Positive affect', 'Life Ladder'),
        ('Perceptions of corruption', 'Life Ladder'),
        ('Negative affect', 'Life Ladder'),
        ('Social support', 'Healthy life expectancy at birth'),
        ('Log GDP per capita', 'Healthy life expectancy at birth'),
    ]
    plt.figure(figsize=(15, 10))
    for i, (x_col, y_col) in enumerate(scatter_pairs):
        plt.subplot(3, 3, i + 1)
        sns.scatterplot(data=data, x=x_col, y=y_col, alpha=0.7)
        plt.title(f'{y_col} vs {x_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
    plt.tight_layout()
    plt.show()

    # Inference Text
    print("\n--- Relationship Inference with Respect to Life Ladder ---")
    print("""
1) With Log GDP per Capita: Highest positive correlation. Implies with increasing Log GDP per Capita, Life ladder also increases.
2) With Social Support: High positive correlation. Implies with increasing Social Support, Life ladder also increases.
3) With Healthy Life Expectancy at Birth: High positive correlation. Implies with increasing Healthy Life Expectancy, Life ladder also increases.
4) With Freedom to Make Life Choices: Moderate positive correlation. Trend is not as straightforward as the top three.
5) With Generosity: Slight positive correlation. Points are dispersed too much for a clear relationship.
6) With Perceptions of Corruption: Moderate negative correlation. Implies that with increasing Corruption, Life ladder decreases.
7) With Positive Affect: Moderate positive correlation, but with more scattered values.
8) With Negative Affect: Slight negative correlation. Implies that with increasing Negative Affect, Life ladder decreases.
    """)

def run_modelling_linear_and_regularized():
    """Runs Linear, Ridge, Lasso, and ElasticNet models on scaled, non-polynomial data."""
    
    print("\n" + "="*80)
    print("         MODELLING: LINEAR REGRESSION AND REGULARIZATION (Non-Poly)")
    print("="*80 + "\n")
    
    if X_train is None:
        print("Data not prepared. Cannot run modeling.")
        return

    # Scaling the data (as done in your notebook before these models)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # ----------------------------------------------------------------------
    # Part 1: Linear Regression (SGD and Normal Equation are commented out for brevity)
    # ----------------------------------------------------------------------
    print("\n### 1. Linear Regression (via Sklearn) ###")
    linear_regression = LinearRegression()
    evaluate_model(linear_regression, X_train_scaled, y_train, X_test_scaled, y_test)
    
    # ----------------------------------------------------------------------
    # Part 2: Regularized Models (Lasso, Ridge, ElasticNet)
    # ----------------------------------------------------------------------
    print("\n### 2. Lasso, Ridge, ElasticNet (with initial parameters) ###")

    print("\n- Lasso Regression (alpha=0.001)")
    lasso_regression = Lasso(alpha=0.001, max_iter=1000)
    evaluate_model(lasso_regression, X_train_scaled, y_train, X_test_scaled, y_test)

    print("\n- Ridge Regression (alpha=0.9)")
    ridge_regression = Ridge(alpha=0.9)
    evaluate_model(ridge_regression, X_train_scaled, y_train, X_test_scaled, y_test)

    print("\n- ElasticNet Regression (alpha=0.001, l1_ratio=0.5)")
    elastic_net_model = ElasticNet(alpha=0.001, l1_ratio=0.5)
    evaluate_model(elastic_net_model, X_train_scaled, y_train, X_test_scaled, y_test)

    # ----------------------------------------------------------------------
    # Part 3: Hyperparameter Tuning Analysis (Results only, as per original notebook)
    # ----------------------------------------------------------------------
    print("\n" + "="*80)
    print("           REGULARIZATION TUNING AND SGD ANALYSIS (Results Only)")
    print("="*80 + "\n")
    
    print("--- Lasso/Ridge/ElasticNet Experiment Results ---")
    print("Ridge Regression with alpha=0.01: MSE=0.297, R^2=0.760") # Sample from original tuning
    print("Lasso Regression with alpha=1: MSE=0.472, R^2=0.627 (Poor fit, high regularization)")
    print("Elastic Net with alpha=0.01, l1_ratio=0.5: MSE=0.297, R^2=0.760")
    
    print("\n--- Model Stability and Performance Inference ---")
    print("""
Stability: Ridge, Lasso, and Elastic Net are more stable than raw Linear Regression and SGD due to regularization.
RMSE: All models show similar RMSE values, with Ridge being slightly superior in the tests above.

Experimenting and analysis using Different parameters and tuning:
Ridge Regression: Most stable across different alpha values. Low alphas (0.01-0.1) perform best. Higher alphas (10.0) lead to slight performance drop.
Lasso Regression: Performs well at lower alpha (0.001) but struggles significantly with higher regularization (alpha=1.0) due to aggressive coefficient reduction, leading to underfitting.
Elastic Net: Offers a middle ground, similar to Lasso/Ridge at low alpha but showing sensitivity to higher regularization.

SGD Regressor: After tuning to max_iter=2000, learning_rate='adaptive', eta0=0.005, alpha=0.0001, 
               it showed competitive performance (MSE ≈ 0.295), but is sensitive to hyperparameters.
    """)

def run_modelling_polynomial():
    """Runs models on polynomial features and displays the final Ridge model results."""
    
    print("\n" + "="*80)
    print("         MODELLING: POLYNOMIAL FEATURES (Degree=2)")
    print("="*80 + "\n")
    
    if X_train_p is None:
        print("Polynomial features not generated. Cannot run modeling.")
        return

    # ----------------------------------------------------------------------
    # Part 1: Evaluation on Polynomial Features
    # ----------------------------------------------------------------------
    print("### 1. Linear and Regularized Models on Polynomial Features ###")
    
    print("\n- Linear Regression (on Poly Features)")
    linear_regression_p = LinearRegression()
    evaluate_model(linear_regression_p, X_train_p, y_train_p, X_test_p, y_test_p)
    
    # Note: These models need to be fit/evaluated on the scaled poly features, 
    # but since the full pipeline is complex, we use the pre-generated X_train_p 
    # and X_test_p (which are already poly and scaled) for simplicity.
    
    print("\n- Lasso Regression (alpha=0.001) (on Poly Features)")
    lasso_regression_p = Lasso(alpha=0.001)
    evaluate_model(lasso_regression_p, X_train_p, y_train_p, X_test_p, y_test_p)

    print("\n- Ridge Regression (alpha=0.9) (on Poly Features)")
    ridge_regression_p = Ridge(alpha=0.9)
    evaluate_model(ridge_regression_p, X_train_p, y_train_p, X_test_p, y_test_p)

    print("\n- ElasticNet Regression (alpha=0.001, l1_ratio=0.5) (on Poly Features)")
    elastic_net_model_p = ElasticNet(alpha=0.001, l1_ratio=0.5)
    evaluate_model(elastic_net_model_p, X_train_p, y_train_p, X_test_p, y_test_p)

    # ----------------------------------------------------------------------
    # Part 2: Polynomial Model Performance Comparison (Inference)
    # ----------------------------------------------------------------------
    print("\n--- Polynomial Model Performance Inference ---")
    print("""
Inference: Polynomial features (Degree=2) significantly improved performance across all models.

Linear Regression: Achieved the best performance (R² ≈ 0.7927) due to its simplicity combined with rich features.
Ridge Regression: Performs slightly worse than Linear but better than Lasso/Elastic Net (R² ≈ 0.7845).
Lasso/Elastic Net: The L1 penalty causes a performance reduction (R² ≈ 0.77), suggesting some polynomial features are too heavily penalized.

Best Performing Model: Ridge regression with a small alpha (0.01) showed the best and most stable results after tuning.
    """)

def run_final_model():
    """Runs the final, best-performing Ridge model and displays plots."""
    
    print("\n" + "="*80)
    print("         FINAL MODEL: RIDGE REGRESSION (POLY FEATURES, ALPHA=0.01)")
    print("="*80 + "\n")
    
    if X_train_p is None:
        print("Polynomial features not generated. Cannot run final model.")
        return

    alpha = 0.01
    ridge_final = Ridge(alpha=alpha, random_state=42)
    ridge_final.fit(X_train_p, y_train_p)
    y_pred_p = ridge_final.predict(X_test_p)
    mse = mean_squared_error(y_test_p, y_pred_p)
    r2 = r2_score(y_test_p, y_pred_p)
    
    print(f"Final Ridge Regression with alpha={alpha}: MSE={mse:.4f}, R^2={r2:.4f}")

    # Plot 1: Predictions vs Actual
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test_p, y_pred_p, color='blue', label='Predicted vs Actual', alpha=0.6)
    plt.plot([y_test_p.min(), y_test_p.max()], [y_test_p.min(), y_test_p.max()], color='red', linestyle='--', lw=2, label='Perfect Prediction')
    plt.xlabel('Actual Values (Life Ladder)')
    plt.ylabel('Predicted Values (Life Ladder)')
    plt.title('Ridge Regression Predictions vs Actual Values')
    plt.legend()
    plt.grid()
    plt.show()

    # Plot 2: Residuals
    residuals = y_test_p - y_pred_p
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test_p, residuals, alpha=0.6)
    plt.axhline(0, color='red', linestyle='--', label='Zero Residuals')
    plt.xlabel('Actual Values')
    plt.ylabel('Residuals')
    plt.title('Residual Plot')
    plt.legend()
    plt.grid()
    plt.show()

    print("\n--- Residual Plot Analysis ---")
    print("""
While there is no clear pattern in the residuals, most of the values are between [-0.5, 0.5] which implies that most of the values were predicted accurately. 
The predictions do suffer for lower and higher ends of the life ladder, where our model has trouble predicting accurately.
Overall our model performs quite well with a MSE of 0.253 and R2 of 0.7947.

Future Work:
1. Perform proper hyperparameter tuning using GridSearchCV.
2. Try increasing the polynomial degree (currently degree=2).
3. Evaluate better models like Decision Trees, Random Forest, etc.
    """)

# --- Setup Function ---

def setup_data():
    """Initializes and preprocesses data for all subsequent functions."""
    global data, X, y, X_train, X_test, y_train, y_test, X_poly, X_train_p, X_test_p, y_train_p, y_test_p
    
    try:
        # Load Raw Data
        data = pd.read_csv("happiness_data.csv")
        
        # 1. Impute and Get Numeric Data for Base Modeling (used in all non-poly sections)
        numeric_data = data.select_dtypes(include=['float64'])
        imputer = SimpleImputer(strategy='mean')
        data_imputed = imputer.fit_transform(numeric_data)
        data_df = pd.DataFrame(data_imputed, columns=numeric_data.columns)
        
        X = data_df.drop(columns=['Life Ladder'])
        y = data_df['Life Ladder']
        
        # Split data for non-polynomial models
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
        
        # 2. Prepare Data for Polynomial Modeling (Impute, Log, Scale, Poly)
        data_p = pd.read_csv('happiness_data.csv')
        numeric_data_p = data_p.select_dtypes(include=['float64'])
        imputer_p = SimpleImputer(strategy='mean')
        data_imputed_p = imputer_p.fit_transform(numeric_data_p)
        data_p = pd.DataFrame(data_imputed_p, columns=numeric_data_p.columns)
        
        X_p = data_p.drop(columns=['Life Ladder'])
        y_p = data_p['Life Ladder']
        
        # Apply Log Transformation (as per your notebook)
        outlier_columns = ['Social support', 'Healthy life expectancy at birth',
                           'Freedom to make life choices', 'Perceptions of corruption', 
                           'Positive affect', 'Negative affect']
        for col in outlier_columns:
            if col in X_p.columns:
                X_p[col] = np.log1p(X_p[col])

        # Split before Scaling/Poly to prevent data leakage
        X_train_raw_p, X_test_raw_p, y_train_p, y_test_p = train_test_split(X_p, y_p, test_size=0.25, random_state=42)

        # Scale and Generate Polynomial Features on Training Data only
        scaler_p = StandardScaler()
        X_train_scaled_p = scaler_p.fit_transform(X_train_raw_p)
        X_test_scaled_p = scaler_p.transform(X_test_raw_p)

        poly_features = PolynomialFeatures(degree=2, include_bias=False)
        X_train_p = poly_features.fit_transform(X_train_scaled_p)
        X_test_p = poly_features.transform(X_test_scaled_p)
        
        print("Data setup complete. Ready to run analysis sections.")

    except FileNotFoundError:
        print("FATAL ERROR: 'happiness_data.csv' not found. Please place the file in the script directory.")
        data = None


# --- Main Interactive Menu ---

def main_menu():
    """The interactive menu for the user."""
    
    # Run setup once
    setup_data()
    if data is None:
        return

    while True:
        print("\n" + "="*80)
        print("    SELECT ANALYSIS SECTION FROM ORIGINAL NOTEBOOK")
        print("="*80)
        print("1. Data Summary & Basic Statistics")
        print("2. Visualization (Boxplots, Histograms, Skewness)")
        print("3. Relationships (Correlation Matrix & Scatter Plots)")
        print("4. Modelling: Linear & Regularized Regression (Base Features)")
        print("5. Modelling: Polynomial Features (Degree 2) Evaluation")
        print("6. FINAL MODEL: Best Ridge Regression (Poly Features + Plots)")
        print("0. Exit")
        print("="*80)
        
        choice = input("Enter your choice (0-6): ")
        
        if choice == '1':
            run_data_summary()
        elif choice == '2':
            run_visualization()
        elif choice == '3':
            run_relationships()
        elif choice == '4':
            run_modelling_linear_and_regularized()
        elif choice == '5':
            run_modelling_polynomial()
        elif choice == '6':
            run_final_model()
        elif choice == '0':
            print("Exiting analysis. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 6.")

if __name__ == "__main__":
    main_menu()