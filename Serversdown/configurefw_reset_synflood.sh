#!/bin/bash

iptables -D OUTPUT -p tcp --tcp-flags RST RST -j DROP
iptables -D OUTPUT -p tcp --tcp-flags ACK ACK -j DROP
iptables -D OUTPUT -p tcp --tcp-flags FIN FIN -j DROP
