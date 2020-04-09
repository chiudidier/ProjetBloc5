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
# - les classes définies pour le jeu : Taquin et Etat
# - les fonctions bfs (parcours en largeur) et dls (parcours en profondeur)
# - une fonctions pratique txt2list 
from taquin import *
import time
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

def whereTo(etat1, etat2):
    pos_zero_etat1 = etat1.index('0')
    pos_zero_etat2 = etat2.index('0')
    who = etat2[pos_zero_etat1]
    
    if (pos_zero_etat1 % 3 == pos_zero_etat2 % 3) and (pos_zero_etat1 < pos_zero_etat2):
        where = "H"
    if (pos_zero_etat1 % 3 == pos_zero_etat2 % 3) and (pos_zero_etat1 > pos_zero_etat2):
        where = "B"
    if (pos_zero_etat1 % 3 - pos_zero_etat2 % 3 == 1):
        where = "D"
    if (pos_zero_etat1 % 3 - pos_zero_etat2 % 3 == -1):
        where = "G"
    
    return(who+where)
    
#==============
# Phase de jeu
#==============

# Initialisation du taquin (position gagnante)
taquindejeu = initializetaquin("012345678")


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
    #taquindejeu est initialisé au début à "012345678" par la fonction initializetaquin (voir plus haut)
    #mélange du taquin
    taquindejeu.melanger(35)
    print("Le taquin au départ", Etat(taquindejeu).val) #contient par exemple "312645780"
    #chaîne à envoyer pour transmettre l'état 
    machaine = Etat(taquindejeu).val
    
    # Pour faire planter : '172356840'
    # En 15 coups : '301756482'
    return render_template('play.html', depart=machaine) 
    
@app.route('/action')
def ReturnOfTheJedi():
    
    # Récupération de l'action demandée par JS (ici une chaine de caractères)
    actionaskedbyJS = request.args.get("action", type = str)
    argument2fromJS = request.args.get("argument2", type = str) #argument2fromJS contient l'état (chaîne) du taquin avant le click
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
        
        # On lance DLS 
        elif (actionaskedbyJS == "giveup1"):
            #print("état du jeu à l'abandon", argument2fromJS)
            #taquindejeu = initializetaquin(argument2fromJS)
            # Pour tester avec une chaîne prédéfinie
            
            if taquindejeu.gagnant() == False:
                
                # calcul la profondeur minimum de la solution via BFS
                print("début BFS")
                debut=time.time()
                reste = bfs(taquindejeu)
                fin=time.time() - debut
                print("fin BFS", fin)
                
                # préparation pour DLS
                chemin = []
                etatzero = Etat(taquindejeu)
                print("VAR etatzero", etatzero, "reste", reste, "chemin", chemin)
                # recherche du chemin vers la solution via DLS
                print("début DLS")
                debut=time.time()
                dls(reste, etatzero, 0, chemin)
                fin=time.time() - debut
                print("fin DLS", fin)
                
                # affiche l'aide
                print(reste, 'mouvements au moins pour terminer. \nSolution =', chemin)
                
                # retire de la liste des états suivants le premier pour affichage
                etat1 = etatzero.val
                toVictory = ''
                
                while(chemin != []):
                    nextmove = chemin.pop()
                    nexttaquin = Taquin(nextmove)
                    #print('meilleur coup suivant :')
                    #print(nexttaquin)     
                    #print("step zero", etatzero)
                    
                    etat2 = nextmove
                    #print("who really needs to move", whereTo(etat1, etat2))
                    toVictory += whereTo(etat1, etat2)
                    etat1 = nextmove
                print("road to victory", toVictory)
        
            #la variable renvoyée à JS doit être un string, tuple, response instance ou WSGI callable
            argument2_tosend = toVictory #1G4H3D6H7G8G5B2B
        
        elif (actionaskedbyJS == "giveup2"):
            # On lance IDA*
            
            if taquindejeu.gagnant() == False:
                print("Début IDA*")
                chemin = []
                debut=time.time()
                ida(taquindejeu, chemin)
                fin=time.time() - debut
                print("Fin IDA*", fin)
                
                etatzero = Etat(taquindejeu)
                etat1 = etatzero.val
                toVictory = ''
                    
                while(chemin != []):
                    nextmove = chemin.pop()
                    nexttaquin = Taquin(nextmove)
                    #print('meilleur coup suivant :')
                    #print(nexttaquin)     
                    #print("step zero", etatzero)
                    
                    etat2 = nextmove
                    #print("who really needs to move", whereTo(etat1, etat2))
                    toVictory += whereTo(etat1, etat2)
                    etat1 = nextmove
                print("This is the way", toVictory)
        
            #la variable renvoyée à JS doit être un string, tuple, response instance ou WSGI callable
            argument2_tosend = toVictory #1G4H3D6H7G8G5B2B
        
        
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
