import random
from flask import Flask
import json
# importation de la bibliothèque
import requests
import pickle

model = pickle.load(open("model.pkl", "rb"))
prediction = model.predict([0,0,0,0])
print(prediction)

# récupération du contenu à l'aide de la méthode get()
"""r = requests.get("https://jsonplaceholder.typicode.com/posts")

app=Flask(__name__)
@app.route("/test", methods=["GET"])
def test_get():
    return r.json()[random.randint(0,20)]

@app.route('/enregistrement',methods=['POST'])
def enregistrement():
    pass


if __name__ == '__main__':
    app.run(debug=True)
    print("lancement")"""
