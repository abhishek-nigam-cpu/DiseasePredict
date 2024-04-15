import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import seaborn as sns

df = pd.read_csv('heartDataset.csv')

#df.drop('age',axis=1,inplace=True)
#df.drop('gender',axis=1,inplace=True)
#df.gender[df.gender == 'Male'] = 1
#df.gender[df.gender == 'Female'] = 2
#df['gender'].replace(['Female','Male'],[0,1],inplace=True)
#print(df['gender'])
#modelling
X=df.drop('Target',axis=1)
y=df['Target']
#print(y.head())

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()

knn.fit(X, y)

pickle.dump(knn, open('heartKNN.pkl','wb'))

model = pickle.load(open('heartKNN.pkl','rb'))
print("result is",model.predict([[63,1,1,145,233,1,2,150,0,2.3,3,0,6]])[0])