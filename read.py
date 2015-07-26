#!/usr/bin/python

import collections, sys, time, colorama
from colorama import Fore, Back, Style

fichiermou = 'txt/entree.txt'
fichierdur = 'txt/monthy-python-meaning-life.txt'
fichier = fichiermou
total = 0
compte = 0

colorama.init()

### http://rosettacode.org/wiki/Letter_frequency#Using_collections.Counter
def letterfrequency(openfile):
	return sorted(collections.Counter(c for l in openfile for c in l).items())

def letterfrequency_non_sensible(openfile):
	return sorted(collections.Counter(c.upper() for l in openfile for c in l).items())

print "[ OK ] Initialisation des modules"

print "[ OK ] Fichier choisi : "+fichier
time.sleep(6)


retour = letterfrequency(open(fichier))
retour_non_sensible = letterfrequency_non_sensible(open(fichier))
print "[ OK ] Initialisation de la variable"

for item in retour:
	if (compte <= 1) :
		pass
	elif (compte % 2 == 0) :
		print "       "+Fore.WHITE+Back.MAGENTA+"-  [ "+item[0]+" ]\tRep : "+str(item[1])+"   \tTotal : "+Fore.YELLOW+str(total)+Style.RESET_ALL
	else :
		print "       "+Fore.BLACK+Back.WHITE+"-  [ "+item[0]+" ]\tRep : "+str(item[1])+"   \tTotal : "+Fore.GREEN+str(total)+Style.RESET_ALL
	total += item[1]
	time.sleep(.6)
	compte += 1

print "[ OK ] La liste est terminee"
