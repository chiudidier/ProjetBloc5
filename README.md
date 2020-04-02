# ProjetBloc5
Jeu du Taquin 3x3

## Structure 
Le projet est constitué de 2 principaux modules relativement indépendants :
- Un module Python pour faire de la recherche de solution via un parcours en largeur dans un arbre d'états,
- Un module Web (notamment JS) qui va permettre d'afficher l'état du jeu et de représenter les mouvements des tuiles

## Module Python
Le module python permetra de récupérer les données et de calculer la meilleur solution pour ensuite donner la tuile à jouer pour arriver au plus vite à la solution.

## Module Web
Le module web utilise les librairies :
-JQuery pour la partie JavaScript (écoute des clicks, validité d'un mouvement, ...)
-GSAP pour la partie d'animation des objets

## Travail Collaboratif
Travail lancé par Didier CHIU et Nicolas VAZ-PINTO, avec l'aide précieuse de David CAISSON et Teddy CHENE

## Change Log

**Bugs connus**
- Déplacement buggué si on click trop vite sur une tuile

**02-04-2020** v0.1
- Création du Dépot Git et initialisation du readme.md
- Affichage de la grille 3x3
- Test si la tuile cliquée est amovible
- Déplacement d'une tuile et échange avec la tuile vide

**02-04-2020** v0.1
- dépot de la verison python du taquin 3x3 comprennant :
  - affichage du taquin 3x3
  - gestion des déplacements et de la victoire
  - gestion des états
  - calcul et affichage de la profondeur optimale pour trouver la solution
