#!/usr/bin/env python

def checkserversdown(destination):
    import requests
    import time
    import os
    from configurefw_synflood import configurefw
    url = str(destination)
    os.system('clear')
    configurefw('reset')
    try:
       requests.get(url)
       print 'Website is still up'
       print 'Still attacking'

       time.sleep(1)
    except requests.exceptions.ConnectionError:
       print 'SERVERSDOWN!!!'
       print 'ATTACK SUCCESFULL!!!'
       time.sleep(10)
    configurefw('restrict')
