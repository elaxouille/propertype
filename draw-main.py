#!/usr/bin/python

from curves import * 	# module contenant les fonctions qui dessinent
from read import *		# module contenant la fonction qui compte les lettres

orig = 0				# origine
base = 100				# un carre
div = 2					# division de base pour arrondi
half = base/div
courbe = base / (2*div)	# poignee bezier : largeur carre sur moitie de div
argu = [orig,base,div,half,courbe]

margin = 60		# marge

header = '<?xml version="1.0" standalone="no"?>'
header += '\n'
header += '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">'
header += '\n'
header += '<svg style="margin:'+str(margin)+'px;" version="1.1" xmlns="http://www.w3.org/2000/svg">'

def pathn(a):
	"""
	Dessine un N minuscule en SVG
	"""

	liste=[]
	if (isinstance(a,list)) and (len(a)>=4):
		liste = a
	print "[ OK ] - Invocation reussie"
	o = a[0] # 0
	b = a[1] # 100
	d = a[2] # 2
	h = a[3] # 50
	c = a[4] # 25
	 # O - B - D - H - C
	 # 0 -100- 2 - 50- 25
	print "[ OK ] - Definition des fonctions"
	print "[ OK ] - Initialisation du 'n'"
	ch = '<path fill="black" stroke="none" d="'
	ch += move(0,0)+lr(b,0.5)+cNE(o,b,d,h,c)+cWN(o,b,d,h,c)+lr(b,2)+cNE(o,b,d,h,c)+ld(b,4.5)+ll(b,1.5)+cSE(o,b,d,h,c)+lu(b,3)+cEN(o,b,d,h,c)+ll(b,1)+cNW(o,b,d,h,c)+ld(b,3)+cES(o,b,d,h,c)+ll(b,0.5)+lu(b,5)
	ch += closePath()
	print "[ OK ] - Dessin du 'n' termine"
	return ch

for i in range(6):
	st = 'n-test-'+str(i)+'.svg'
	f = open(st, 'w')
	f.write(header)
	f.write(pathn([i,base,div,half,courbe]))
	f.write('\n')
	f.write('</svg>')
	f.close()