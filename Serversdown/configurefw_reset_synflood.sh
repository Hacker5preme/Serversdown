#!/bin/bash

iptables -D OUTPUT -p tcp --tcp-flags RST RST -j DROP

