import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn import svm
#from dataprep.eda.missing import plot_missing
e=LabelEncoder()
covid = pd.read_csv('Covid Dataset.csv')

#df.drop('age',axis=1,inplace=True)
#df.drop('gender',axis=1,inplace=True)
#df.gender[df.gender == 'Male'] = 1
#df.gender[df.gender == 'Female'] = 2
#df['gender'].replace(['Female','Male'],[0,1],inplace=True)
#print(df['gender'])
#modelling
#print(df.head())
#Transforming Yes/No to 1/0
"""covid['Breathing Problem']=e.fit_transform(covid['Breathing Problem'])
covid['Fever']=e.fit_transform(covid['Fever'])
covid['Dry Cough']=e.fit_transform(covid['Dry Cough'])
covid['Sore throat']=e.fit_transform(covid['Sore throat'])
covid['Running Nose']=e.fit_transform(covid['Running Nose'])
covid['Asthma']=e.fit_transform(covid['Asthma'])
covid['Chronic Lung Disease']=e.fit_transform(covid['Chronic Lung Disease'])
covid['Headache']=e.fit_transform(covid['Headache'])
covid['Heart Disease']=e.fit_transform(covid['Heart Disease'])
covid['Diabetes']=e.fit_transform(covid['Diabetes'])
covid['Hyper Tension']=e.fit_transform(covid['Hyper Tension'])
covid['Abroad travel']=e.fit_transform(covid['Abroad travel'])
covid['Contact with COVID Patient']=e.fit_transform(covid['Contact with COVID Patient'])
covid['Attended Large Gathering']=e.fit_transform(covid['Attended Large Gathering'])
covid['Visited Public Exposed Places']=e.fit_transform(covid['Visited Public Exposed Places'])
covid['Family working in Public Exposed Places']=e.fit_transform(covid['Family working in Public Exposed Places'])
covid['Wearing Masks']=e.fit_transform(covid['Wearing Masks'])
covid['Sanitization from Market']=e.fit_transform(covid['Sanitization from Market'])
covid['COVID-19']=e.fit_transform(covid['COVID-19'])
covid['Dry Cough']=e.fit_transform(covid['Dry Cough'])
covid['Sore throat']=e.fit_transform(covid['Sore throat'])
covid['Gastrointestinal ']=e.fit_transform(covid['Gastrointestinal '])
covid['Fatigue ']=e.fit_transform(covid['Fatigue '])"""
#Transforming Yes/No to 1/0
for column in covid:
    covid[column]=e.fit_transform(covid[column])

covid=covid.drop('Running Nose',axis=1)
covid=covid.drop('Chronic Lung Disease',axis=1)
covid=covid.drop('Headache',axis=1)
covid=covid.drop('Heart Disease',axis=1)
covid=covid.drop('Diabetes',axis=1)
covid=covid.drop('Gastrointestinal ',axis=1)
covid=covid.drop('Wearing Masks',axis=1)
covid=covid.drop('Sanitization from Market',axis=1)
covid=covid.drop('Asthma',axis=1)
covid=covid.drop('Fatigue ',axis=1)

X=covid.drop('COVID-19',axis=1)
y=covid['COVID-19']

RFC=RandomForestClassifier()
RFC.fit(X,y)
print("RFC:",RFC.score(X,y))

tree = tree.DecisionTreeClassifier()
tree.fit(X,y)
print("Tree:",tree.score(X,y))

KNN=KNeighborsClassifier(n_neighbors=20)
KNN.fit(X,y)
print("KNN:",KNN.score(X,y))



pickle.dump(RFC, open('covidRFC.pkl','wb'))
pickle.dump(tree, open('covidTree.pkl','wb'))
pickle.dump(KNN, open('covidKNN.pkl','wb'))

model = pickle.load(open('covidTree.pkl','rb'))
print("result is",model.predict([[1,0,0,1,0,0,0,1,0,1]])[0])