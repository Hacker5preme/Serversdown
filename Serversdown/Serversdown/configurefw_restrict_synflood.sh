#!/bin/bash

iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
iptables -A OUTPUT -p tcp --tcp-flags ACK ACK -j DROP
iptables -A OUTPUT -p tcp --tcp-flags FIN FIN -j DROP

