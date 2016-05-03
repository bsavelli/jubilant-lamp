SNMPInterfaceDate.py






snmp_oids = (
    ('sysName', '1.3.6.1.2.1.1.5.0', None),
    ('sysUptime', '1.3.6.1.2.1.1.3.0', None),
    ('ifDescr_fa4', '1.3.5.1.2.1.2.2.1.2.5', None),
    ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5', True),
    ('ifInUcastPkts_fa4', '1.2.6.1.2.1.2.2.1.11.5', True),
    ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5', True),
    ('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5', True),
)

snmp_data = snmp_helper.snmp_get_oud_v3(pynet_rtr2, snmp_user, oid=snmp_oids[0][1])


for desc,an_oid,is_count in snmp_oids:
	snmp_data = snmp_helper.snmp_get_oud_v3(pynet_rtr2, snmp_user, oid=an_oid)
	output = snmp_helper.snmp_extract(snmp_data)
	print "%s %s" % (desc, output)

	
