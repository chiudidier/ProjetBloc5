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

@app.route("/Red_pill")
def Chase_the_white_rabbit():
    #le shuffle est géré par la route /shuffle
    
    #A modifier plus tard
    
    #shufflelist=['1','2','4','3','9','7','6','8','5']
    
    # On passe la liste de question et la liste des types en paramètres à questionnaire.html
    #return render_template('taquin.html', depart=shufflelist) #même nom de var dans jinja html
    return "Warning, cette route n'est pas encore configurée"

@app.route('/shuffle')
def retourJS():
    # Récupération de ce qui a été envoyé par JS (ici une chaine de caractères)
    fromJS = request.args.get('argument1', type = str)
    #print("\nCe que j'ai reçu de JS", fromJS)
          
    # Préparation de la réponse à envoyer à JS
    if (fromJS != "None"):
        if (fromJS == "melange"):
            #la variable renvoyée à JS doit être un string, tuple, response instance ou WSGI callable
            pingpong = "6B5D8H7D4B1B2G3G5H"
        else:
            pingpong="NULL"
    else:
        pingpong="None bizarre"
    return(pingpong)

if __name__ == "__main__":
    # Précédemment debug = False. 
    # Mettre debug=True permet au serveur de relancer ce fichier après modification directement (sans avoir à redémarrer le serveur)
    app.run(host= '0.0.0.0',port=5000,debug=True)
