#!/bin/bash

echo "===== System Health Stats ====="
echo "Date & Time: $(date)"
echo

#  CPU load
echo ">> CPU Load:"
uptime | awk -F'load average:' '{print $2 }'

# RAM Usage
echo ">> RAM Usage:"
free -m | awk 'NR==2 {printf "Used: %sMB / Total: %sMB (%.2f%%)\n", $3,$2,$3*100/$2}'

#Disk Usage
echo ">>Disk Usage:"
df -h --total | grep total | awk '{print "Used: "$3" / Total: "$2" ("$5" used)"}'
echo

# Network Status
echo ">> Network (Packets):"
ifconfig | grep "RX packets\|TX packets"
echo "================================"


