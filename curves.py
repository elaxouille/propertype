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
