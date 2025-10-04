<<<<<<< HEAD
## Interactive Happiness Data Analysis Script
This repository contains an interactive Python script that performs a complete machine learning analysis on the World Happiness Report data. The script is a refactored version of an extensive Jupyter Notebook, preserving all original data summaries, visualizations, model evaluations, and final conclusions.
=======
##Happiness Data Analysis
>>>>>>> origin/main

Users can run the script and navigate an interactive command-line menu to explore different stages of the analysis, from initial data exploration to the final Ridge Regression model with polynomial features.

## Features
Interactive Menu: Navigate through the entire data analysis pipeline using simple terminal inputs.

Data Preparation: Includes automatic loading, missing value imputation, and feature engineering (log transformations and polynomial features).

<<<<<<< HEAD
Comprehensive Evaluation: Runs and reports metrics (MSE, RMSE, R²) for four different models: Linear Regression, Lasso, Ridge, and ElasticNet.
=======
##Requirements & Dependencies
>>>>>>> origin/main

Visualization: Generates the original Boxplots, Histograms, Correlation Heatmaps, and the final Residual Plots on demand.

Preserved Analysis: All text-based inferences and statistical conclusions from the original notebook are included and displayed upon selection.
## Setup and Installation
1. Prerequisites
You need a working installation of Python 3.x.

2. Required Libraries
The analysis relies on standard scientific Python libraries. You can install all necessary packages using pip:

Bash

<<<<<<< HEAD
pip install pandas numpy matplotlib seaborn scikit-learn
3. Files Required
Ensure the following two files are in the same directory on your local machine:
=======
##Key Features
>>>>>>> origin/main

happiness_analysis_interactive.py (The main script provided)

happiness_data.csv (The dataset used in the analysis)
## How to Run the Script
Open your terminal or command prompt.

Navigate to the directory where you saved your files:

Bash

cd /path/to/your/project/folder
Execute the script using the Python interpreter:

Bash

python happiness_analysis_interactive.py
Interactive Usage
Once the script starts, it will first confirm that the data is loaded and then display the main menu:

================================================================================
    SELECT ANALYSIS SECTION FROM ORIGINAL NOTEBOOK
================================================================================
1. Data Summary & Basic Statistics
2. Visualization (Boxplots, Histograms, Skewness)
3. Relationships (Correlation Matrix & Scatter Plots)
4. Modelling: Linear & Regularized Regression (Base Features)
5. Modelling: Polynomial Features (Degree 2) Evaluation
6. FINAL MODEL: Best Ridge Regression (Poly Features + Plots)
0. Exit
================================================================================
Enter your choice (0-6):
Note on Plots: When you select options 2, 3, or 6, the script will open visual plots (e.g., boxplots or scatter plots). You must close the plot windows to return to the main menu and continue the analysis.

<<<<<<< HEAD
## Analysis Summary
The final and best-performing model identified by the analysis is Ridge Regression applied to Degree 2 Polynomial Features.
=======
##Steps to Run Locally
>>>>>>> origin/main

Metric	Value (Approx.)
Test Set MSE	0.253
Test Set R² Score	0.795

Export to Sheets
This strong R² indicates that the model explains approximately 79.5% of the variance in the 'Life Ladder' (Happiness Score) using the engineered features.

🛠️ Script Structure (For Developers)
The code is organized into modular functions:

setup_data(): Runs once at startup to load, impute, split, and prepare both the base and polynomial datasets.

evaluate_model(...): A helper function that performs 3-fold cross-validation and calculates final test metrics.

run_data_summary(), run_visualization(), etc.: These functions correspond to the menu options and contain the logic, original analysis text, and plotting commands for each section.

<<<<<<< HEAD
main_menu(): The control loop that handles user input and calls the appropriate analysis function.
=======
Happiness_data_analysis.ipynb


Run all cells

Run each cell sequentially (Shift + Enter),
or use Kernel → Restart & Run All to execute the entire notebook.

##Dataset Information

The dataset includes the following columns:

Year

Life Ladder (target variable)

Log GDP per capita

Social support

Healthy life expectancy at birth

Freedom to make life choices

Generosity

Perceptions of corruption

and several other socio-economic indicators.

Outliers and missing values are handled thoughtfully to maintain data integrity.

##Output & Results

Correlation matrix and feature importance visualizations

Regression metrics (MAE, RMSE, R²) for each model

Comparison of regularization effects on model performance

Interpretation of top factors influencing life satisfaction

🧑‍💻 Author

Sanskar Srivastava
>>>>>>> origin/main
