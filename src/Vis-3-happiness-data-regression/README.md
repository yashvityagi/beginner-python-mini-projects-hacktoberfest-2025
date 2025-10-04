#Happiness Data Analysis


This project analyzes global happiness data to understand which socio-economic and health-related factors most strongly influence a country's life satisfaction (Life Ladder).
It involves data cleaning, exploratory data analysis (EDA), outlier handling, feature transformation, and regression modeling (Linear, Polynomial, Ridge, Lasso, Elastic Net, and SGD).

The notebook walks through each step — from importing data to model evaluation — and provides insights into the key drivers of happiness across countries and years.

#Requirements & Dependencies

Make sure the following packages are installed in your Python environment:
pip install numpy pandas matplotlib seaborn scikit-learn scipy

If you plan to run it inside Jupyter Notebook or VS Code, also install:
pip install jupyterlab

Python Version

Python 3.8 or higher is recommended.

#Key Features

Data exploration and visualization

Handling missing values and outliers (via Winsorization)

Log transformation for skewed variables

Correlation and feature analysis

Polynomial feature expansion

Regression modeling (Linear, Ridge, Lasso, Elastic Net, SGD)

Cross-validation and model comparison

Insights into the most influential happiness indicators

#Steps to Run Locally

Clone or download the repository


Install dependencies

pip install numpy pandas matplotlib seaborn scikit-learn scipy

Launch Jupyter Notebook
Open the notebook

From the browser tab that opens, select:

Happiness_data_analysis.ipynb


Run all cells

Run each cell sequentially (Shift + Enter),
or use Kernel → Restart & Run All to execute the entire notebook.

#Dataset Information

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

#Output & Results

Correlation matrix and feature importance visualizations

Regression metrics (MAE, RMSE, R²) for each model

Comparison of regularization effects on model performance

Interpretation of top factors influencing life satisfaction

🧑‍💻 Author

Sanskar Srivastava