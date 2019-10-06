#!/usr/bin/env python

def checkserversdown(destination):
    import requests
    import time
    import os
    url = str(destination)
    os.system('clear')
    try:
       requests.get(url)
       print 'Website is still up'
       print 'Still attacking'
       time.sleep(1)
    except requests.exceptions.ConnectionError:
       print 'SERVERSDOWN!!!'
       print 'ATTACK SUCCESFULL!!!'
       time.sleep(10)
       



