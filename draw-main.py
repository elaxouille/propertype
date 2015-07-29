#!/usr/bin/python

from curves import * 	# module contenant les fonctions qui dessinent
from read import *		# module contenant la fonction qui compte les lettres

orig = 0				# origine
base = 100				# un carre
div = 2					# division de base pour arrondi
half = base/div
courbe = base / (2*div)	# poignee bezier : largeur carre sur moitie de div
argu = [orig,base,div,half,courbe]

margin = 200		# marge

header = '<?xml version="1.0" standalone="no"?>'
header += '\n'
header += '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">'
header += '\n'
header += '<svg transform="scale(0.5,0.5)" style="margin:'+str(margin)+'px;" version="1.1" xmlns="http://www.w3.org/2000/svg">'

def patha(a,posx):
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
	ch = '<path fill="black" transform="translate('+str(posx)+',0)" fill-rule="evenodd" stroke="none" d="' # Pour les dessins avec un creux, rajouter 'fill-rule="evenodd"'
	ch += lower_a(o,b,d,h,c)
	ch += closePath()
	ch += closeTag()
	# print " [ n ]"
	return ch

def pathb(a,posx):
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
	ch = '<path fill="black" transform="translate('+str(posx)+',0)" fill-rule="evenodd" stroke="none" d="' # Pour les dessins avec un creux, rajouter 'fill-rule="evenodd"'
	ch += lower_b(o,b,d,h,c)
	ch += closePath()
	ch += closeTag()
	# print " [ n ]"
	return ch

def pathc(a,posx):
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
	ch += lower_c(o,b,d,h,c)
	ch += closePath()
	ch += closeTag()
	# print " [ n ]"
	return ch

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
	ch += lower_n(o,b,d,h,c)
	ch += closePath()
	ch += closeTag()
	# print " [ n ]"
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
	ch += lower_o(o,b,d,h,c)
	ch += closePath()
	ch += closeTag()
	# print " [ o ]"
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
	ch += lower_e(o,b,d,h,c)
	ch += closeTag()
	# print " [ e ]"
	return ch

for i in range(6):
	st = 'svg/n-o-e-test-'+str(i)+'.svg'
	f = open(st, 'w')
	f.write(header)
	# f.write(patha([orig,base,div,half,courbe*i*10],0))
	f.write(pathb([orig,base,div,half,courbe*i*10],400))
	f.write(pathc([orig,base,div,half,courbe*i*10],800))
	# f.write(pathn([orig,base,div,half,courbe*i*10],1200))
	f.write(patho([orig,base,div,half,courbe*i*10],1600))
	f.write(pathe([orig,base,div,half,courbe*i*10],2000))
	print '\r'
	# f.write(pathn([orig,75,8,100,3],0))
	# f.write(patho([orig,60,2,50,25],400))
	# f.write(pathe([orig,100,5,28,8],800))
	f.write('\n')
	f.write('</svg>')
	f.close()