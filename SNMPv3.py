SNMPv3.py

import snmp-helper


'''Cisco SNMP server commands for local testing of SNMPv3 

snmp-server view VIEWSTD iso included
snmp-server group READONLY v3 priv read VIEWSTD access 98
snmp-server user pysnmp READONLY v3 auth sha galileo1 priv aes 128 galileo1'''

if True:

	IP = 'lab env'

	a_user = '50.76.53.27'
	auth_key = 'galileo1'
	encrypt_key = 'galileo1'

	snmp_user = (a_user, auth_key, encrypt_key)

	pynet_rtr1 = (IP, 7961)
	pynet_rtr2 = (IP, 8061)

snmp_data = snmp-helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid='1.3.6.1.2.1.1.5.0')
output  = snmp-helper.snmp_extract(snmp_data)
print output
