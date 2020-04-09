#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 12:37:34 2020

@author: n.vaz-pinto
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
    
    def __init__(self, txt):
        # la liste qui représente la taquin en mémoire
        liste = [] 
        for i in txt:
            liste.append(i)
        self.contenu = liste 
		
        #gestion de la taille si on veut travailler sur un taquin plus grand mais toujours carré
        self.nbcol=int(sqrt(len(liste)))
        self.nblig=int(sqrt(len(liste)))	
	
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
        
    def rangzero(self):
        return(self.contenu.index('0'))
        
    def inverser(self,rang1,rang2):
        tmp1 = self.contenu[rang1]
        tmp2 = self.contenu[rang2]
        self.contenu[rang1] = tmp2
        self.contenu[rang2] = tmp1
        
    def haut(self):
        rang = self.rangzero()
        if rang > 2:
            self.inverser(rang,rang-3)
            
    def bas(self):
        rang = self.rangzero()
        if rang < 6:
            self.inverser(rang,rang+3)
            
    def gauche(self):
        rang = self.rangzero()
        if (rang != 0 and rang != 3 and rang != 6):
            self.inverser(rang,rang-1)
            
    def droite(self):
        rang = self.rangzero()
        if (rang != 2 and rang != 5 and rang != 8):
            self.inverser(rang,rang+1)
            
    def melanger(self,profondeur):
        for i in range (0,profondeur):
            move = randint(1,4)
            if move == 1:
                self.haut()
            elif move == 2:
                self.bas()
            elif move == 3:
                self.droite()
            elif move == 4:
                self.gauche()
                
    def gagnant(self):
        averif = Etat(self)
        if averif.val == '012345678':
            return(True)
        else:
            return(False)
            
class Etat():
    """
    Classe Etat : permet de retenir un état du taquin pour calculer les suivants.
    Constructeur :
        - __init__(self, taquin) : crée une chaîne de caractères représentant le taquin à partir de la liste des valeurs contenues dans un objet de classe Taquin
    Attributs :
        - val : chaîne représentant le taquin
        - longueur (de la chaîne)
    Methodes :
        - __str__(self) : affiche la chaîne représentant l'état du taquin
        - etatzero(self) : renvoie la position du zéro pour calculer les suivants
        - suivants(self) : automate qui prend un état en entrée et renvoie une chaine avec l'ensemble des états accessibles depuis l'état d'entrée
		- gagnant(self) : permet de verifier si un état est gagnant
    """
    
    def __init__(self,taquin):
        etat = ''
        longueur = 0
        for i in taquin.contenu:
            etat = etat + str(i)
            longueur = longueur+1
        self.val = etat
        self.len = longueur
        
    def __str__(self):
        rendu=''
        for i in range (0,self.len):
            rendu = rendu + str(self.val[i])
        return(rendu)
        
    def etatzero(self):
        for i in range(0,self.len):
            if self.val[i] == '0':
                return(i)
                
    def suivants(self):
        position = self.etatzero()
        eH=''
        eB=''
        eD=''
        eG=''
        if position == 0:
            eH=''
            eB=self.val[3]+self.val[1]+self.val[2]+self.val[0]+self.val[4]+self.val[5]+self.val[6]+self.val[7]+self.val[8]+','
            eD=self.val[1]+self.val[0]+self.val[2]+self.val[3]+self.val[4]+self.val[5]+self.val[6]+self.val[7]+self.val[8]+','
            eG=''
        if position == 1:
            eH=''
            eB=self.val[0]+self.val[4]+self.val[2]+self.val[3]+self.val[1]+self.val[5]+self.val[6]+self.val[7]+self.val[8]+','
            eD=self.val[0]+self.val[2]+self.val[1]+self.val[3]+self.val[4]+self.val[5]+self.val[6]+self.val[7]+self.val[8]+','
            eG=self.val[1]+self.val[0]+self.val[2]+self.val[3]+self.val[4]+self.val[5]+self.val[6]+self.val[7]+self.val[8]+','
        if position == 2:
            eH=''
            eB=self.val[0]+self.val[1]+self.val[5]+self.val[3]+self.val[4]+self.val[2]+self.val[6]+self.val[7]+self.val[8]+','
            eD=''
            eG=self.val[0]+self.val[2]+self.val[1]+self.val[3]+self.val[4]+self.val[5]+self.val[6]+self.val[7]+self.val[8]+','
        if position == 3:
            eH=self.val[3]+self.val[1]+self.val[2]+self.val[0]+self.val[4]+self.val[5]+self.val[6]+self.val[7]+self.val[8]+','
            eB=self.val[0]+self.val[1]+self.val[2]+self.val[6]+self.val[4]+self.val[5]+self.val[3]+self.val[7]+self.val[8]+','
            eD=self.val[0]+self.val[1]+self.val[2]+self.val[4]+self.val[3]+self.val[5]+self.val[6]+self.val[7]+self.val[8]+','
            eG=''
        if position == 4:
            eH=self.val[0]+self.val[4]+self.val[2]+self.val[3]+self.val[1]+self.val[5]+self.val[6]+self.val[7]+self.val[8]+','
            eB=self.val[0]+self.val[1]+self.val[2]+self.val[3]+self.val[7]+self.val[5]+self.val[6]+self.val[4]+self.val[8]+','
            eD=self.val[0]+self.val[1]+self.val[2]+self.val[3]+self.val[5]+self.val[4]+self.val[6]+self.val[7]+self.val[8]+','
            eG=self.val[0]+self.val[1]+self.val[2]+self.val[4]+self.val[3]+self.val[5]+self.val[6]+self.val[7]+self.val[8]+','
        if position == 5:
            eH=self.val[0]+self.val[1]+self.val[5]+self.val[3]+self.val[4]+self.val[2]+self.val[6]+self.val[7]+self.val[8]+','
            eB=self.val[0]+self.val[1]+self.val[2]+self.val[3]+self.val[4]+self.val[8]+self.val[6]+self.val[7]+self.val[5]+','
            eD=''
            eG=self.val[0]+self.val[1]+self.val[2]+self.val[3]+self.val[5]+self.val[4]+self.val[6]+self.val[7]+self.val[8]+','
        if position == 6:
            eH=self.val[0]+self.val[1]+self.val[2]+self.val[6]+self.val[4]+self.val[5]+self.val[3]+self.val[7]+self.val[8]+','
            eB=''
            eD=self.val[0]+self.val[1]+self.val[2]+self.val[3]+self.val[4]+self.val[5]+self.val[7]+self.val[6]+self.val[8]+','
            eG=''
        if position == 7:
            eH=self.val[0]+self.val[1]+self.val[2]+self.val[3]+self.val[7]+self.val[5]+self.val[6]+self.val[4]+self.val[8]+','
            eB=''
            eD=self.val[0]+self.val[1]+self.val[2]+self.val[3]+self.val[4]+self.val[5]+self.val[6]+self.val[8]+self.val[7]+','
            eG=self.val[0]+self.val[1]+self.val[2]+self.val[3]+self.val[4]+self.val[5]+self.val[7]+self.val[6]+self.val[8]+','
        if position == 8:
            eH=self.val[0]+self.val[1]+self.val[2]+self.val[3]+self.val[4]+self.val[8]+self.val[6]+self.val[7]+self.val[5]+','
            eB=''
            eD=''
            eG=self.val[0]+self.val[1]+self.val[2]+self.val[3]+self.val[4]+self.val[5]+self.val[6]+self.val[8]+self.val[7]+','
        rendu = eH + eB + eD + eG
        return(rendu)
        
    def gagnant(self):
        if self.val == '012345678':
            return(True)
        else:
            return(False)
			
def txt2list(txt):
	"""
    Fonction permettant de convertir une chaine de caractères en liste pour passer d'un (objet de classe) Etat à un Taquin
    Entrée : une chaîne de caractères
    Sortie : une liste contenant ces caractères
    """
	elmnt = ''
	rendu = []
	for i in txt:
		if i != ',':
			elmnt = elmnt + i
		else:
			rendu.append(elmnt)
			elmnt = ''
	return(rendu)	
    
#def list2txt(liste):
#    """
#    Fonction permettant de convertir liste en une chaine de caractères pour passer d'un (objet de classe) Taquin à un Etat
#    Entrée : une liste contenant ces caractères
#    Sortie : une chaîne de caractères
#    """
#    rendu = ""
#    rendu = rendu.join([str(elem) for elem in liste])  
#    return(rendu)

def bfs(taquinzero):
    """
    Fonction qui part d'une position initiale du taquin et effectue un parcour en largeur jusqu'à ce qu'elle trouve l'éat gagnant. A ce moment elle renvoie la profondeur de la solution trouvée. 
    Principe : Elle teste chaque état d'une profondeur donnée avant de passer à la profondeur suivante dans le cas où elle ne trouve pas la combinaison gagnante à cette profondeur.
    Entrée : un taquin (que le fonction convertira en Etat)
	Sortie : profondeur à laquelle la solution aura été trouvée
    """
    
    # état gagnant
    gagnant = '012345678'
    
    e0 = Etat(taquinzero)
    # position initiale
    A = [e0.val]
    # profondeur de départ
    p = 0
    while A != []:
		# initialisation de la liste des résultats
        B = []
        # boucle qui teste un par un les états de profondeur p
        for i in range(0, len(A)):
            # On vérifie si l'etat est gagnant
            if A[i] == gagnant:
                # renvoie la profondeur de la solution
                return(p)
            # convertit le texte testé en (objet de classe) Taquin
            Ttmp=Taquin(A[i])
            # convertit le taquin en (objet de classe) Etat
            Etmp=Etat(Ttmp)
            # calcule tous les états suivants dà partir de l'état testé
            Ltmp=txt2list(Etmp.suivants())
            for i in Ltmp:
                # ajoute chaque état suivant à la liste qui sera testée à la profondeur suivante
                B.append(i)
        A = B
        # pour passer à la profondeur suivante
        p = p + 1 


def dfs(profmax,etattest,proftest,chemin):
    """
    Fonction qui teste les états suivants à partir d'un état en profondeur tout en se limitant à une profondeur max donnée
    Entrées :
        - profmax : profondeur maximale
        - etattest : état de départ
        - profest : profondeur initiale
        - chemin : chemin (liste des états successifs) d'accès à la configuration gagnante
    Sorties : 
    """
    
    gagnant='012345678'
    # vérification si la profondeur maximum n'est pas atteinte
    if proftest > profmax:
        return(False)
    # vérification si l'etat testé est gagnant ou non
    if etattest.val == gagnant:
        return(True)
	# calcul des états suivants
    suivantstxt = etattest.suivants()
    suivantslist = txt2list(suivantstxt)
    suivantsetats = []
	
    # mise en liste des états suivants pour traitement
    for i in suivantslist:
        taquintmp=Taquin(i)
        tmp=Etat(taquintmp)
        suivantsetats.append(tmp)
	
    # appel récursif de la fonction de test pour descendre en profondeur	
    for i in suivantsetats:
        if dfs(profmax, i, proftest + 1, chemin) == True:
			#stockage du chemin d'accès en mémoire et retour
            chemin.append(i.val)
            return(True)
    return(False)

# fonction qui calcule (sans la chercher dans l'arbre) un minorant du nombre de coup pour atteindre la solution
def nbcoup(table):
	# fonction qui calcule (sans la chercher dans l'arbre) un minorant du nombre de coup pour atteindre la solution
	total=0
	coord=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
	for i in range (0,len(table)):
#		print(table[i])
		if int(table[i])!='0':
#			print('coordonnee: ',coord[i][0],' ',coord[i][1])
#			print('val=',table[i])
#			print('ent/3=',table[i]%3,' modulo/3=',fmod(table[i],3))
			total=total+(fabs(coord[i][0]-int(int(table[i])/3))+fabs(coord[i][1]-fmod(int(table[i]),3)))
#			print(total)
	return(total)

		
def dfsnew(profmax,etattest,proftest,chemin):
	#fonction qui test les suivants d'un etat en profondeur tout en se limitant a une profondeur donnée
	global min
	gagnant='012345678'
	taquintest=Taquin(etattest.val)
#	print('etat testé:',etattest,' min=',min)
#	print(etattest.val)
#	tabetatest=txt2list(str(etattest.val))
#	print(tabetatest)
#	print('nb coup de etat testé=',nbcoup(tabetatest))
	evalcoup=proftest+nbcoup(taquintest.contenu) #évalue le nombre de coup minimum pour atteindre la solution en ajoutant le minorant du niombre de coup à la profondeur actuellement testé
	
#	print('nb coup a la solution (evalcoup)=',evalcoup)
#	print('nb coup evalluer',evalcoup)
	if evalcoup>profmax:# verification si la profondeur maximum n'est pas atteinte en tenant compte de la minoration du nombre de coup
#		print('nb profmax depassé')
#		print('min=',min,' evalcoup=',evalcoup)
		if evalcoup<min:
			min=evalcoup
		return(False)
	if etattest.val==gagnant:# verification si l'etat testé est gagnant ou non
		return(True)
	# calcul des suivants de l'etat testé
	suivantstxt=etattest.suivants()
	suivantslist=txt2list(suivantstxt)
	suivantsetats=[]

	
	for i in suivantslist:# mise en liste des suivants pour traitement
		taquintmp=Taquin(i)
		tmp=Etat(taquintmp)
		suivantsetats.append(tmp)
	

	for i in suivantsetats:# appel recursif de la fonction de test pour descendre en profondeur
#		print('suivants : pour (p=',proftest,' etat' ,i.val)
		if dfsnew(profmax,i,proftest+1,chemin)==True:
			chemin.append(i.val)#stockage du chemin d'acces pour memoire et retour
			return(True)
#	print('branche fausse')
	return(False)


# determine les profondeur minimum des solutions accessibles en réduisant au maximum les plages de recherche
def ida(taquin0, chemin):
	global min
#	print('je passe par ida')
	etat0=Etat(taquin0)
	m=nbcoup(taquin0.contenu)
	print('The Force is this strong with this one', m)
	while m!=1000:
		min=1000
		if dfsnew(m,etat0,0,chemin):
#			print('m=',m,' min=',min)
			return(True)
#		print('maj de m')
		m=min
	return(False)
