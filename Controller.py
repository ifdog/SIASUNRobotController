# -*- coding: gbk -*-
__author__ = 'ifdog'
"""
V1,".参数在./pos.txt"
"""
import socket, struct
aa=True
def tohex(s):
    d = []
    for i in s:
        a = hex(ord(i))
        b = a.replace("0x","")
        c = str.zfill(b, 2)
        d.append(c.upper())
    return " ".join(d)



def connect():
    socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socks.bind(('172.16.1.63', 9999))#本机ip,port
    #socks.bind(('localhost', 9999))#for test
    socks.listen(5)
    print "CON:1/2 running,waiting for client."
    connection, address = socks.accept()
    print "CON:2/2 client connected from %s" % str(address)
    return connection

def lop(server):
    global x,y,z,aa
    #n = 1
    fi=file(".\\pos.txt")
    cont=fi.readlines()
    fi.close()
    print "=============file read============="
    try:
        x,y,z,=[float(i) for i in cont[0:3]]
        print "==========parameter loaded=========="
        print "now ","x=",x,"y=",y,"z=",z
    except Exception as e:
        print e
    a = server.recv(1024)
    b = tohex(a)
    print "RECV: ", b
    if not a:
        print "Client quitted"
        aa=False
    if b == "02 21 00 00 01 01 00 00":
        print "TRIG:1/2 TRIG from robot"
        server.send("\x00\x27\x00\x00\x00\x00\x00\x01\x01")
        print "TRIG:2/2 send back"
    elif b == "02 22 00 00 01 01 00 00":
        print "GET:1/2 request from robot"
        st = "\x00\x26\x10\x00\x01\x01\x00\x00" + struct.pack("f", x) + struct.pack("f", y) + struct.pack("f",z) + "\x00\x00\x00\x00"
        server.send(st)
        print "GET:2/2 send back %s %s %s " % (x,y,z)

if __name__ =="__main__":
    print "==========script started=========="
    s = connect()
    while aa:
        lop(s)
