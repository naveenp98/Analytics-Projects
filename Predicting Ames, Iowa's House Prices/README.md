# House Price Prediction - Analyzing Ames Housing Data
House price prediction refers to the process of using data analysis, statistical modeling, and machine learning techniques to forecast the future prices of residential properties.
House price prediction models are typically built using historical sales data and other relevant information to train a predictive algorithm. 
These models aim to identify patterns and relationships between the features of a property and its sale price.

In this project, we aim to use the Ames Housing Data to create a machine learning solution that accurately predicts house prices. The house price is the 'SalePrice' variable in the dataset.

# Problem Statement
How do we accurately predict the price of a house?
Do non-continous variables affect the price of a house?

# Data Dictionary
The data dictionary consists of over 80 columns. A thorough analysis of each variable is present in the [data description](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)

# Executive Summary
The project consists of 2 datasets, the train and test datasets. The analysis required training on the train data and submitting predictions on Kaggle using test data.

Columns were grouped according to nominal, ordinal, discrete and numeric among others, to ease with transformations that may arise.

Initially, summary statistics and an analysis of missing-ness of data was conducted. 
This helped understanding the data types available, the completeness of the data and if transformations/filtering was required. 
After this, histograms and scatter plots were constructed to visualise distributions and understand spread in accordance with the target variable respectively.

Numeric columns has their missing values handled by analyzing their distributions.

Then a correlation matrix was developed with the primary focus of understanding the relationship between predictor variables and SalePrice. 
All variables that had over a threshold of 0.4 correlation with SalePrice were selected.

Out of all columns selected, only one had missing values and since it was highly correlated with another variable that possesed no nulls, this column was dropped.

6 models were created, some simple while some others a bit complex. 
All models provided an output in the output folder. The best RMSE on the test data attained was 24396.28268 from the final model.