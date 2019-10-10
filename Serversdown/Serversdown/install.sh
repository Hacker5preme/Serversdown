#!/bin/bash
apt-get install pypy pypy-dev
wget https://bootstrap.pypa.io/get-pip.py
pypy get-pip.py
pypy -m pip install scapy
pypy -m pip install multiprocessing
pypy -m pip install ipaddress
pypy -m pip install requests
pypy -m pip install subprocess
chmod u+rx configurefw_restrict_synflood.sh
chmod u+rx configurefw_reset_synflood.sh
pypy Serversdown.py


