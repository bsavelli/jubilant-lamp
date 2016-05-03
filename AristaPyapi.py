''' be sure to check the .eapi.conf hosts file to see the list of variables that are 
being used to set up the environment for connecting to the devices'''

import pyeapi
from pprint import pprint

pynet_sw3 = pyeapi.connect_to("pynet-sw3")
pynet_sw4 = pyeapi.connect_to("pynet-sw4")

pynet_sw3.get_config()

my_config = pynet_sw3.get_config()
for line in my_config:
	print line


pynet_sw3.get_config(as_string=True)

pynet_sw3.enable('show version')

show_version = pynet_sw3.enable('show version')

pprint(show_version)

show_arp = pynet_sw3.enable("show arp")
pprint(show_arp)

cmds = ['vlan 225', 'name red', 'vlan 226', 'name black']
show_arp = pynet_sw4.config(cmds)
"remember empty dictionaries mean success"

cmds = ['no vlan 225', 'no vlan 226']
output = pynet_sw4.enable("write memory")
pprint(output)