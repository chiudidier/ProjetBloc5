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

def nbcoup(etat):
	# fonction qui calcul un minorant du nombre de coup pour solutionner un etat en se basant sur l'écart de chaque tuile à sa position initiale.
	total=0
	rang=-1
	coord=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
	for i in etat:
		rang=rang+1
		if i!='0':
			val=int(i)
			term1=int(val/3)
			term2=fmod(val,3)
			part1=fabs(coord[rang][0]-term1)#ecart de la tuile par rapport aux lignes
			part2=fabs(coord[rang][1]-term2)#ecart de la tuile par rapport aux colonnes
			soustotal=part1+part2
			total=total+soustotal
	return(total)

def comparetaquins(taquin1,taquin2):
	# fonction qui donne le mouvement necessaire pour passer d'un taquin à l'autre
	origine=taquin1.rangzero()
	finale=taquin2.rangzero()
	move=origine-finale
	if move==-3:
		deplacement='b'
	elif move==3:
		deplacement='h'
	elif move==1:
		deplacement='g'
	elif move==-1:
		deplacement='d'
	return(deplacement)
 
def ida():# determine la profondeur minimum des solutions accessibles en resuisant au maximum les plages de recherche.
	global min
	etat0=montaquin.etat
	m=nbcoup(etat0)# calcul un minorant du nombre de coup vers la solution
	while m!=1000:
		min=1000
		if dfs(m,etat0,0):
			return(True)
		m=min
	return(False)

def dfs(profmax,etattest,proftest):
	#fonction qui test les suivants d'un etat en profondeur tout en se limitant a une profondeur donnée
	global min	
	gagnant='012345678'
	evalcoup=proftest+nbcoup(etattest)#estimation du nombre de coups vers la solution
	if evalcoup>profmax:# verification si la profondeur maximum n'est pas atteinte
		if evalcoup<min:
			min=evalcoup
		return(False)
	if etattest==gagnant:# verification si l'etat testé est gagnant ou non
		return(True)
	# calcul des suivants de l'etat testé
	Ttmp=Taquin(etattest)
	suivantslist=Ttmp.suivants()
	
	for i in suivantslist: # appel recursif de la fonction de test pour descendre en profondeur
		if dfs(profmax,i,proftest+1)==True:
			chemin.append(i)#stockage du chemin d'acces pour memoire et retour
			return(True)
	return(False)


def shufflelist(s):
    # Le module random dispose d'une fonction shuffle qui mélange les éléments d'une liste
    # Il suffit de créer une chaîne à partir des éléments de la liste mélangée
    L = list(s)
    shuffle(L)
    result = ''.join(L)
    return result

def levelofchaos(etat):
    # Mesure le dérangement d'un état du taquin
    # Un état est représenté par une chaîne de caractères
    level = 0
    for i in range(len(etat)):
        for j in range(i+1, len(etat)):
            #print("couple", etat[i], etat[j])
            if etat[i] > etat[j]:
                #print("elements mal rangés")
                level += 1
    return level

def melanger(statetaquin):
    # Mélange aléatoirement un taquin
    # statetaquin est une chaîne représentant l'état du taquin
    # on crée la liste correspondante
    L = []
    for i in range(0, len(statetaquin)):
        L.append(statetaquin[i])
    randstate = shufflelist(L)
    
    nbpass = 0
    # on mélange la chaîne ainsi produite tant que la mesure du dérangement n'est pas paire    
    while (levelofchaos(randstate) % 2 != 0):
        nbpass += 1
        randstate = shufflelist(L)
    print("Nb de mélanges aléatoires effectués", nbpass)
    # on renvoie la chaîne mélangée pour une configuration acceptable
    # on pourrait aussi renvoyer une liste contenant les éléments de la chaîne
    return randstate


#main
'''
old
montxt='012345678'# position initiale = solution
montaquin=Taquin(montxt)# création du taquin

# mélange en realisant 15 coups aléatoires à partir de la position initiale pour garantir que la position obtenu soit bien solutionnable.
while montaquin.gagnant():
	montaquin.melanger(15)
'''
continuer=True

while continuer:
    montxt=melanger('012345678')# position initiale créé à partir d'une position aléatoire mais dont la solvabilité est vérifiable
    montaquin=Taquin(montxt)# création du taquin

    print(montaquin)
    if nbcoup(montxt) > 12 :
        print('dsl nous ne pouvont pas résoudre se taquin en un temps raisonable')
    else:
        while montaquin.gagnant()==False:# boucle principale du jeu. Sort qaund le taquin est solutionnéc
            chemin=[]
            ida()# calcul la profondeur minimum de la solution
            print('solution = ', chemin)#affichage des differents etats de la solution
            nextmove=chemin.pop()
            nexttaquin=Taquin(nextmove)
            print('meilleur coup suivant :')
            print(comparetaquins(montaquin,nexttaquin))#affichage du prochain coup
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
    reponse=input('Voulez vous recommencer ? o/n : ')
    if reponse == 'n':
        continuer=False   
print('Au revoir')
