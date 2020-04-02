#!/usr/bin/python
# -*- coding: utf-8 -*-

# Flask
from flask import Flask, render_template, request


# Utilisation de la libraire random
from random import *
#Flask
app = Flask(__name__)


@app.route("/")
def Morpheus():

    return render_template('index.html')    

if __name__ == "__main__":
    # Précédemment debug = False. 
    # Mettre debug=True permet au serveur de relancer ce fichier après modification directement (sans avoir à redémarrer le serveur)
    app.run(host= '0.0.0.0',port=5000,debug=False)
