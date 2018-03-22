#!/bin/bash
if [ "$1" = "-g" ]
then
echo .1.3.6.1.4.1.8000.2.1
echo gauge
python3 /usr/local/bin/icecast2-snmp.py -l
fi
exit 0
