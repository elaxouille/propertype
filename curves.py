#!/usr/bin/python

print "\r"
print "\t###### Bienvenue ! ######"


print "\r"
print "[ OK ] Invocation de la grille"
print "\r"


move = lambda x,y : 'm'+str(x)+','+str(y)

lr = lambda b,x : 'l'+str(b*x)+',0'
ld = lambda b,x : 'l0,'+str(b*x)
ll = lambda b,x : 'l'+str(-(b*x))+',0'
lu = lambda b,x : 'l0,'+str(-(b*x))

cNE = lambda o,h,c : 'c'+str(c)+','+str(o)+' '+str(h)+','+str(c)+' '+str(h)+','+str(h)
cES = lambda o,h,c : 'c'+str(o)+','+str(c)+' '+str(-c)+','+str(h)+' '+str(-h)+','+str(h)
cSW = lambda o,h,c : 'c'+str(-c)+','+str(o)+' '+str(-h)+','+str(o)+' '+str(-h)+','+str(-h)
cWN = lambda o,h,c : 'c'+str(o)+','+str(-c)+' '+str(c)+','+str(-h)+' '+str(h)+','+str(-h)

cNW = lambda o,h,c : 'c'+str(-c)+','+str(o)+' '+str(-h)+','+str(c)+' '+str(-h)+','+str(h)
###
cWS = lambda o,h,c : 'c'+str(o)+','+str(-c)+' '+str(h)+','+str(-c)+' '+str(h)+','+str(-c)
###
cSE = lambda o,h,c : 'c'+str(c)+','+str(o)+' '+str(h)+','+str(-c)+' '+str(h)+','+str(-h)
cEN = lambda o,h,c : 'c'+str(o)+','+str(-c)+' '+str(-c)+','+str(-h)+' '+str(-h)+','+str(-h)

closePath = lambda : 'z'
closeTag = lambda : '"/>'

print "[ OK ] Grille initialisee"
print "\r"


def lower_n(o,b,d,h,c):
	return move(0,0)+lr(b,0.5)+cNE(o,h,c)+cWN(o,h,c)+lr(b,2)+cNE(o,h,c)+ld(b,4.5)+ll(b,1.5)+cSE(o,h,c)+lu(b,3)+cEN(o,h,c)+ll(b,1)+cNW(o,h,c)+ld(b,3)+cES(o,h,c)+ll(b,0.5)+lu(b,5)

def lower_o(o,b,d,h,c):
	return move(h,b)+lr(b,3)+cNE(o,h,c)+ld(b,3)+cES(o,h,c)+ll(b,3)+cSW(o,h,c)+lu(b,3)+cWN(o,h,c)+closePath()+move(b,b)+lr(b,1)+cNE(o,h,c)+ld(b,1)+cES(o,h,c)+ll(b,1)+cSW(o,h,c)+lu(b,1)+cWN(o,h,c)

def lower_e(o,b,d,h,c):
	return move(h,0)+lr(b,3)+cNE(o,h,c)+ld(b,2)+cES(o,h,c)+ll(b,2)+cNW(o,h,c)+cWS(o,h,c)+lr(b,2)+cNE(o,h,c)+cES(o,h,c)+ll(b,3)+cSW(o,h,c)+lu(b,4)+closePath()+move(b,b)+lr(b,1)+cNE(o,h,c)+cES(o,h,c)+ll(b,1)+cSW(o,h,c)+cWN(o,h,c)