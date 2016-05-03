import jsonrpclib
from pprint import pprint

ip = '50.242.94.227'
port = '8243'


username = 'eapi'
password = '99saturday'

switch_url = 'https://{}:{}@{}:{}'.format(username, password, ip, port)

switch_url = switch_url + '/command-api'


remote_connect = jsonrpclib.Server(switch_url)

response = remote_connect.runCmds(1, ['show version'])

pprint(response)

response = remote_connect.runCmds(1, ['show arp'])

print response

output_dict = response[0]

"peel back the onions When you are trying to decipher the json return information"

commands = []
commands.append('configure terminal')
commands.append('vlan 225')
commands.insert(0, {'cmd': 'enable', 'input': ''})
commands.append('name green')

remote_connect.runCmds(1, commands)
"blank dictionary returns verify that commands were executed"





