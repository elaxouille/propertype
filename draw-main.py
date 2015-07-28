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
header += '<svg transform="scale(0.5,0.5)" style="margin:'+str(margin)+'px;" version="1.1" xmlns="http://www.w3.org/2000/svg">'

def pathn(a,posx):
	"""
	Dessine un N minuscule en SVG
	"""

	liste=[]
	if (isinstance(a,list)) and (len(a)>=4):
		liste = a
	o = a[0] # 0
	b = a[1] # 100
	d = a[2] # 2
	h = a[3] # 50
	c = a[4] # 25
	 # O - B - D - H - C
	 # 0 -100- 2 - 50- 25
	ch = '<path fill="black" transform="translate('+str(posx)+',0)" stroke="none" d="' # Pour les dessins avec un creux, rajouter 'fill-rule="evenodd"'
	ch += move(0,0)+lr(b,0.5)+cNE(o,h,c)+cWN(o,h,c)+lr(b,2)+cNE(o,h,c)+ld(b,4.5)+ll(b,1.5)+cSE(o,h,c)+lu(b,3)+cEN(o,h,c)+ll(b,1)+cNW(o,h,c)+ld(b,3)+cES(o,h,c)+ll(b,0.5)+lu(b,5)
	ch += closePath()
	ch += closeTag()
	print " [ n ]"
	return ch

def patho(a,posx):
	"""
	Dessine un O minuscule en SVG
	"""

	liste = []
	if (isinstance(a,list)) and (len(a)>=4):
		liste = a
	o = a[0] # 0
	b = a[1] # 100
	d = a[2] # 2
	h = a[3] # 50
	c = a[4] # 25
	 # O - B - D - H - C
	 # 0 -100- 2 - 50- 25
	ch = '<path fill="black" transform="translate('+str(posx)+',0)" fill-rule="evenodd" stroke="none" d="' # Pour les dessins avec un creux, rajouter 'fill-rule="evenodd"'
	ch += move(h,b)+lr(b,3)+cNE(o,h,c)+ld(b,3)+cES(o,h,c)+ll(b,3)+cSW(o,h,c)+lu(b,3)+cWN(o,h,c)
	ch += closePath()
	ch += move(b,b)+lr(b,1)+cNE(o,h,c)+ld(b,1)+cES(o,h,c)+ll(b,1)+cSW(o,h,c)+lu(b,1)+cWN(o,h,c)
	ch += closePath()
	ch += closeTag()
	print " [ o ]"
	return ch

def pathe(a,posx):
	"""
	Dessine un E minuscule en SVG
	"""

	liste = []
	if (isinstance(a,list)) and (len(a)>=4):
		liste = a
	o = a[0] # 0
	b = a[1] # 100
	d = a[2] # 2
	h = a[3] # 50
	c = a[4] # 25
	 # O - B - D - H - C
	 # 0 -100- 2 - 50- 25
	ch = '<path fill="black" transform="translate('+str(posx)+',0)" fill-rule="evenodd" stroke="none" d="' # Pour les dessins avec un creux, rajouter 'fill-rule="evenodd"'
	ch += move(h,0)+lr(b,3)+cNE(o,h,c)+ld(b,2)+cES(o,h,c)+ll(b,2)+cNW(o,h,c)+cWS(o,h,c)+lr(b,2)+cNE(o,h,c)+cES(o,h,c)+ll(b,3)+cSW(o,h,c)+lu(b,4)
	ch += closePath()
	ch += move(b,b)+lr(b,1)+cNE(o,h,c)+cES(o,h,c)+ll(b,1)+cSW(o,h,c)+cWN(o,h,c)
	ch += closePath()
	ch += closeTag()
	print " [ e ]"
	return ch

for i in range(60):
	st = 'svg/n-o-test-'+str(i)+'.svg'
	f = open(st, 'w')
	f.write(header)
	f.write(pathn([orig,base,div,half,i*-10],0))
	f.write(patho([orig,base,div,half,i*-10],400))
	f.write(pathe([orig,base,div,half,i*-10],800))
	f.write('\n')
	f.write('</svg>')
	f.close()