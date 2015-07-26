#!/usr/bin/python

print "[ OK ] Initialisations des courbes"

def move(x,y) :
	return 'm'+str(x)+','+str(y)

def lr(b,x): # x = coefficient
	return 'l'+str(b*x)+',0'
def ld(b,x):
	return 'l0,'+str(b*x)
def ll(b,x):
	return 'l'+str(-(b*x))+',0'
def lu(b,x):
	return 'l0,'+str(-(b*x))

def cNE(o,b,d,h,c):
	return 'c'+str(c)+','+str(o)+' '+str(h)+','+str(c)+' '+str(h)+','+str(h)
def cES(o,b,d,h,c):
	return 'c'+str(o)+','+str(c)+' '+str(-c)+','+str(h)+' '+str(-h)+','+str(h)
def cSW(o,b,d,h,c):
	return 'c'+str(-c)+','+str(o)+' '+str(-h)+','+str(o)+' '+str(-h)+','+str(-h)
def cWN(o,b,d,h,c):
	return 'c'+str(o)+','+str(-c)+' '+str(c)+','+str(-h)+' '+str(h)+','+str(-h)

def cNW(o,b,d,h,c):
	return 'c'+str(-c)+','+str(o)+' '+str(-h)+','+str(c)+' '+str(-h)+','+str(h)
def cWS(o,b,d,h,c): #################################
	return 'c'+str(o)+','+str(-c)+' '+str(h)+','+str(-c)+' '+str(h)+','+str(-c)
def cSE(o,b,d,h,c):
	return 'c'+str(c)+','+str(o)+' '+str(h)+','+str(-c)+' '+str(h)+','+str(-h)
def cEN(o,b,d,h,c):
	return 'c'+str(o)+','+str(-c)+' '+str(-c)+','+str(-h)+' '+str(-h)+','+str(-h)

def closePath():
	return 'z"/>'

