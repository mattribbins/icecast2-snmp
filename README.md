SNMP passthrough for Icecast2
=============================

This is a simple script to pass basic Icecast information via SNMP. The script
will expose the number of listeners and the number of sources.

Requirements
------------
* Icecast 2 server
* Python 3

Installation
---------------------
* Set up the `snmpd` daemon
* Copy the icecast2-snmp.py, icecast2-listeners.sh and icecast2-sources.sh to a folder, for example /usr/local/bin/. Edit the sh scripts to point to the correct folder that icecast2-snmp.py is located!
* Edit the snmpd passthrough configuration, look at snmpd.conf.example as an example.

Testing
-------
Once the sensor is working correctly natively, and the setup of the snmpd is
completed, you can run a SNMP client to check values are coming through.
Check all SNMP values
```
$ snmpget -v 1 -c public 127.0.0.1 .1.3.6.1.4.1.8000.2.1
```
