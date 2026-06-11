import numpy as np
import pandas as pd

df=pd.read_csv("Social_Network_Ads.csv")
print(df.head())

df=df.drop(columns=['User ID','Gender'])

X=df.drop(columns=['Purchased'])
y=df['Purchased']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
rf.fit(X_train,y_train)


#save the model
import joblib

joblib.dump(rf,'rf_model.pkl')
print("Model saved as rf_model.pkl")