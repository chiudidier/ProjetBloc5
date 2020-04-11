#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 12:37:34 2020

@author: d.chiu, n.vaz-pinto
"""

#============================
# Importation des librairies
#============================

# Flask
from flask import Flask, render_template, request, jsonify, json

# Utilisation de la libraire random
from random import *
#Flask
app = Flask(__name__)

# le fichier taquin.py contient :
# - la classe Taquin définie pour le jeu
# - les fonctions bfs (parcours en largeur), dls (parcours en profondeur avec limite), ids (parcours en profondeur itérée) et ida* (ids avec heuristique)
# - les fonctions de création de succession d'action pour animer le chemin vers la solution
from taquin import *

    
#==============
# Phase de jeu
#==============

# Initialisation du taquin
taquindejeu = Taquin("012345678")

#=========================
# Création de la page web
#=========================

@app.route("/")
def MayTheForceBeWithYou():

    return render_template('index.html')    

#======================
# Conversation avec JS
#======================

@app.route('/next')
def ANewHope():    
    #mélange du taquin
    taquindejeu.melanger(95)
    print("Le taquin au départ", taquindejeu.etat) #contient par exemple "312645780"
    #chaîne à envoyer pour transmettre l'état 
    machaine = taquindejeu.etat
    
    # Pour faire planter : '172356840'
    # En 15 coups : '301756482'
    return render_template('play.html', depart=machaine) 
    
@app.route('/action')
def ReturnOfTheJedi():
    
    # Récupération de l'action demandée par JS (ici une chaine de caractères)
    actionaskedbyJS = request.args.get("action", type = str)
    argument2fromJS = request.args.get("argument2", type = str) #argument2fromJS contient l'état (chaîne) du taquin avant le click
    print("\nCe que j'ai reçu de JS début", actionaskedbyJS, argument2fromJS)
              
    # Préparation de la réponse à envoyer à JS    
    if (actionaskedbyJS != "None"):
        
        # Si on a clické sur une tuile dans la page web
        if (actionaskedbyJS == "mymove"):
            if argument2fromJS == 'H': 
                taquindejeu.haut()
            elif argument2fromJS == 'B':
                taquindejeu.bas()
            elif argument2fromJS == 'D':
                taquindejeu.droite()
            elif argument2fromJS == 'G':
                taquindejeu.gauche()
            
            print("état du jeu après click", taquindejeu.etat)
            argument2_tosend = "done"
        
        # On lance DLS 
        elif (actionaskedbyJS == "giveup1"):
            #On lance DLS
            if taquindejeu.estGagnant() == False:
                
                # calcul la profondeur minimum de la solution via BFS
                #print("début BFS")
                profsol = bfs(taquindejeu.etat)
                print("solution à la profondeur", profsol)
                
                #print("début DLS")
                chemin = []
                dls(profsol, taquindejeu.etat, 0, chemin)
                
                # création des déplacements à faire pour atteindre l'état solution
                arg2retour = pathfinder(taquindejeu, chemin) 
            #la variable renvoyée à JS doit être un string, tuple, response instance ou WSGI callable
            argument2_tosend = arg2retour
        
        elif (actionaskedbyJS == "giveup2"):
            # On lance IDS
            if taquindejeu.estGagnant() == False:
                #print("Début IDS")
                chemin = []
                ids(taquindejeu.etat, chemin)
                
                # création des déplacements à faire pour atteindre l'état solution
                arg2retour = pathfinder(taquindejeu, chemin)             
            #la variable renvoyée à JS doit être un string, tuple, response instance ou WSGI callable
            argument2_tosend = arg2retour
        
        elif (actionaskedbyJS == "giveup3"):
            # On lance IDA*
            if taquindejeu.estGagnant() == False:
                #print("Début IDA*")
                chemin = []
                ida(taquindejeu, chemin)
                
                # création des déplacements à faire pour atteindre l'état solution
                arg2retour = pathfinder(taquindejeu, chemin) 
            #la variable renvoyée à JS doit être un string, tuple, response instance ou WSGI callable
            argument2_tosend = arg2retour
        
        elif (actionaskedbyJS == "help me Obi-wan Kenobi, you're my only hope"):
            # On lance IDA*
            if taquindejeu.estGagnant() == False:
                #print("Début IDA*")
                chemin = []
                ida(taquindejeu, chemin)
                
                # création des déplacements à faire pour atteindre l'état solution
                arg2retour = chemin.pop()
            #la variable renvoyée à JS doit être un string, tuple, response instance ou WSGI callable
            argument2_tosend = arg2retour
        
        else:
            argument2_tosend="NULL"
    else:
        argument2_tosend = "None bizarre"
    
    answerdict = {"action": actionaskedbyJS, "argument2": argument2_tosend}
    #print("Je vais renvoyer à JS en JSON ", jsonify(answerdict)) <= renvoie un dictionnaire avec les keys entourées de simple quote
    #print("Je vais renvoyer à JS en JSON ", json.dumps(answerdict))
    # envoi le dictionnaire en JSON à JS
    return(json.dumps(answerdict))

if __name__ == "__main__":
    # Précédemment debug = False. 
    # Mettre debug=True permet au serveur de relancer ce fichier après modification directement (sans avoir à redémarrer le serveur)
    app.run(host= '0.0.0.0',port=5000,debug=True)
