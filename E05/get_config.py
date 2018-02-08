#!/usr/bin/python
#
# Get configs using Netconf
#
# darien@sdnessentials.com
#

from ncclient import manager
import sys
import xml.dom.minidom

# Decvice IP or FQDN
HOST = str(sys.argv[2]).replace(",", "")
# NETCONF port 
PORT = str(sys.argv[3]).replace(",", "")
# credentials
USER = str(sys.argv[4]).replace(",", "")
PASS = str(sys.argv[5]).replace(",", "")
# XML filter file to open
FILE = sys.argv[6]

def get_config():
    """Main method that retrieves the interfaces from config via NETCONF."""
    print FILE

    with manager.connect(host=HOST, port=PORT, username=USER, password=PASS,
                         hostkey_verify=False, device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:

        with open(FILE) as f:
            return(m.get_config('running', f.read()))

# create a main() method
def main(argv):
    """Simple main method calling our function."""
    snippet = get_config()
    print(xml.dom.minidom.parseString(snippet.xml).toprettyxml())

if __name__ == '__main__':
   main(sys.argv[1:])