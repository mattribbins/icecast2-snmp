#! /usr/bin/python3
# -*- mode: python; coding: utf-8-unix; -*-

# Icecast2 SNMP
# Author: Matt Ribbins (mattyribbo.co.uk) for Celador Radio (celador.co.uk)

# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


#################
# Configuration #
#################
import os
# Hostname of Icecast server
# Just canonical name, no http:// nor ending /, include port number if required
host = os.getenv('ice2host','localhost:8000')
# Username and password to the administration panel
username = os.getenv('ice2user','admin')
password = os.getenv('ice2pass','hackme')


#######################
# Magic happens below #
#######################
import os.path, time, sys, getopt
import requests
from xml.dom import minidom

host = "http://" + host + "/admin/stats"


def munin_print(u):
	sys.stdout.buffer.write((u+"\n").encode('ascii','replace'))

def ic2xml():
	# Get
	try:
	    opts, args = getopt.getopt(sys.argv[1:], "hls", ["total-listeners", "total-sources"])
	except getopt.GetoptError:
	    print("-1")
	    exit(1)

	# Get the XML with all the stats information.
	req = requests.get(host, auth=(username, password))

	xmldoc = minidom.parseString(req.text)
	xmldoc = xmldoc.firstChild


	for opt, arg in opts:
		if opt == '-h':
			exit(1)
		elif opt in ("-l", "--total-listeners"):
			total_listeners = int(xmldoc.getElementsByTagName("listeners")[0].firstChild.nodeValue)
			total_listeners = round(total_listeners)
			print(total_listeners)

		elif opt in ("-s", "-total-sources"):
			total_sources = int(xmldoc.getElementsByTagName("sources")[0].firstChild.nodeValue)
			total_sources = round(total_sources)
			print(total_sources)


if __name__ == "__main__":
	ic2xml()
