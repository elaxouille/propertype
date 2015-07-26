#!/usr/bin/python

import collections, sys, time

fichiermou = 'txt/entree.txt'
fichierdur = 'txt/amusements-in-mathematics.txt'

### http://rosettacode.org/wiki/Letter_frequency#Using_collections.Counter
def letterfrequency(openfile):
	return sorted(collections.Counter(c for l in openfile for c in l).items())

print "[ OK ] Initialisation des modules"

retour = letterfrequency(open(fichiermou))

print "[ OK ] Initialisation de la variable"

# for item in retour:
# 	print " \t... character : "+item[0]+" ::: repetitions : "+str(item[1])
# 	time.sleep(.6)

print "[ OK ] La liste est terminee"
