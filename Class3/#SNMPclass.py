#SNMP class


1.3.6.1.2.1.1.1

from snmp_helper import snmp_get_oid, snmp_extract


COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161
IP = " "

device_name = (IP, COMMUNITY_STRING, SNMP_PORT)
OID = '1.3.6.1.2.1.1.0'

snmp_data = snmp_get_oid(device_name, oid=OID)
print snmp_data

output = snmp_extract(snmp_data)

print output