# ProjetBloc5
Jeu du Taquin 3x3

## Structure 
Le projet est constitué de 2 principaux modules relativement indépendants :
- Un module Python pour faire de la recherche de solution via un parcours en largeur dans un premier temps dans un arbre d'états. Ensuite remplacé par une fonction. Recherche de la solution par un parcours en profondeur limité par la fonction précédente.
- Un module Web (notamment JS) qui va permettre d'afficher l'état du jeu et de représenter les mouvements des tuiles

## Module Python
Le module python permetra de récupérer les données et de calculer la meilleur solution pour ensuite donner la tuile à jouer pour arriver au plus vite à la solution.

## Module Web
Le module web utilise les librairies :
- JQuery pour la partie JavaScript (écoute des clicks, validité d'un mouvement, ...)
- GSAP pour la partie d'animation des objets

## Travail Collaboratif
Travail lancé par Didier CHIU et Nicolas VAZ-PINTO, avec l'aide précieuse de David CAISSON et Teddy CHENE

## Change Log

**Bugs connus**
- Déplacement buggué si on click trop vite sur une tuile
- Recherche de la solution optimale à optimiser car trop long au dessus de 15 coups
- fonction qui calcul le nombre de coup restant erronée sur coups supérieurs à 15.

**07-04-2020** v0.4.3
- Correction de l'automate de détermination des états suivants sur toutes les versions
- Renommage des versions pour coller au document élève.
- Ajout de la fonction comparetaquin au code Taquin 3x3 BFS+DFS (qui permet de comparer 2 taquins proches pour déterminer le mouvement utile pour passer de l'un à l'autre) 

**06-04-2020** v0.4.3
- Correction de l'automate de détermination des états suivants sur IDA*
- Mise en place efficace de l'algorithme IDA* qui permet de faire une rehcerche en profondeur avec horison (sans parcourir l'arbre sur chaque branche)
- La fonction du calcul du nombre de coup est éronnée sur le profondeur supéreiur à 15, il faut la retravailler.

**05-04-2020** v0.42
- Légère amélioration de la vitesse de calcul avec l'introdution d'une fonctioon qui calcul le nombre de coup pour aller à la solution sans parcourir l'arbre en largeur.
- Amélioration de l'interface d'aide en indiquant directement le coup à jouer au lieu de la position à obtenir.

**05-04-2020** v0.41
- Connexion entre le bouton d'abandon et le module python : création de la liste des mouvements à faire pour arriver à la solution
- Cette recherche de chemin n'aboutit pas dans tous les cas : 
  - au delà d'environ une quinzaine de coups, le module python plante
  - message d'erreur : An exception has occurred, use %tb to see the full traceback. SystemExit: -9
 - Un enregistrement d'une résolution en 14 coups est disponible

**05-04-2020** v0.4
- Création d'une page play.html initialisée avec un taquin mélangé
- MAJ de la page index.html pour la présentation du projet
- MAJ de style.css pour faire joli

**04-04-2020** v0.31
- Début d'incorporation des actions du jeu en python dans link.py
- Séparation avec le fichier de Nico (tout se trouve dans taquin.py)
- Les clicks sur la page web "font jouer" le taquin dans le module python

**04-04-2020** v0.3
- Modification de la représentation de la tuile vide : identique en JS et en python (numéro 0)
- Ajout d'une variable qui représente par une chaîne de caractères l'état du taquin (JS)

**03-04-2020** v0.21
- Calcul et affichage de la solution optimale pour résoudre le taquin python
- Affichage du prochain taquin à obtenir

**03-04-2020** v0.2
- Communication avec le module python établie via la route /shuffle
- Le module python renvoie une chaîne de caractères (ex : 6B5D7H)
- La chaîne est traitée pour créer une animation des tuiles

**02-04-2020** v0.1
- dépot de la verison python du taquin 3x3 comprennant :
  - affichage du taquin 3x3
  - gestion des déplacements et de la victoire
  - gestion des états
  - calcul et affichage de la profondeur optimale pour trouver la solution
  - ajout des commentaires pour un meilleur suivi du projet

**02-04-2020** v0.1
- Création du Dépot Git et initialisation du readme.md
- Affichage de la grille 3x3
- Test si la tuile cliquée est amovible
- Déplacement d'une tuile et échange avec la tuile vide
