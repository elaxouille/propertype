#!/usr/bin/python

def move(x,y) :
	return 'm'+str(x)+','+str(y)

def lineRight(b,x): # x = coefficient
	return 'l'+str(b*x)+',0'
def lineDown(b,x):
	return 'l0,'+str(b*x)
def lineLeft(b,x):
	return 'l'+str(-(b*x))+',0'
def lineUp(b,x):
	return 'l0,'+str(-(b*x))

def curveNE(o,b,d,h,c):
	return 'c'+str(c)+','+str(o)+' '+str(h)+','+str(c)+' '+str(h)+','+str(h)
def curveES(o,b,d,h,c):
	return 'c'+str(o)+','+str(c)+' '+str(-c)+','+str(h)+' '+str(-h)+','+str(h)
def curveSW(o,b,d,h,c):
	return 'c'+str(-c)+','+str(o)+' '+str(-h)+','+str(o)+' '+str(-h)+','+str(-h)
def curveWN(o,b,d,h,c):
	return 'c'+str(o)+','+str(-c)+' '+str(c)+','+str(-h)+' '+str(h)+','+str(-h)

def curveNW(o,b,d,h,c):
	return 'c'+str(-c)+','+str(o)+' '+str(-h)+','+str(c)+' '+str(-h)+','+str(h)
def curveWS(o,b,d,h,c): #################################
	return 'c'+str(o)+','+str(-c)+' '+str(h)+','+str(-c)+' '+str(h)+','+str(-c)
def curveSE(o,b,d,h,c):
	return 'c'+str(c)+','+str(o)+' '+str(h)+','+str(-c)+' '+str(h)+','+str(-h)
def curveEN(o,b,d,h,c):
	return 'c'+str(o)+','+str(-c)+' '+str(-c)+','+str(-h)+' '+str(-h)+','+str(-h)

def closePath():
	return 'z"/>'