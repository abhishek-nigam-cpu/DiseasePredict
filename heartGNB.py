import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import seaborn as sns

df = pd.read_csv('heartDataset.csv')
X=df.drop('Target',axis=1)
y=df['Target']
#print(y.head())

from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()

gnb.fit(X, y)

pickle.dump(gnb, open('heartGNB.pkl','wb'))

model = pickle.load(open('heartGNB.pkl','rb'))
print("result is",model.predict([[63,1,1,145,233,1,2,150,0,2.3,3,0,6]])[0])