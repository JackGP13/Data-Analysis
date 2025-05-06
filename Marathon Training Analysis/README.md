# Marathon  Training Analysis

## Project Overview
This project was a comprehensive analysis of personal marathon training data. The goal was to identify the most influential factors contributing to improved performance during long-distance running.

### Prerequisites: 
Python version 3.9.12 or later
Python libraries numpy, matplotlib, pandas, statsmodels, and scikit-learn

## Analysis Workflow

### Data Import and Preprocessing
Utilized Jupyter Notebooks for exploratory data analysis. The data had been manually entered into a csv file and checked for errors, so no preprocessing was done. 
Multivariate Linear Regression was first completed to identify the most significant predictor variables affecting marathon performance. Statsmodels was used for detailed Output: p-values, F-statistics, etc.

### Assumption Testing and Visualization
Visually inspected scatter plots of fitted vs residual values for homoscedasticity and also of independent variables to ensure linearity assumptions were met.

### LASSO Model with Scikit-learn
Implemented a LASSO regression model using scikit-learn to determine the optimal set of predictor variables that contribute most significantly to performance improvements. This would include more independent variables and check if my original choices for running the linear regression were optimal.

## Key Findings
While my original multivariate linear regression showed that run distance, the prior number of runs completed in the training regimen, and ambient humidity were statisticaly significant independent variables (p<0.05), during the GridSearchCV process for identifying the best alpha, an unexpected result was observed: all coefficients went to zero when optimizing for r^2. This outcome implies that the training regimen did not improve running speed but rather allowed maintainance of original pace while increasing distance covered. The LASSO model suggests that the training program focused on optimizing endurance rather than pure speed.

## Conclusion
This analysis demonstrates how data-driven insights can provide valuable feedback for personal marathon training programs. By leveraging machine learning techniques, individuals can refine their strategies to achieve optimal performance improvements. Manual entry errors may have possible led to errors in the analysis, and the next step will be imporation and processing of raw data from orignal source.
