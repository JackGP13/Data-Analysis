# Project Overview
A collection of data analysis projects using Python and R. Each folder contains a  Jupyter Notebooks and a project-level README with more detail. The datasets used in these projects come from a mix of sources (listed below), including personal data.

## Repository Structure
The repository is organized into multiple folders, each containing a separate project:

### Marathon Training Analysis: Python
I manually exported my Apple Health data across a full training cycle and tried to build a model that could predict my marathon race time. Used multivariate linear regression and LASSO regularization to find the variables that actually mattered. Ambient temperature turned out to be the dominant predictor, even more than total distance. Validated the model's predicted range against three prior race results.

### Rivian EV Pricing Analysis: R
A marketing analytics project from UC Berkeley Haas. Used survey data from a third-party firm to model customer willingness-to-pay for a Rivian SUV and identify the optimal price point. Analysis found that younger, politically liberal men showed the highest willingness to pay, suggesting where Rivian's marketing spend would have the most impact.

### Diamond Price Prediction: R
Regression analysis on a Kaggle dataset to predict diamond prices from cut, color, clarity, and carat. Primarily an exercise in exploratory data analysis and feature engineering.

...
## Datasets Used
Some datasets used in these projects are sourced from online repositories, while others are based on personal experience. The following online sources were used:

My own Apple Health data

Survey Data provided by third-party marketing firm

Kaggle Datasets


For more information on the specific datasets used for each project, please refer to their respective README files or documentation.

## Software Requirements
To run and view the code for these projects, you'll need:

R (version 3.6.1 or later) with necessary packages installed (dplyr, glmnet, randomforest, etc.)
Python (version 3.12.9 or later) with necessary libraries installed (pandas, numpy, matplotlib, etc.)
Jupyter Notebook

# Getting Started
Clone the repository to your local machine using Git.
Install required software and packages as mentioned above.
For R projects, create a new R environment and install necessary packages using install.packages() commands in the console.
For Python projects, activate the relevant Python environment using conda or similar package managers.

# Project Documentation
Each project contains its own README file with more detailed information on:

# Project objectives
Data sources and processing steps
Analysis methodology
Results and findings
Please consult these individual README files for specific details about each project.

# Contributions and Feedback
Feel free to fork this repository, contribute your own projects or datasets, or provide feedback on existing work. I'm always interested in discussing data analysis approaches and learning from others!
