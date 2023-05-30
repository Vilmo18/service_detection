import random
from flask import Flask
import json
# importation de la bibliothèque
import requests
import pickle
import json
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import pandas as pd
import requests
import random as rd
from bson.json_util import dumps
import pickle


app = Flask(__name__)
CORS(app)
mongo_db = PyMongo(app, uri='mongodb://127.0.0.1:27017/minfopra')
db = mongo_db.db


@app.route('/detection/update')
def transaction():
    """model = pickle.load(open("model.pkl", "rb"))
    prediction = model.predict([0, 0, 0, 0])
    print(prediction)"""
    # id=requests.args.get('id')
    val = []
    result = db.agents.find()
    j = 0
    model = pickle.load(open("detection.pkl", "rb"))
    for i in result:
        prediction = model.predict(
            [[i['diff_recens'], i['diff_conges'], i['diff_travail'], i['actif']]])
        if (prediction[0] == 'fraude'):
            val.append(i)
            print(prediction[0])
            print(val[j], end='\n')
            # ajout dans ma bd transaction
            db.detected.insert_one(val[j])
            # Suppresion dans la agents des frauduleux
            db.agents.delete_one({'matricule': val[j]['matricule']})
            j = j+1
    return json.loads(dumps(val))


# Function which is used for list of detected
@app.route('/Agent/fraud_detected')
def solde():
    # id=requests.args.get('id')
    val = []
    result = db.detected.find()
    for i in result:
        val.append(i)
    return json.loads(dumps(val))


if __name__ == '__main__':
    app.run(debug=True, port=6000)
    print("lancement")

# récupération du contenu à l'aide de la méthode get()
"""r = requests.get("https://jsonplaceholder.typicode.com/posts")

app=Flask(__name__)
@app.route("/test", methods=["GET"])
def test_get():
    return r.json()[random.randint(0,20)]

@app.route('/enregistrement',methods=['POST'])
def enregistrement():
    pass
"""
