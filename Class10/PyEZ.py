from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from getpass import getpass
from pprint import pprint



pwd = getpass()
a_device = Device(host='50.242.94.227', user='pyclass', password=pwd)
a_device.open()
pprint(a_device.facts)



ports = EthPortTable(a_device)
ports.get()
ports.keys()

ports.items()
ports.values()

ports['fe-0/0/1']
ports['fe-0/0/1'].items()
for k,v in ports['fe-0/0/1'].items():
	print k, v

ports['fe-0/0/1']['oper']
ports['fe-0/0/1']['macaddr']



from jnpr.junos.op.arp import ArpTable
arp_entries = ArpTable(a_device)
arp_entries.get()
arp_entries.items()
arp_entries.keys()
arp_entries.values()


from jnpr.junos.op.phyport import PhyPortTable
phy_ports = PhyPortTable(a_device)
phy_ports.get()
phy_ports.items()
phy_ports.keys()
phy_ports.values()
phy_ports['fe-0/0/1']
phy_ports['fe-0/0/1'].keys()
phy_ports['fe-0/0/1'].items()


from jnpr.junos.op.phyport import PhyPortStatsTable
port_stats = PhyPortStatsTable(a_device)
port_stats.get()
port_stats.keys()
port_stats['fe-0/0/1'].items()


if __name__ == "__main__"


def __main__:
