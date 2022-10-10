from flask import Flask, request, jsonify
import os
import pickle
#from sklearn.model_selection import cross_val_score
import pandas as pd

#import sqlite3
#from datetime import datetime

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def hello():
    return  "<h1>Bienvenido a la página principal del servicio ofrecido por Nomedalavidaenello</h1>\
            <p><h5>web realizada por Javier Tenorio</h5></p>\
            <p><h2>Servicio generado para estudiar si una campaña en Twitter será existosa o no</h2></p>"
#            <p><h3>Introduzca aqui el Tweet a estudiar:</h3></p"
            

# --PREDICCIÓN--
@app.route('/predict', methods=['GET'])
def predict():
    model = pickle.load(open('model\sentiment_model','rb'))
    
    text = request.args.get('text', None)
    file={'text':text}
    df_test=pd.DataFrame()
    df_test['text']=file

    
    if text is None:
        return "Faltan argumentos para realizar la predicción"

    prediction = model.predict(df_test)

    if prediction == 0:
         return 'El TEXTO no genera impacto.'
    else:
         return 'Ha conseguido un  TEXTO exitoso, le recomendamos que lo publique'








#app.run()