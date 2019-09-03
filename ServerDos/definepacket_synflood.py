#!/usr/bin/env python

def setpacketinfoip(Ip_range,destination):
    from scapy.all import IP
    if type(Ip_range) != list:
       sourceip = Ip_range
       targetip = destination
       Ip_packet = IP()
       Ip_packet.src = str(sourceip)
       Ip_packet.dst = str(targetip)
       Ip_packet.proto = 6
       return Ip_packet
       
    
    else:
       versionip = '4'
       targetip = destination
       Ip_packet = IP()
       Ip_packet.version = versionip
       Ip_packet.dst = targetip
       Ip_packet.proto = 6
       return Ip_packet
      

       
def setpacketinfotcp(targetport):
    from scapy.all import TCP
    import random
    Tcp_packet = TCP()
    Tcp_packet.dport = int(targetport)
    Tcp_packet.sport = int(random.randint(1, 65535))
    Tcp_packet.seq = int(random.randint(1,65535))
    Tcp_packet.window = int(random.randint(1, 65535))
    Tcp_packet.flags = "S"
    return Tcp_packet
    	
