#!/usr/bin/env python

def uanoIP():
    from requests import get
    yourIP = get('https://api.ipify.org').text
    return yourIP

