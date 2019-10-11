#!/usr/bin/env python

def configurefw(check):
    import subprocess
    if check == 'restrict':
        os.system('clear')
        print 'Restricitng firewall rules to perform SYN attack'
        subprocess.call('./configurefw_restrict_synflood.sh')
    if check == 'reset':
        os.system('clear')
        print 'Reseting firewall rules'
        subprocess.call('./configurefw_reset_synflood.sh')
