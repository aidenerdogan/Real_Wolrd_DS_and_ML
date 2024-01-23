# Food Delivery Time Prediction Cutting Edge Realworld Problem ML Solution


![Food Develiry](imgs/boltcloneapp.jpg)

### Contents
- [Overview of the Project](#overview-of-the-project)
- [Source of Data](#source-of-data)
- [Link to the Website](#link-to-the-website)
- [Details of Implementation](#details-of-implementation)
    - [Approaches Employed](#approaches-employed)
    - [Technological Framework](#technological-framework)
    - [Utilized Python Packages](#utilized-python-packages)
- [Sequence of Steps](#sequence-of-steps)
- [Results and Criteria for Evaluation](#results-and-criteria-for-evaluation)
- [Future Enhancements](#future-enhancements)

  
## Overview of the Project
The primary aim of this project is to create a model that predicts food delivery times. Its purpose is to precisely estimate how long it will take for food to reach customers. Accurate delivery predictions can significantly improve customer satisfaction, streamline delivery operations, and boost overall efficiency for food delivery platforms.

## Source of Data
The dataset used for this project can be obtained from [here](https://www.kaggle.com/datasets/gauravmalik26/food-delivery-dataset).

It contains relevant information such as order details, location, city, delivery person information, weather conditions and actual delivery times.

## Link to the Website

You can access a demonstration of the food delivery time prediction model through this (link will be activated) on the web.

## Details of Implementation

### Approaches Employed
* Machine Learning
* Data Cleaning
* Feature Engineering
* Regression Algorithms

### Main Technological Frameworks
* Python
* Jupyter
* streamlit

### Utilized Python Packages
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* xgboost

## Sequence of Steps

1. Data Collection: Gathered the food delivery dataset from the provided data source.
2. Data Preprocessing: Performed data cleaning to handle missing values, outliers, and inconsistencies in the dataset. Conducted feature engineering to extract relevant features for the prediction model.
3. Model Development: Utilized regression algorithms to train a food delivery time prediction model. Explored different models such as linear regression, decision trees, random forests, xgboost to identify the best-performing model.
4. Model Evaluation: Evaluated the performance of the models using appropriate metrics such as mean squared error (MSE),root mean squared error (RMSE) and R2 score.
5. Deployment: Deployed the food delivery time prediction model as a standalone application for real-time predictions.

## Results and Criteria for Evaluation

Based on the evaluation results, the best-performing model was **XGBoost** with R2 score of **0.82**

## Future Enhancements

The project holds promising avenues for future enhancements:

* Expand feature inclusion by integrating delivery partner details like working start time and end time etc., current real time weather conditions, or traffic patterns to elevate prediction precision.
* Engage in extensive data analysis to uncover deeper patterns or correlations that could enrich prediction accuracy.
* More data and time resies analysis to understand time patterns
* Try some NN models to better understanding.
* Refine model parameters for potential performance enhancements.





