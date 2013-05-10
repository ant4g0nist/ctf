#!/usr/bin/env python
import os,sys,commands
from socket import *
ip="194.106.195.60"
port=9502
s=socket(AF_INET,SOCK_STREAM)
s.connect((ip,port))
cmd="nc {0} {1} -w 2".format(ip,port)
for i in range(2):
	a=s.recv(1024)
b=""

c=[]
a=a.split("\n")
#print a
#sys.exit()
for i in a:

	for j in i:
		if j=="+":
			b=b+"-"
		if j=="-":
			b=b+"+"
		if len(b)==10:
			print i,b
			c.append(b)	
			b=""

c="\n".join(c)
#print c
#print "---------"
#print a
#sys.exit()
s.send(c)
print s.recv(1024)
#	sys.exit()
