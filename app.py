from flask import Flask, render_template, request
from datetime import date
import pickle
import numpy as np
app = Flask(__name__)
model = pickle.load(open('XGBoost.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():    
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Year=date.today().year-Year
        Present_Price=float(request.form['Present_Price'])
        drived=int(request.form['Kms_Driven'])
        Owner=request.form['Owner']
        if (Owner == 0):
            Owner=0
        elif(Owner == 1):
            Owner=1
        else:
            Owner=3
        Fuel_Type_Petrol=request.form['Fuel_Type']
        Fuel_Type_Diesel=0
        if(Fuel_Type_Petrol=='Petrol'):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
        elif(Fuel_Type_Petrol=='Diesel'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
        Seller_Type_Individual=request.form['Seller_Type_Individual']
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0	
        Transmission=request.form['Transmission_Mannual']
        if(Transmission=='Mannual'):
            Transmission=1
        else:
            Transmission=0

        inpt=np.asarray([[Present_Price,drived,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission]])   
        prediction=model.predict(inpt)
        if prediction<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html', prediction_text="You Can Sell The Car at {}".format(prediction))
    else:
        return render_template('index.html')
    
if __name__=="__main__":
    app.run(debug=True)
