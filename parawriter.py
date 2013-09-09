# -*- coding: gbk -*-
__author__ = 'ifdog'
"""
V2,"参数在./pos.txt"
"""
def getpos():
    a=open("./pos.txt")
    b=a.readlines()
    i,j,k=b[0:3]
    return float(i),float(j),float(k)

def writepos(aa,bb,cc):
    a=open("./pos.txt","w")
    a.write(str(aa))
    a.write('\n')
    a.write(str(bb))
    a.write('\n')
    a.write(str(cc))
    a.write('\n') 
    a.close()
    
while True:
    print "="*20
    a1=getpos()
    pos=[0,0,0]
    i=str(raw_input("input the pos\n"))
    if i==" ":
        print "set to 0"
        writepos(0.0,0.0,0.0)
    else:
        j=i.split(',')
        if len(j)==1:
            for i in range(3-len(j)):
                j.append(0.0)
        j1= j[0:3]
        print "INPUT:",
        for x in j1:
            print x,
        print
        for k in range(3):
            try:
                pos[k]=a1[k]+float(j1[k])
                if pos[k]>499 or pos[k]<-499:
                    print "pos",pos[k],"out of range"
                    pos[k]=pos[k]-float(j1[k])
            except Exception as e:
                print e,"set to 0"
                pos[k]=a1[k]
        print "OUTPUT:",
        for y in pos:
            print y,
        print
        aa,bb,cc=pos
        writepos(aa,bb,cc)
