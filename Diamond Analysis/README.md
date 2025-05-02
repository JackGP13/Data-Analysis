# Project: Predicting Diamond Prices
## Overview
This project aims to develop predictive models for diamond prices using various methods. We'll explore the relationship between diamond attributes (carat, cut, clarity, and color) and their corresponding prices.

## Data Source
The dataset used in this project is based on publicly available data from the Kaggle Diamonds Dataset . This dataset contains 53940 entries across various attributes.

## Methodology
This project involves multiple steps:

Data Preprocessing: Clean and preprocess the data by handling missing values, encoding categorical variables.
Modeling:
Linear Regression with Lasso Regularization: Use glmnet package in R to perform least squares regression using Lasso regularization.
Unpruned Decision Trees: Implement decision trees using the rpart package in R and evaluate their performance on the dataset.
Pruned Decision Trees: Utilize the rpart package to prune the decision trees and improve generalization.
Random Forests: Employ the randomForest package in R to create an ensemble model combining multiple decision trees.

## R Scripts
The project includes three Jupyter Notebook files:

data_preprocessing.Rmd: Contains code for data cleaning, encoding, and preprocessing.
modeling.Rmd: Implements the modeling steps (Lasso regression, unpruned and pruned decision trees, and random forests).
results.Rmd: Summarizes model performance metrics (e.g., R-squared, mean squared error) and visualizations.

## Results
The project evaluates each model using various metrics:

Mean Squared Error (MSE)
Root Mean Squared Percentage Error (RMSPE)
R-squared value
Coefficient of Determination (R^2)
We'll compare the performance of each model to determine which one provides the best predictions.

## Requirements
To run this project, you'll need:

R (version 3.6.1 or later) with necessary packages installed (glmnet, randomForest, etc.)
Jupyter Notebook
A compatible Python environment for running the notebooks (optional)
This project aims to serve as a starting point for further exploration and improvement of diamond price prediction models!