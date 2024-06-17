# Making imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats

from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.metrics import ConfusionMatrixDisplay

from sklearn.ensemble import RandomForestClassifier
from keras.models import Sequential
from keras.layers import Dense, Input, Dropout
from keras import callbacks
import pickle

# Reading in data
df = pd.read_csv('../Capstone/data/water_potability.csv')

# Converting to ppm scale
metrics_conv_dict = {
    'ph':1,
    'Hardness':1,
    'Solids':1,
    'Chloramines':1,
    'Sulfate':1,
    'Conductivity':0.55,
    'Organic_carbon':1,
    'Trihalomethanes':0.001,
    'Turbidity':3,
    'Potability':1
    }
for i in df.columns:
    df[i] = df[i] * metrics_conv_dict[i]

# Finding non null columns to train KNN imputer
non_null_cols = [i for i in df.columns if df[i].isna().sum()==0 and i not in ['Potability']]

# Initializing KNNimputer
knn_impute = KNNImputer(n_neighbors=7)

# Imputing nulls using KNN
for i in [x for x in df.columns if x not in non_null_cols]:
    df[i] = knn_impute.fit_transform(df[[i]])
    # non_null_cols.append(i)

# Splitting data into train-test split
X = df.drop('Potability', axis=1)
y = df['Potability']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Generating Random Forest pipeline
pipe2 = Pipeline([('scaler', StandardScaler()), ('rf_clf', RandomForestClassifier())])

param_grid2 = {
    'rf_clf__n_estimators':[400, 600, 800],
    'rf_clf__max_depth':[None, 3, 5]
}

# Generating grid
grid2 = GridSearchCV(pipe2, param_grid2, n_jobs=-1)

# Fitting on train data
grid2.fit(X_train, y_train)

with open('rf_model.pkl', 'wb') as f:
    pickle.dump(grid2, f)

