#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 12:37:34 2020

@author: d.chiu, n.vaz-pinto
"""

from math import *
from random import *

class Taquin():
    """
    Classe Taquin : permet de définir un objet pour le jeu du taquin
    Constructeur :
        - __init__(self, txt) : gestion de l'affichage, du déplacement et de la victoire du taquin
    Attributs :
        - contenu : liste représentant le taquin
        - etat : chaîne de caractères représentant le taquin
        - nbcol : nombre de colonnes
        - nblig : nombre de lignes
    Methodes :
        - __str__(self) : permet un affichage conventionnel en carré
        - rangezero(self) : permet de donner la position du zero, donc de la case à déplacer
        - inverser(self,rang1,rang2) : permet d´inverser la position de 2 valeurs dans la liste. Utile pour les déplacements
		- haut(self) : vérifie si le déplacement est faisable et réalise l'inversion des positions
		- bas(self) : vérifie si le déplacement est faisable et réalise l'inversion des positions
		- gauche(self) : vérifie si le déplacement est faisable et réalise l'inversion des positions
		- droite(self) : vérifie si le déplacement est faisable et réalise l'inversion des positions
		- melanger(self,profondeur) : réalise une série de mouvement aléatoire à partir d'une position initiale pour mélanger le taquin
		- gagnant(self) : vérifie si la position actuelle est la position gagnante, utilise la classe Etat
    """
    # constructeur
    def __init__(self, txt):
        # la liste qui représente la taquin en mémoire
        liste = [] 
        for i in txt:
            liste.append(i)
        self.contenu = liste 
		
        # gestion de la taille si on veut travailler sur un taquin plus grand mais toujours carré
        self.nbcol = int(sqrt(len(liste)))
        self.nblig = int(sqrt(len(liste)))
        # stocke l'état du taquin sous la forme d'une chaîne de caractères
        self.etat = txt
        
    # affichage
    def __str__(self):
        affichage = ''
        for i in range (0,self.nbcol):
            affichage = affichage + str(self.contenu[i]) + ' '
        affichage = affichage + '\n'
        for i in range (self.nbcol,self.nbcol*2):
            affichage = affichage + str(self.contenu[i]) + ' '
        affichage = affichage + '\n'
        for i in range (self.nbcol*2,self.nbcol*3):
            affichage = affichage + str(self.contenu[i]) + ' '
        affichage = affichage + '\n'
        return(affichage)        
        	
	# méthode qui permet de mettre à jour l'état du taquin à partir de son contenu (liste)
    def majetat(self):
        self.etat = ''
        for i in self.contenu:
            self.etat = self.etat + str(i)

    # méthode qui permet de connaître la position de la case vide (zéro)
    def rangzero(self):
        return(self.contenu.index('0'))
        
    # méthode qui permet d'échanger la position de deux éléments de la liste "contenu", et modifie l'attribut etat en conséquence    
    def echanger(self,rang1, rang2):
        tmp1 = self.contenu[rang1]
        tmp2 = self.contenu[rang2]
        self.contenu[rang1] = tmp2
        self.contenu[rang2] = tmp1
        self.majetat()
                
    # les quatre méthodes suivantes permettent de modifier le taquin selon le mouvement souhaité d'une case
	# les mouvements se font par rapport à la case vide : on échange la position de la case vide avec la case ciblée
    def haut(self):
        rang = self.rangzero()
        # vérifie si le déplacement est faisable avant l'échange
        if rang > 2:
            self.echanger(rang, rang-3)
    
    def bas(self):
        rang = self.rangzero()
        # vérifie si le déplacement est faisable avant l'échange
        if rang < 6:
            self.echanger(rang, rang+3)
    
    def gauche(self):
        rang = self.rangzero()
        # vérifie si le déplacement est faisable avant l'échange
        if rang != 0 and rang != 3 and rang != 6:
            self.echanger(rang, rang-1)
    
    def droite(self):
        rang = self.rangzero()
        # vérifie si le déplacement est faisable avant l'échange
        if rang != 2 and rang != 5 and rang != 8:
            self.echanger(rang, rang+1)    
        
    # méthode qui effectue une série de mouvements choisis aléatoirement afin de mélanger le taquin     
    def melanger(self, nbdefois):
        while (self.estGagnant() != False):
            for i in range (0, nbdefois):
                move = randint(1,4)
                if move == 1:
                    self.haut()
                elif move == 2:
                    self.bas()
                elif move == 3:
                    self.droite()
                elif move == 4:
                    self.gauche()
                    
    # méthode qui permet de vérifier si l'état actuel est gagnant            
    def estGagnant(self):
        averif = self.etat
        if averif == '012345678':
            return True
        else:
            return False
    
    # méthode qui renvoie la liste des états suivants du taquin par rapport à son état actuel
    def suivants(self):
		# automate qui prend un etat en entrée et renvoie une chaine avec l'ensemble de setats accessibles depuis l'etat d'entrée
        position=self.rangzero()
        eH = ''
        eB = ''
        eD = ''
        eG = ''
        rendu=[]
        
        if position == 0:
            eH = ''
            eB = self.etat[3]+self.etat[1]+self.etat[2]+self.etat[0]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
            eD = self.etat[1]+self.etat[0]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
            eG = ''
        
        if position == 1:
            eH = ''
            eB = self.etat[0]+self.etat[4]+self.etat[2]+self.etat[3]+self.etat[1]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
            eD = self.etat[0]+self.etat[2]+self.etat[1]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
            eG = self.etat[1]+self.etat[0]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
        
        if position == 2:
            eH = ''
            eB = self.etat[0]+self.etat[1]+self.etat[5]+self.etat[3]+self.etat[4]+self.etat[2]+self.etat[6]+self.etat[7]+self.etat[8]
            eD = ''
            eG = self.etat[0]+self.etat[2]+self.etat[1]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
        
        if position == 3:
            eH = self.etat[3]+self.etat[1]+self.etat[2]+self.etat[0]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
            eB = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[6]+self.etat[4]+self.etat[5]+self.etat[3]+self.etat[7]+self.etat[8]
            eD = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[4]+self.etat[3]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
            eG = ''
        
        if position == 4:
            eH = self.etat[0]+self.etat[4]+self.etat[2]+self.etat[3]+self.etat[1]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
            eB = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[7]+self.etat[5]+self.etat[6]+self.etat[4]+self.etat[8]
            eD = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[5]+self.etat[4]+self.etat[6]+self.etat[7]+self.etat[8]
            eG = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[4]+self.etat[3]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
        
        if position == 5:
            eH = self.etat[0]+self.etat[1]+self.etat[5]+self.etat[3]+self.etat[4]+self.etat[2]+self.etat[6]+self.etat[7]+self.etat[8]
            eB = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[8]+self.etat[6]+self.etat[7]+self.etat[5]
            eD = ''
            eG = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[5]+self.etat[4]+self.etat[6]+self.etat[7]+self.etat[8]
        
        if position == 6:
            eH = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[6]+self.etat[4]+self.etat[5]+self.etat[3]+self.etat[7]+self.etat[8]
            eB = ''
            eD = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[7]+self.etat[6]+self.etat[8]
            eG = ''
        
        if position == 7:
            eH = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[7]+self.etat[5]+self.etat[6]+self.etat[4]+self.etat[8]
            eB = ''
            eD = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[8]+self.etat[7]
            eG = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[7]+self.etat[6]+self.etat[8]
        
        if position == 8:
            eH = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[8]+self.etat[6]+self.etat[7]+self.etat[5]
            eB = ''
            eD = ''
            eG = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[8]+self.etat[7]
        
        if eH != '':
            rendu.append(eH)
        if eB != '':
            rendu.append(eB)
        if eG != '':
            rendu.append(eG)
        if eD != '':
            rendu.append(eD)
        return(rendu) 

# Plusieurs fonctions de recherche d'un état gagnant du taquin
# Recherche avec un parcours en largeur (BFS = Breadth First Search)
def bfs(etatdepart):
    """
    Fonction de recherche qui part d'un état initial du taquin et effectue un parcours en largeur jusqu'à ce qu'elle trouve l'état gagnant. A ce moment elle renvoie la profondeur de la solution trouvée. 
    Principe : Elle teste chaque état d'une profondeur donnée avant de passer à la profondeur suivante dans le cas où elle ne trouve pas la combinaison gagnante à cette profondeur.
    Entrée : un état du taquin
	Sortie : profondeur à laquelle la solution aura été trouvée
    """
    
    # état de départ pour lancer la recherche avec parcours en largeur
    A = [etatdepart]
    
    # profondeur de départ
    p = 0
    while A != []:
		# initialisation de la liste des états suivants
        B = []
        # boucle qui teste un par un les états de profondeur p
        for i in range(0, len(A)):
            # On vérifie si l'état est gagnant
            taquindetravail = Taquin(A[i])
            if taquindetravail.estGagnant():
                # renvoie la profondeur de la solution
                return p
                        
            # On rajoute les états suivants pour chaque élément de la file
            for i in taquindetravail.suivants():
                # ajoute chaque état suivant à la liste qui sera testée à la profondeur suivante
                B.append(i)
        A = B
        # pour passer à la profondeur suivante
        p = p + 1 

# Recherche avec un parcours en profondeur limitée (DLS = Depth-Limited Search)
def dls(profmax, etatdepart, profdepart, path):
    """
    Fonction qui teste les états suivants à partir d'un état en profondeur tout en se limitant à une profondeur max donnée
    Entrées :
        - profmax : profondeur maximale
        - etatdepart : état de départ
        - profdepart : profondeur initiale
        - path : chemin (liste des états successifs) d'accès à l'état gagnant
    Sorties : 
    """
    
    # vérification si la profondeur maximum n'est pas atteinte
    if profdepart > profmax:
        return(False)
    # vérification si l'etat testé est gagnant ou non
    taquindetravail = Taquin(etatdepart)
    if taquindetravail.estGagnant():
        return True
        
    # parcours récursif des états suivants
    # appel récursif de la fonction de test pour descendre en profondeur
    for etatsuivant in taquindetravail.suivants():
        if dls(profmax, etatsuivant, profdepart + 1, path) == True:
            #stockage du chemin d'accès en mémoire et retour
            path.append(etatsuivant)
            return True
        
    return False
	
# Recherche avec un parcours en profondeur itérée (IDS = Iterative Deepening Search)
def ids(etatdepart, path):
    profmax = 0
    profinit = 0
    while not dls(profmax, etatdepart, profinit, path):
        profmax += 1
	
# Une fonction (heuristique pour IDA*) qui calcule un minorant du nombre de coups pour atteindre l'état solution à partir d'un état donné
def nbcoup(etat):
    total = 0
    rang = -1
    coord = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    
    for i in etat:
        rang += 1
        
        if i != '0':
            val = int(i)
            # écart de la case par rapport aux lignes
            terme1 = int(val/3)
            # écart de la case par rapport aux colonnes
            terme2 = (fmod(val,3))
            
            part1 = fabs(coord[rang][0] - terme1)
            part2 = fabs(coord[rang][1] - terme2)
            total += part1 + part2
    
    return(total)

# Adaptation de DLS pour tenir compte de l'heuristique	
def dlsplus(profmax, etatdepart, profdepart, path):
	#fonction qui test les suivants d'un etat en profondeur tout en se limitant a une profondeur donnée
    global min
    taquindetravail = Taquin(etatdepart)
    
    #évalue le nombre de coup minimum pour atteindre la solution en ajoutant le minorant du nombre de coups à la profondeur actuellement testée
    evalcoup = profdepart + nbcoup(etatdepart)
    #print('nb coup a la solution (evalcoup)=',evalcoup)
        
    # vérification si la profondeur maximum n'est pas atteinte en tenant compte de la minoration du nombre de coup
    if evalcoup > profmax:
        #print('nb profmax depassé')
        #print('min=',min,' evalcoup=',evalcoup)
        if evalcoup < min:
            min = evalcoup
        return False
    
    # verification si l'etat testé est gagnant ou non
    if taquindetravail.estGagnant():
        return True
    
    # Appel récursif de la fonction pour descendre en profondeur
    for etatsuivant in taquindetravail.suivants():
        if dlsplus(profmax, etatsuivant, profdepart + 1, path) == True:
            #stockage du chemin d'accès en mémoire et retour
            path.append(etatsuivant)
            return True
    
    return(False)
    
        
# Recherche avec IDA * détermine les profondeur minimum des solutions accessibles en réduisant au maximum les plages de recherche
def ida(etatdepart, path):
    global min
    
    m = nbcoup(etatdepart)
    #print('The Force is this strong with this one', m)
    while m != 1000:
        min = 1000
        if dlsplus(m, etatdepart, 0, path):
            #print('m=',m,' min=',min)
            return(True)
        #print('maj de m')
        m = min
    
    return False

# Les fonctions suivantes permettent de créer la succession de mouvements afin d'animer le chemin vers l'état solution
# Fonction qui permet de déterminer l'action à entreprendre pour passer du premier au second état
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

# Fonction qui prend la liste des états successifs pour atteindre l'état solution (produite par l'un des algorithmes de recherche) et qui renvoie la liste des mouvements à effectuer
def pathfinder(taquindetravail, road):
    etat1 = taquindetravail.etat
    toVictory = ''
    print("chemin", road)
    
    while(road != []):
        etat2 = road.pop()
        #print("who really needs to move", whereTo(etat1, etat2))
        toVictory += whereTo(etat1, etat2)
        etat1 = etat2
        #print("road to victory", toVictory)
                
    # Cette partie mets à jour le taquin lorsqu'on emprunte le chemin vers la victoire !
    for i in toVictory:
        if i == 'B':
            taquindetravail.haut()
        elif i == 'H':
            taquindetravail.bas()
        elif i == 'G':
            taquindetravail.droite()
        elif i == 'D':
            taquindetravail.gauche()
    
    return toVictory
