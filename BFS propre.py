from math import *
from random import *

class Taquin():
#gestion de l'affichage, du deplacement et de la victoire du taquin
	def __init__(self,txt):
		liste=[]
		for i in txt:
			liste.append(i)
		self.contenu=liste # la liste qui représente la taquin en memoire
		 #gestion de la taille si on veut travailler sur un taquin plus grand mais toujours carré
		self.nbcol=int(sqrt(len(liste)))
		self.nblig=int(sqrt(len(liste)))	
		self.etat=txt # garde l'etat du taquin
		
	def __str__(self):#permet un affichage conventionnel en carré
		affichage=''
		for i in range (0,self.nbcol):
			affichage=affichage+str(self.contenu[i])+' '
		affichage=affichage+'\n'
		for i in range (self.nbcol,self.nbcol*2):
			affichage=affichage+str(self.contenu[i])+' '
		affichage=affichage+'\n'
		for i in range (self.nbcol*2,self.nbcol*3):
			affichage=affichage+str(self.contenu[i])+' '
		affichage=affichage+'\n'
		return(affichage)
	
	def majetat(self):# permet de mettre a jour l'etat du taquin
		self.etat=''
		for i in self.contenu:
			self.etat=self.etat+str(i)
	
	
	def rangzero(self):#permet de donner la position du zero, donc de la case à déplacer
		return(self.contenu.index('0'))
	
	def inverser(self,rang1,rang2):
		# permet d´inverser la position de 2 valeurs dans la liste. Utile pour les déplacements
		tmp1=self.contenu[rang1]
		tmp2=self.contenu[rang2]
		self.contenu[rang1]=tmp2
		self.contenu[rang2]=tmp1
		self.majetat()
	
	def haut(self):# vérifie si le déplacement est faisable et réalise l'inversion des positions
		rang=self.rangzero()
		if rang>2:
			self.inverser(rang,rang-3)
	
	def bas(self):# vérifie si le déplacement est faisable et réalise l'inversion des positions
		rang=self.rangzero()
		if rang<6:
			self.inverser(rang,rang+3)
	
	def gauche(self):# vérifie si le déplacement est faisable et réalise l'inversion des positions
		rang=self.rangzero()
		if rang!=0 and rang!=3 and rang!=6:
			self.inverser(rang,rang-1)

	def droite(self):# vérifie si le déplacement est faisable et réalise l'inversion des positions
		rang=self.rangzero()
		if rang!=2 and rang!=5 and rang!=8:
			self.inverser(rang,rang+1)
	
	def melanger(self,profondeur):
		# réalise une série de mouvement aléatoire à partir d'une position initiale pour mélanger le taquin
		for i in range (0,profondeur):
			move=randint(1,4)
			if move==1:
				self.haut()
			elif move==2:
				self.bas()
			elif move==3:
				self.droite()
			elif move==4:
				self.gauche()
		
	def gagnant(self):# vérifie si la position actuelle est la position gagnante 
		averif=self.etat
		if averif=='012345678':
			return(True)
		else:
			return(False)
		
	def suivants(self):
		# automate qui prend un etat en entrée et renvoie une chaine avec l'ensemble de setats accessibles depuis l'etat d'entrée
		position=self.rangzero()
		eH=''
		eB=''
		eD=''
		eG=''
		rendu=[]
		
		if position==0:
			eH=''
			eB=self.etat[3]+self.etat[1]+self.etat[2]+self.etat[0]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
			eD=self.etat[1]+self.etat[0]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
			eG=''
			
		if position==1:
			eH=''
			eB=self.etat[0]+self.etat[4]+self.etat[2]+self.etat[3]+self.etat[1]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
			eD=self.etat[0]+self.etat[2]+self.etat[1]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
			eG=self.etat[1]+self.etat[0]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
			
		if position==2:
			eH=''
			eB=self.etat[0]+self.etat[1]+self.etat[5]+self.etat[3]+self.etat[4]+self.etat[2]+self.etat[6]+self.etat[7]+self.etat[8]
			eD=''
			eG=self.etat[0]+self.etat[2]+self.etat[1]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
			
		if position==3:
			eH=self.etat[3]+self.etat[1]+self.etat[2]+self.etat[0]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
			eB=self.etat[0]+self.etat[1]+self.etat[2]+self.etat[6]+self.etat[4]+self.etat[5]+self.etat[3]+self.etat[7]+self.etat[8]
			eD=self.etat[0]+self.etat[1]+self.etat[2]+self.etat[4]+self.etat[3]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
			eG=''
			
		if position==4:
			eH=self.etat[0]+self.etat[4]+self.etat[2]+self.etat[3]+self.etat[1]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
			eB=self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[7]+self.etat[5]+self.etat[6]+self.etat[4]+self.etat[8]
			eD=self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[5]+self.etat[4]+self.etat[6]+self.etat[7]+self.etat[8]
			eG=self.etat[0]+self.etat[1]+self.etat[2]+self.etat[4]+self.etat[3]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
			
		if position==5:
			eH=self.etat[0]+self.etat[1]+self.etat[5]+self.etat[3]+self.etat[4]+self.etat[2]+self.etat[6]+self.etat[7]+self.etat[8]
			eB=self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[8]+self.etat[6]+self.etat[7]+self.etat[5]
			eD=''
			eG=self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[5]+self.etat[4]+self.etat[6]+self.etat[7]+self.etat[8]
			
		if position==6:
			eH=self.etat[0]+self.etat[1]+self.etat[2]+self.etat[6]+self.etat[4]+self.etat[5]+self.etat[3]+self.etat[7]+self.etat[8]
			eB=''
			eD=self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[7]+self.etat[6]+self.etat[8]
			eG=''
			
		if position==7:
			eH=self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[7]+self.etat[5]+self.etat[6]+self.etat[4]+self.etat[8]
			eB=''
			eD=self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[8]+self.etat[7]
			eG=self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[7]+self.etat[6]+self.etat[8]
			
		if position==8:
			eH=self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[8]+self.etat[6]+self.etat[7]+self.etat[5]
			eB=''
			eD=''
			eG=self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[8]+self.etat[7]
		
		if eH!='':
			rendu.append(eH)
		if eB!='':
			rendu.append(eB)
		if eG!='':
			rendu.append(eG)
		if eD!='':
			rendu.append(eD)
		return(rendu) 

def bfs():
	# fonction qui part d'une position initiale du taquin et effectue un parcour en largeur  jusqu'a ce qu'elle trouve la solution gagnant. A ce moment elle renvoie la profondeur de la solution trouvée. En pratique elle test chaque état d'une profondeur donnée un par un. Si elle ne trouve pas la combinaison gagnante elle passe à la profondeur suivante.
	gagnant='012345678'# etat gagnant
	e0=montaquin.etat
	A=[e0]#position initiale
	p=0	# profondeur de départ
	while A!=[]:
		B=[]# initialisation de la liste des resultats
		for i in range(0,len(A)):# boucle qui test un par un les etats de profondeur p
			if A[i]==gagnant:# verifi si l'etat est gagnant
				return(p)# renvoie la profondeur de la solution
			Ttmp=Taquin(A[i])# convertie le texte testé en taquin
			Ltmp=Ttmp.suivants()# calculs tous les etats suivants de l'etat testé'
			for i in Ltmp:
				B.append(i)# ajoute chaque suivant à la liste qui sera testé à la profondeur suivante
		A=B
		p=p+1# augmente la profondeur de 1


#main

montxt='012345678'# position initiale = solution
montaquin=Taquin(montxt)# création du taquin

# mélange en realisant 15 coups aléatoires à partir de la position initiale pour garantir que la position obtenu soit bien solutionnable.
while montaquin.gagnant():
	montaquin.melanger(15)

print(montaquin)

while montaquin.gagnant()==False:# boucle principale du jeu. Sort qaund le taquin est solutionné
	reste=bfs()# calcul la profondeur minimum de la solution
	print(reste,' mouvements au moins pour terminer.')# affiche l'aide
	move=input('\n que voulez vous jouer (h,b,d,g): ')# demande le coup à jouer et applique le mouvement
	if move=='h':
		montaquin.haut()
	elif move=='b':
		montaquin.bas()
	elif move=='d':
		montaquin.droite()
	elif move=='g':
		montaquin.gauche()
	print(montaquin)

print('Bravo vous avez gagné !')


