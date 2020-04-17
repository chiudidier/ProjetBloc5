from taquin import *
from random import *
from math import *


#main
'''
old : ancienne façon de mélanger qui correspond à une manipulation du taquin. Plus à coder pour les élèves et pour faire des essais de profondeur
montxt='012345678'# position initiale = solution
montaquin=Taquin(montxt)# création du taquin

# mélange en realisant 15 coups aléatoires à partir de la position initiale pour garantir que la position obtenu soit bien solutionnable.
while montaquin.gagnant():
	montaquin.melanger(15)
'''
continuer=True

while continuer:
    
    '''
    #old : ancienne façon de mélanger qui correspond à une manipulation du taquin. Plus à coder pour les élèves et pour faire des essais de profondeur
    montxt='012345678'# position initiale = solution
    montaquin=Taquin(montxt)# création du taquin

    # mélange en realisant 15 coups aléatoires à partir de la position initiale pour garantir que la position obtenu soit bien solutionnable.
    while montaquin.estGagnant():
        montaquin.melanger(15)
    '''
    # création aléatoire du taquin initiale, n'utiliser qu'avec IDA
    montxt=random_init('012345678')# position initiale créé à partir d'une position aléatoire mais dont la solvabilité est vérifiable
    montaquin=Taquin(montxt)# création du taquin
    
    print(montaquin)
    if nbcoup(montxt) > 12 :
        print('dsl nous ne pouvont pas résoudre se taquin en un temps raisonable')
    else:
        while not montaquin.estGagnant():# boucle principale du jeu. Sort qaund le taquin est solutionné
            chemin=[]
            '''
            #version BFS
            # attention ne pas utuiliser cette version avec la génération de taquin aléatoire mais utiliser le mélange à base de coup aléatoire depuis la solution.
            reste=bfs(montaquin.etat)# calcul la profondeur minimum de la solution
            print(reste,' mouvements au moins pour terminer.')# affiche l'aide
            #fin version BFS
            '''
            '''
            #version DLS=BFS+DFS
            # attention ne pas utuiliser cette version avec la génération de taquin aléatoire mais utiliser le mélange à base de coup aléatoire depuis la solution.
            reste=bfs(montaquin.etat)# calcul la profondeur minimum de la solution
            dls(reste,montaquin.etat,0,chemin) #version DLS = DFS + BFS # attention ne pas utuiliser cette version avec la génération de taquin aléatoire mais utiliser le mélange à base de coup aléatoire depuis la solution.
            #fin version DLS
            '''
            
            #ids(montaquin.etat,chemin) #version IDS = itération d'IDS # attention ne pas utiliser cette version avec la génération de taquin aléatoire mais utiliser le mélange à base de coup aléatoire depuis la solution.
            
            ida(montaquin.etat,chemin) #version IDA  calcul la profondeur minimum de la solution, les parametre ne sont pas indispensable mais améliore la lisibilité du code
                                
            # cette partie est utilisable pour les version IDS, DFS et IDA
            print('solution = ', chemin)#affichage des differents etats de la solution
            print('nb coup à la solution',len(chemin))
            nextmove=chemin.pop()
            nexttaquin=Taquin(nextmove)
            print('meilleur coup suivant :')
            print(comparetaquins(montaquin,nexttaquin))#affichage du prochain coup
            #fin de la partie solution
            
            # enregistrement du coup du joueur
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
            # fin du coup du joueur
            
        print('Bravo vous avez gagné !')
    reponse=input('Voulez vous recommencer ? o/n : ')
    if reponse == 'n':
        continuer=False   
print('Au revoir')


