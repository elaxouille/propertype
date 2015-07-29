#!/usr/bin/python

import collections, sys, time, colorama
from colorama import Fore, Back, Style

fichiermou = 'txt/entree.txt'
fichierdur = 'txt/monthy-python-meaning-life.txt'
fichier_hyper_dur = 'txt/huge-lorem.txt'
total = 0
compte = 0

user_0 = raw_input('Fichier dur ou fichier mou ? : ')
if (user_0 == 'dur'):
	fichier = fichierdur
elif (user_0 == 'DURDURDUR'):
	fichier = fichier_hyper_dur
else:
	fichier = fichiermou
affiche_liste = False
user_1 = raw_input('Afficher la liste des lettres ? : ')
if (user_1 == 'oui'):
	affiche_liste = True
	print "\r"

colorama.init()

### http://rosettacode.org/wiki/Letter_frequency#Using_collections.Counter
def letterfrequency(openfile):
	return sorted(collections.Counter(c for l in openfile for c in l).items())

def letterfrequency_non_sensible(openfile):
	return sorted(collections.Counter(c.upper() for l in openfile for c in l).items())

print "[ OK ] Initialisation des modules"

print "[ OK ] Fichier choisi : "+Fore.GREEN+fichier+Style.RESET_ALL


liste_sensible = letterfrequency(open(fichier))
liste_non_sensible = letterfrequency_non_sensible(open(fichier))
print "[ OK ] Initialisation de la variable"

if (affiche_liste):
	for i in range(6):
		print str(i+1)+ " . . "
		time.sleep(1)
	for item in liste_sensible:
		total += item[1]
		if (compte <= 1) :
			pass
		elif (compte % 2 == 0) :
			print "       "+Fore.WHITE+Back.MAGENTA+"-  [ "+item[0]+" ]\tRep : "+str(item[1])+"   \tTotal : "+Fore.YELLOW+str(total)+Style.RESET_ALL
		else :
			print "       "+Fore.WHITE+Back.BLACK+"-  [ "+item[0]+" ]\tRep : "+str(item[1])+"   \tTotal : "+Fore.GREEN+str(total)+Style.RESET_ALL
		time.sleep(.2)
		compte += 1

print "[ OK ] La liste est terminee"
print "\r"
nombre_de_n = 0


