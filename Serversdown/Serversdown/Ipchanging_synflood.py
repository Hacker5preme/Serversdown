#!/usr/bin/env python

def chooseiprange(awnser_anonymizing, supcountries):
  if type(awnser_anonymizing) == str:
     if awnser_anonymizing in supcountries:
        selectland = awnser_anonymizing
        selectland = selectland.replace(' ','')
        countryfile = selectland + '.txt'
        useriprange = []   
        with open(countryfile) as fp:
            for number,line in enumerate(fp):
                line = line.replace('\n', '')
                useriprange.append(line)
        if '' in useriprange:
          useriprange.remove('')   
        return useriprange
     if awnser_anonymizing == 'all':
        filename = 'allipranges.txt'
        useriprange = []   
        with open(filename) as fp:
            for number,line in enumerate(fp):
                line = line.replace('\n', '')
                if line == '':
                   no = 'no'
                else:
                   useriprange.append(line)
     return useriprange

  if type(awnser_anonymizing) == list:
     pathlist = []
     selectedlandlist = awnser_anonymizing
     useriprange = []
     for kohr in selectedlandlist:
         kohr = kohr.replace(' ', '')
         countryfile = kohr + '.txt'
         pathlist.append(countryfile)
         selectedlandlist.remove(kohr)
     for durm in pathlist:
        with open(durm) as fp:
             for number,line in enumerate(fp):
                 line = line.replace('\n', '')
                 useriprange.append(line)
     
     if '' in useriprange:
        useriprange.remove('')
      



     return useriprange
    


def ipRange(useriprange):
   import ipaddress
   import os
   os.system('clear')
   print 'Do something good for the enviroment while the IP-adresses are getting calculated'
   Ip_range = []
   for element in useriprange:
        start_ip = useriprange[0]
        start_ip = start_ip.replace(' ','')
        del(useriprange[0])
        end_ip = useriprange[0]
        end_ip = end_ip.replace(' ', '')
        del(useriprange[0])
        start = ipaddress.IPv4Address(unicode(str(start_ip)))
        end = ipaddress.IPv4Address(unicode(str(end_ip)))
        ipaddress_list = [start]
        temp = start
        while temp != end:
              temp += 1
              dost = str(temp)
              dost = dost.replace("'", '')
              Ip_range.append(dost)
   print str(len(Ip_range)) + ' IP-adresses usable for anonymization'
   return Ip_range
   
  
