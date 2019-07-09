SNMP passthrough for Icecast2
=============================

This is a simple script to pass basic Icecast information via SNMP. The script
will expose the number of listeners and the number of sources.

Requirements
------------
* Icecast 2 server
* Python 3 with Requests library

Installation
---------------------
* Set up the `snmpd` daemon
* Install Python3 if not already installed. Ensure the requests library is installed (usually by default)
* Copy the icecast2-snmp.py and bash example scripts to a folder, for example /usr/local/bin/. Edit the sh scripts, ensure they point to the correct folder that icecast2-snmp.py is located!
* Edit the snmpd passthrough configuration, look at snmpd.conf.example as an example.

Usage
-----
Set up the SNMP passthrough scripts as appropriate. icecast2-snmp.py can report the following information:
* ``-l --total-listeners`` reports the number of total listeners connected to the server
* ``-s -total-sources`` reports the number of sources connected to the server
* ``-c <stream-name> --check-stream=<stream-name>`` reports the number of listeners on a stream, -1 if stream doesn't exist

Testing
-------
Once the sensor is working correctly natively, and the setup of the snmpd is
completed, you can run a SNMP client to check values are coming through.
Check all SNMP values
```
$ snmpget -v 1 -c public 127.0.0.1 .1.3.6.1.4.1.8000.2.1
```
