from netmiko import ConnectHandler
from getpass import getpass




pynet1 = {
	'device_type': 'cisco_ios',
	'ip': '50.76.53.27',
	'username': 'pyclass',
	'password': password,
}

pynet2 = {
	'device_type': 'cisco_ios',
	'ip': '50.76.53.27',
	'username': 'pyclass',
	'password': password,
	'port': 8022,
}

juniper_srx = {
	'device_type': 'juniper',
	'ip': '50.76.53.27',
	'username': 'pyclass',
	'password': password,
	'secret': '',
	'port': 9822,
}


pynet_rtr1 = ConnectHandler(**pynet1)
pynet_rtr2 = ConnectHandler(**pynet2)
srx = ConnectHandler(**juniper_srx)

output = pynet_rtr1.send_command('show run | inc logging')
print output
config_commands = ['logging buffered 19999']
output = pynet_rtr1send_config_set(config_commands)
output = pynet_rtr1.send_command('show run | inc logging')
print output

#netstat -an | grep 50.76.53. to search for active ssh sessions 