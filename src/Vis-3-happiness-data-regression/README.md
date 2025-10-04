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
