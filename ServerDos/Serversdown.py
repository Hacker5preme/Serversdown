#!/usr/bin/env python

import os
print 'SERVERDOS'
filepath = 'Versionnotes.txt'
with open(filepath) as fp:
   line = fp.readline()
   while line:
       print line
       line = fp.readline()
       


print ''
print ''
print 'Supported attacks till now: Syn Flood'
print 'For Syn Flood attack press 1'
choice = int(raw_input(''))
if choice == 1:
   os.system('clear')
   execfile('synflood.py')
 









































































































