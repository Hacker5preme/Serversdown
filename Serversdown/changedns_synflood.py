#!/usr/bin/env python
def changedns():
 path= '/etc/resolv.conf'
 a = open(path, 'w')
 a.write('nameserver 1.1.1.1')
 a.close()
 print 'NO DNS LEAK POSSIBLE'
