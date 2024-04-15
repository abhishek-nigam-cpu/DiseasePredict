import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import seaborn as sns

df = pd.read_csv('ILPD.csv')

#dataset['rate'].fillna(0, inplace=True)

#dataset['sales_first'].fillna(dataset['sales_first'].mean(), inplace=True)
#print(df.isna().sum())
'''corr_matrix = df.corr()
fig, ax = plt.subplots(figsize=(15, 10))
ax = sns.heatmap(corr_matrix,
                 annot=True,
                 linewidths=0.5,
                 fmt=".2f",
                 cmap="YlGnBu");
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)'''
#df.drop('age',axis=1,inplace=True)
#df.drop('gender',axis=1,inplace=True)
#df.gender[df.gender == 'Male'] = 1
#df.gender[df.gender == 'Female'] = 2
df['gender'].replace(['Female','Male'],[0,1],inplace=True)
#print(df['gender'])
#modelling
X=df.drop('target',axis=1)
y=df['target']
#print(y.head())

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()

knn.fit(X, y)

pickle.dump(knn, open('ILPDKNN.pkl','wb'))

model = pickle.load(open('ILPDKNN.pkl','rb'))
print("result is",model.predict([[65,1,0.7,0.1,187,16,18,6.8,3.3,0.9]])[0])