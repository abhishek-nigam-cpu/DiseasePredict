import numpy as np
# from flask_mobility import Mobility
from flask import Flask, request, jsonify, render_template,redirect
import pickle
import sqlite3
import pandas as pd
app = Flask(__name__)
def get_db_connection():
    conn = sqlite3.connect('disPred.db')
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/home')
def home2():
    return render_template('home.html')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login_validation',methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    # return "done"
    conn=get_db_connection()
    cur=conn.cursor()
    #cur.execute("INSERT INTO users (ID,NAME,PASSWORD) VALUES (?,?,?)",("new@gmail.com","Rahul Sharma","1234567") )
    cur.execute("select * from users where ID=? and PASSWORD=?",(email,password))
    user=cur.fetchall()
    if(len(user)>0):
        return redirect('/home')
    else:
        return redirect('/')

@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/add_user',methods=['POST'])
def add_user():
    email=request.form.get('email')
    fname=request.form.get('fname')
    # lname=request.form.get('lname')
    pwd=request.form.get('pwd')
    pwdc=request.form.get('pwdc')
    name=fname
    #establishing connection with database named "disPred"
    # return "done"
    if(pwd!=pwdc):
        return redirect('/register')
    conn=get_db_connection()
    cur=conn.cursor()
    cur.execute("select * from users where ID=?",(email,))
    check_user=cur.fetchall()
    if(len(check_user)>0):
        return redirect('/register')
    cur.execute('INSERT INTO users (ID,NAME,PASSWORD) VALUES (?,?,?)',(email,name,pwd))
    conn.commit()
    return redirect('/')


@app.route('/heart')
def heart():
    return render_template('heart.html')

@app.route('/predicth',methods=['POST'])
def predicth():
    int_f=list(request.form.values())
    # res={}
    # res={"int":int_f}
    # return res
    if(int_f[0]=='1'):
        int_f[0]="KNN Classifier"
        model = pickle.load(open('heartKNN.pkl', 'rb'))
    elif(int_f[0]=='2'):
        int_f[0]="Random Forest Classifier"
        model = pickle.load(open('heartRFC.pkl', 'rb'))
    elif(int_f[0]=='3'):
        int_f[0]="Naive Bayes Classifier"
        model = pickle.load(open('heartGNB.pkl', 'rb'))
    temp_f=int_f[1:]
    temp_f=[float(x) for x in temp_f]
    final_features = [temp_f]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    # pred_text=""
    # if output==1:
    #     pred_text="There is no problem in the patient's liver"
    # else:
    #     pred_text="Patient is suffering from liver disease"
    #Table preparation to display
    headings=["Prediction Model","Age","Gender","Chest pain type","Resting Blood Pressure","cholestrol","Fasting blood sugar","Rest ECG","MHRA","Excercised Induced Angina","ST_depression","slope","Major Vessels","Thallessemia","Prediction Remarks"]
    if(int_f[0]==1):
        int_f[0]="KNN Classifier"
    elif(int_f[0]==2):
        int_f[0]="Random Forest Classifier"
    if(int_f[2]==0):
        int_f[2]="Female"
    else:
        int_f[2]="Male"
    int_f.append(output)
    # dictr={"res":int_f}
    # return dictr
    data=[int_f]
    return render_template('heart.html',headings=headings,data=data)

@app.route('/ILPD')
def ILPD():
    return render_template('ILPD.html')

@app.route('/predict',methods=['POST'])
def predict():
    # model = pickle.load(open('ILPDKNN.pkl', 'rb'))
    # int_features = [float(x) for x in request.form.values()]
    int_f=list(request.form.values())
    if(int_f[0]=='1'):
        int_f[0]="KNN Classifier"
        model = pickle.load(open('ILPDKNN.pkl', 'rb'))
    elif(int_f[0]=='2'):
        int_f[0]="Random Forest Classifier"
        model = pickle.load(open('ILPDrfc.pkl', 'rb'))
    # if(int_f[1]=='Female'or int_f[1]=='female'):
    #     int_f[1]=0
    # else:
    #     int_f[1]=1
    temp_f=int_f[1:]
    # dictr={"res":int_f}
    # return dictr
    # del temp_f[0]
    temp_f=[float(x) for x in temp_f]
    # final_features = [np.array(temp_f)]
    final_features = [temp_f]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    pred_text=""
    if output==1:
        pred_text="There is no problem in the patient's liver"
    else:
        pred_text="Patient is suffering from liver disease"
    #Table preparation to display
    headings=["Prediction Model","Age","Gender","Total Bilirubin","Direct Bilirubin","Total Proteins","Albumin","AG Ratio","SGPT","SGOT","Alkphos","Prediction Remarks"]
    if(int_f[0]==1):
        int_f[0]="KNN Classifier"
    elif(int_f[0]==2):
        int_f[0]="Random Forest Classifier"
    if(int_f[2]==0):
        int_f[2]="Female"
    else:
        int_f[2]="Male"
    int_f.append(pred_text)
    # dictr={"res":int_f}
    # return dictr
    data=[int_f]
    return render_template('ILPD.html', headings=headings,data=data,prediction_text='{}'.format(pred_text))

@app.route('/covid')
def covid():
    return render_template('covid.html')

@app.route('/predCovid',methods=['POST'])
def predCovid():
    int_f=list(request.form.values())
    # res={}
    # res={"int":int_f}
    # return res
    if(int_f[0]=='1'):
        int_f[0]="Random Forest Classifier"
        model = pickle.load(open('covidRFC.pkl', 'rb'))
    elif(int_f[0]=='2'):
        int_f[0]="Decision"
        model = pickle.load(open('covidTree.pkl', 'rb'))
    elif(int_f[0]=='3'):
        int_f[0]="KNN classfier"
        model = pickle.load(open('covidKNN.pkl', 'rb'))
    temp_f=int_f[1:]
    temp_f=[float(x) for x in temp_f]
    final_features = [temp_f]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    pred_text=""
    if output==1:
        pred_text="Result is Positive"
    else:
        pred_text="Result is Negative"
    #Table preparation to display
    headings=['Prediction Model','Breathing Problem', 'Fever', 'Dry Cough', 'Sore throat', 'Hyper Tension', 'Abroad travel', 'Contact with COVID Patient', 'Attended Large Gathering', 'Visited Public Exposed Places', 'Family working in Public Exposed Places', 'COVID-19']
    int_f.append(pred_text)
    for i in range(len(int_f)):
        if(int_f[i]=='1'):
            int_f[i]="Yes"
        elif(int_f[i]=='0'):
            int_f[i]="No"
    # dictr={"res":int_f}
    # return dictr
    data=[int_f]
    return render_template('covid.html',headings=headings,data=data)
# @app.route('/results',methods=['POST'])
# def results():

#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)