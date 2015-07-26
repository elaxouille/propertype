#!/usr/bin/python

from letterfrequency import letterfrequency
import time

fichiermou = 'entree.txt'
fichierdur = 'amusements-in-mathematics.txt'

print "[ OK ] Initialisation des modules"

retour = letterfrequency(open(fichiermou))

print "[ OK ] Initialisation de la variable"

# for item in retour:
# 	print " \t... character : "+item[0]+" ::: repetitions : "+str(item[1])
# 	time.sleep(.6)

print "[ OK ] La liste est terminee"
