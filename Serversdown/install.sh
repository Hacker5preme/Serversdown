#!/bin/bash
apt-get install pypy pypy:dev
wget https://bootstrap.pypa.io/get-pip.py
pypy get-pip.py
pypy -m pip install scapy
pypy -m pip install multiprocessing
pypy -m pip install ipaddress
pypy Serversdown.py


