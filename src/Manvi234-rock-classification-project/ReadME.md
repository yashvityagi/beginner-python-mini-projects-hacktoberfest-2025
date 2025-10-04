# Rock Classification Project

## Description

This project focuses on the classification of rocks into three distinct categories. It utilizes a machine learning approach to classify rock samples based on a set of 11 features. The goal is to build and evaluate different classification models to find the one that performs best on the given dataset. 🪨

-----

## How to Run

1.  **Install Dependencies:** Make sure you have Python installed, and then install the necessary libraries using pip:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn
    ```
2.  **Data:** Place the `aggregateRockData.xlsx` and `feature_presence540.txt` files in the same directory as the Jupyter Notebook.
3.  **Run the Notebook:** Open and run the `Rock_Classification.ipynb` notebook in a Jupyter environment. Execute the cells in order to see the data loading, preprocessing, model training, and evaluation steps.

-----

## Dependencies

  * **pandas**
  * **numpy**
  * **matplotlib**
  * **seaborn**
  * **scikit-learn**

-----

## Dataset

The project uses two data files:

  * `aggregateRockData.xlsx`: This file contains the labels for the rock samples.
  * `feature_presence540.txt`: This file contains 11 features for each rock sample.

These two files are merged to create a single dataset of 480 samples with 11 features and one target label.

-----

## Models Implemented

The following machine learning models are used for the classification task:

  * **Random Forest Classifier**
  * **AdaBoost Classifier**
  * **Gradient Boosting Classifier**
  * **Stacking Classifier**
  * **Support Vector Machine (SVM)**
  * **Logistic Regression**

-----

## Evaluation

The performance of the models is evaluated using the following metrics:

  * **Classification Report**
  * **Confusion Matrix**
  * **Accuracy Score**
  * **Precision Score**
  * **Recall Score**
  * **F1 Score**
