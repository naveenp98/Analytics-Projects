# Predicting the potability of water using Machine Learning

## Problem Statement
The importance of water quality cannot be understated. The lack of access to safe and clean water is one of the largest risk factors for the spread of infectious diseases, such as polio, typhoid, cholera, dysentery, hepatitis, and diarrhea. The unavailability of drinkable water worsens and intensifies malnutrition, particularly in children. [1](https://healingwaters.org/what-is-the-importance-of-water-quality/#:~:text=The%20Importance%20of%20Access%20to%20Safe%20and%20Clean%20Water&text=The%20lack%20of%20access%20to,dysentery%2C%20hepatitis%2C%20and%20diarrhea.)

In this project, we will explore the use of machine learning algorithms to predict the potability of water based on various physical and chemical properties. The dataset we will be using contains 3276 water samples . The dataset includes information such as pH, conductivity, dissolved oxygen, and other physical and chemical properties. Our goal is to build a machine learning model that can accurately predict the potability of water based on these properties.

## Dataset
The Dataset is from Kaggle and is available here - [Link](https://www.kaggle.com/datasets/nayanack/water-probability)

## Data Dictionary

- **Variable Name** | **Description** | **Data Type**
- **pH** | pH of the water (measured in pH units). | float

- **Hardness** | Hardness of the water (measured in mg/L). | float

- **Solids** | Total dissolved solids in the water (measured in ppm). | float

- **Chloramines** | Amount of chloramines in the water (measured in ppm). | float

- **Sulfate** | Amount of sulfate in the water (measured in mg/L). | float

- **Conductivity** | Conductivity of the water (measured in μS/cm). | float

- **Organic_carbon** | Amount of organic carbon in the water (measured in ppm). | float

- **Trihalomethanes** | Amount of trihalomethanes in the water (measured in μg/L). | float

- **Turbidity** | Turbidity of the water (measured in NTU). | float

- **Potability** | Potability of the water (1 indicates potable, 0 indicates non-potable). | float


## Summary
The dataset was first explored to understand the distribution between features, presence of outliers and missing values. With missing values imputed while maintaning the natural distribution of each variable, the dataset was ready for modeling.

After establishing a simple baseline, 5 models were developed. Each model included a standard scaler to scale values and a normalizer to deal with outliers and transform the data within a pipeline. Most models included a grid search for hyperparameter tuning. The final model included the use of polynomial features in an attempt to obtain best performance.

The models were Logistic Regression, Random Forest Classifier, Simple Neural Network, grid-searched Neural Network and a Polynomial Feature-Random Forest Classifier. The final model was the best performing model with an accuracy of 70%.

## Demonstration
To demonstrate the model, the following link can be used - [Link](https://potablewater.streamlit.app/)
The model utilised for the app is the first Random Forest Classifier which has similar performance to the best performing model.

## Conclusion
The models generated, at best, provided an accuracy of ~70%. To improve these numbers a number of other techniques can be explored including - 
- Feature engineering
- Data augmentation
- Hyperparameter tuning
- Ensemble learning

## Acknowledgements
- [Kaggle](https://www.kaggle.com/)
- [Streamlit](https://streamlit.io/)
