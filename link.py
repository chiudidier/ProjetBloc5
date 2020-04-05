#!/usr/bin/python
# -*- coding: utf-8 -*-

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
# - les classes définies pour le jeu : Taquin et Etat
# - les fonctions bfs (parcours en largeur) et dfs (parcours en profondeur)
# - une fonctions pratique txt2list 
from taquin import *

#=========================================================================
# Partie de code tirée du fichier de Nicolas pour utiliser ses fonctions
#=========================================================================

def initializetaquin(machaine):
    # old by Nico
    # position initiale = solution
    # montxt='012345678'
    # création du taquin
    montaquin=Taquin(machaine)
    return montaquin

def playtaquin():    
    montaquin = initializetaquin("012345678")
    # mélange en réalisant 15 coups aléatoires à partir de la position initiale pour garantir que la position obtenue soit bien solutionnable.
    while montaquin.gagnant():
    	montaquin.melanger(15)
    print('taquin a résoudre:')
    print(montaquin)
    
    # boucle principale du jeu. Sort quand le taquin est solutionné
    while montaquin.gagnant() == False:
    	# calcul la profondeur minimum de la solution
        reste = bfs(montaquin)
        chemin = []
        etatzero = Etat(montaquin)
        dfs(reste,etatzero,0,chemin)
        # affiche l'aide
        print(reste, 'mouvements au moins pour terminer. \nSolution =', chemin)
        
        # retire de la liste des états suivants le premier pour affichage
        nextmove = chemin.pop()
        nexttaquin = Taquin(nextmove)
        print('meilleur coup suivant :')
        print(nexttaquin)
        
        # demande le coup à jouer et applique le mouvement
        move = input('Que voulez vous jouer (h,b,d,g): ')
        if move == 'h':
            montaquin.haut()
        elif move == 'b':
            montaquin.bas()
        elif move == 'd':
            montaquin.droite()
        elif move == 'g':
            montaquin.gauche()
        print(montaquin)
    
    print('Bravo vous avez gagné !')


#==============
# Phase de jeu
#==============

# Initialisation du taquin (position gagnante)
taquindejeu = initializetaquin("012345678")


#=========================
# Création de la page web
#=========================

@app.route("/")
def Morpheus():

    return render_template('index.html')    


#======================
# Conversation avec JS
#======================

@app.route("/Red_pill")
def Chase_the_white_rabbit():
    #le shuffle est géré par la route /shuffle
    
    #A modifier plus tard
    
    #shufflelist=['1','2','4','3','9','7','6','8','5']
    
    # On passe la liste de question et la liste des types en paramètres à questionnaire.html
    #return render_template('taquin.html', depart=shufflelist) #même nom de var dans jinja html
    return "Warning, cette route n'est pas encore configurée"

@app.route('/action')
def retourJS():
    
    # Récupération de l'action demandée par JS (ici une chaine de caractères)
    actionaskedbyJS = request.args.get("action", type = str)
    argument2fromJS = request.args.get("argument2", type = str)
    print("\nCe que j'ai reçu de JS", actionaskedbyJS, argument2fromJS)
              
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
            
            print("état du jeu après click", Etat(taquindejeu))
            argument2_tosend = "done"
        
        # Si on a clické sur le boutton dans la page web
        elif (actionaskedbyJS == "shuffle"):
            #la variable renvoyée à JS doit être un string, tuple, response instance ou WSGI callable
            argument2_tosend = "1G4H3D6H7G8G5B2B"
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
