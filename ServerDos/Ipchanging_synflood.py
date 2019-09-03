#!/usr/bin/env python

def chooseiprange(awnser_anonymizing, supcountries):
  if awnser_anonymizing in supcountries:
     selectland = awnser_anonymizing
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
    


def ipRange(useriprange):
  print(useriprange)
  Ip_range = []
  while len(useriprange) > 0:   
    start_ip = useriprange[0]
    end_ip = useriprange[1]
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    temp = start
    del(useriprange[0])
    del(useriprange[0])
    Ip_range.append(start_ip)
    while temp != end:
       start[3] += 1
       for i in (3, 2, 1):
          if temp[i] == 256:
             temp[i] = 0
             temp[i-1] += 1
       Ip_range.append(".".join(map(str, temp)))
       
   
  print 'IP-adress useable: ' + str(len(Ip_range))
  return Ip_range


