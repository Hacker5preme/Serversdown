#!/usr/bin/env python

def checkserversdown(destination):
    import requests
    import time
    url = str(destination)
    try:
       requests.get(url)
       print 'Website is still up'
       print 'Still attacking'
    except requests.exceptions.ConnectionError:
       print 'SERVERSDOWN!!!'
       print 'ATTACK SUCCESFULL!!!'
       time.sleep(10)
       
 
