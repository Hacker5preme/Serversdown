#!/usr/bin/env python

import os
print 'Serversdown'
print ''
filepath = 'Versionnotes.txt'
a = open(filepath, 'r')
for line in a.readlines():
    print line
       


print ''
print ''
print 'Supported attacks till now: Syn Flood'
print('')
print 'For Syn Flood attack press:  1'
choice = int(raw_input(''))
if choice == 1:
   os.system('clear')
   execfile('synflood.py')
 









































































































