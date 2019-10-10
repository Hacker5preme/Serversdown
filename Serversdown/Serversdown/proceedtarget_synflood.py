#!/usr/bin/env python

def proceedtarget(destination):
    import socket
    destinationnew = str(destination)
    if 'h' in destinationnew: 
       if 'https://' in destinationnew:
           destinationnew = destinationnew.replace('https://', '')
       if 'http://' in destinationnew:
           destinationnew = destiantionnew.replace('http://', '')
       
       destinationnew = str(socket.gethostbyname(destinationnew))
       return destinationnew
    else:
       return destinationnew
