# Math Score Prediction with Random Forest

This project uses a **Random Forest Regressor** to predict student math scores based on demographic and academic performance data. The model is built using Python with the `scikit-learn` and `pandas` libraries and demonstrates a robust data preprocessing pipeline to handle both numerical and categorical features.

## Features

* **Machine Learning Model:** Implements a `RandomForestRegressor`, an effective ensemble learning method for high-accuracy regression tasks.
* **Data Preprocessing:** Uses a `scikit-learn` `Pipeline` to streamline data transformation, including `OneHotEncoder` for handling categorical features cleanly.
* **Clear Feature Engineering:** Explicitly separates numerical and categorical features for clean, readable, and maintainable code.
* **Comprehensive Evaluation:** Measures model performance using standard regression metrics: Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared ($R^2$).

## Performance Metrics

The model was trained and evaluated, yielding the following performance on the test dataset:

* **Mean Absolute Error (MAE):** 4.71
* **Root Mean Squared Error (RMSE):** 6.04
* **R-squared ($R^2$):** 0.85

An **R-squared value of 0.85** indicates that the model successfully explains approximately 85% of the variance in the students' math scores, highlighting its strong predictive power.

## How to Run

I would highly advise to run this ML Model on Google Colab it has preinstalled libraries for running ML Models.
* **Clone the project on your local machine.
* **Upload the .ipynb i.e the jupyter notebook file on drive and open it on google colab.
* **Do not forget to add both the datasets on google colab before running the model.