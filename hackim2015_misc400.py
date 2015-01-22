from __future__ import with_statement
import sys
from contextlib import nested
import socket
import sys
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('54.165.191.231', 2910))
dp={'7e4041326446ac6beeaa886a236c4cd0':'follatore','6f9304f41a89770fa6b7682e8729f7df':'f47h3125hip'}
while True:
	# try:
 
		buffer=clientsocket.recv(1024)
		d=buffer.decode('cp500').encode('latin1')
		if not "Finally you deserve this gift" in d:
			print d
			if 'Decode this' in d:
				# print d.split
				clientsocket.send(dp[d.split('this  ')[1].split(' ')[0]].decode('latin1').encode('cp500'))
				buffer=clientsocket.recv(1024)
				print buffer.decode('cp500').encode('latin1')
		else:
			print d
			sys.exit()
		# except:
		# 	pass
