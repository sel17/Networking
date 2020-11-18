#!/bin/python3

import sys
import socket
from datetime import datetime

#Define target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to IP address
else:
	print("invalid amount of arguments")
	print("Syntax: python3 scanner.py <IP>")
	
#ADD A PRETTY BANNER
print("-" * 50)
print("Scanning target " + target)
print("Time started " + str(datetime.now()))
print("-" * 50)

try:
	for port in range(52,82):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator
		#print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
	
except KeyboardInterrupt:
	print("\nExiting Program.")
	sys.exit()
	
except socket.gaierror:
	print("HOstname could not be resolved")
	sys.exit()
	
except socket.error:
	print("could not connect to the server")
	sys.exit()
