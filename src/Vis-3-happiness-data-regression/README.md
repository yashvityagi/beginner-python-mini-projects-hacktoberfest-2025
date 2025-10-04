## Interactive Happiness Data Analysis Script
This repository contains an interactive Python script that performs a complete machine learning analysis on the World Happiness Report data. The script is a refactored version of an extensive Jupyter Notebook, preserving all original data summaries, visualizations, model evaluations, and final conclusions.

Users can run the script and navigate an interactive command-line menu to explore different stages of the analysis, from initial data exploration to the final Ridge Regression model with polynomial features.

## Features
Interactive Menu: Navigate through the entire data analysis pipeline using simple terminal inputs.

Data Preparation: Includes automatic loading, missing value imputation (mean), and feature engineering (log transformations and polynomial features).

Comprehensive Evaluation: Runs and reports metrics (MSE, RMSE, R²) for four different models: Linear Regression, Lasso, Ridge, and ElasticNet.

Visualization: Generates the original Boxplots, Histograms, Correlation Heatmaps, and the final Residual Plots on demand.

Preserved Analysis: All text-based inferences and statistical conclusions from the original notebook are included and displayed upon selection.

## Setup and Installation
1. Prerequisites
You need a working installation of Python 3.x.

2. Required Libraries
The analysis relies on standard scientific Python libraries. You can install all necessary packages using pip:
pip install pandas numpy matplotlib seaborn scikit-learn

3. File Preparation
Ensure the following two files are in the same directory (folder) on your local machine:
happiness_data_analysis.py (The main script provided)
happiness_data.csv (The dataset used in the analysis)

## How to Run the Script
Open your terminal or command prompt.

Navigate to the directory where you saved your files:

cd /path/to/your/project/folder

Execute the script using the Python interpreter:

python happiness_data_analysis.py
Interactive Usage
Once the script starts, it will display the main menu. To select an analysis section, type the corresponding number (0-6) and press Enter.

Menu Option	Command	Description
Data Summary	1	Shows data structure, statistical summaries, and text-based inferences.

Visualization	2	Generates and displays Boxplots and Histograms. (Requires closing plot windows to continue).

Relationships	3	Displays the Correlation Matrix and Scatter Plots. (Requires closing plot windows to continue).

Modelling (Base Features)	4	Runs and prints evaluation metrics for Linear, Lasso, Ridge, and ElasticNet on the un-engineered features.

Modelling (Polynomial Features)	5	Runs and prints evaluation metrics for the four models on the Degree 2 Polynomial Features.

FINAL MODEL	6	Runs the final best model (Ridge α=0.01) and displays the key test metrics and residual plots.

Exit	0	Stops the script.

🔬 Final Model Summary
The analysis concludes that Ridge Regression applied to Degree 2 Polynomial Features is the best performing model.

Metric	Value (Approx.)
Test Set MSE	0.253
Test Set R² Score	0.795


The R2 of ≈0.795 indicates that the model successfully explains almost 80% of the variance in the target variable, 'Life Ladder' (Happiness Score).


## Author note: You need a GUI to view the plots. This is just an interactive app, the main script that is used for complete anyalsyis is the ipynb file of the same name which is also included in the repo.

