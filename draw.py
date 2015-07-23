#!/usr/bin/python

from curves import *

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
	print "[OK] - Invocation reussie"
	o = a[0] # 0
	b = a[1] # 100
	d = a[2] # 2
	h = a[3] # 50
	c = a[4] # 25
	 # O - B - D - H - C
	 # 0 -100- 2 - 50- 25
	print "[OK] - Definition des fonctions"
	print "[OK] - Initialisation du 'n'"
	ch = '<path fill="black" stroke="none" d="'
	ch += move(0,0) 
	ch += lineRight(b,0.5)
	ch += curveNE(o,b,d,h,c)
	ch += curveWN(o,b,d,h,c)
	ch += lineRight(b,2)
	ch += curveNE(o,b,d,h,c)
	ch += lineDown(b,4.5)
	ch += lineLeft(b,1.5)
	ch += curveSE(o,b,d,h,c)
	ch += lineUp(b,3)
	ch += curveEN(o,b,d,h,c)
	ch += lineLeft(b,1)
	ch += curveNW(o,b,d,h,c)
	ch += lineDown(b,3)
	ch += curveES(o,b,d,h,c)
	ch += lineLeft(b,0.5)
	ch += lineUp(b,5)
	ch += 'z"/>'
	print "[OK] - Dessin du 'n' termine"
	return ch

for i in range(120):
	st = 'n-test-'+str(i)+'.svg'
	f = open(st, 'w')
	f.write(header)
	f.write(pathn([i,base,div,half,courbe]))
	f.write('\n')
	f.write('</svg>')
	f.close()