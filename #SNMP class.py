#!/usr/bin/env python

from snmp_helper import snmp_get_oid, snmp_extract


COMMUNITY_STRING = 'galileo'
SNMP_PORT = [7961 , 8061]
IP = '50.76.53.27'
OID = ['1.3.6.1.2.1.1.1.0' , '1.3.6.1.2.1.1.5.0']
for port in SNMP_PORT:
	for item in OID:
        snmp_data = snmp_get_oid(device_name, item)
        print snmp_data
    device_name = (IP, COMMUNITY_STRING, port)
    print port


"""output = snmp_extract(snmp_data)

print output

from snmp_helper import snmp_get_oid, snmp_extract


COMMUNITY_STRING = 'galileo'
SNMP_PORT = 8061
IP = '50.76.53.27'

device_name = (IP, COMMUNITY_STRING, SNMP_PORT)
OID = '1.3.6.1.2.1.1.0'

snmp_data = snmp_get_oid(device_name, oid=OID)
print snmp_data

output = snmp_extract(snmp_data)

print output"""
~