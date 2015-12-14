# Propertype

Machine a ecrire, de la typographie generative.


Fichier | Dependances | Description
--------|-------------|------------
read.py| collections, sys, time | lit l'input.txt et deduit des variables et constantes
curves.py|aucune| liste des fonctions qui dessinent les courbes de bezier en svg
draw-main.py| read, curves | rassemble les variables de read et les fonctions de curves

a faire :
- toutes les lettres
- algorithme qui redistribue intelligemment les variables
- reappropriation des variables par les fonctions

problemes a resoudre :
- ~~sortie de la liste lue~~
- reparation de la courbe ouest-sud
- debug et catching exceptions
- gestion MEP et PDF
- gestion interface


rajout du dossier typo strokefont