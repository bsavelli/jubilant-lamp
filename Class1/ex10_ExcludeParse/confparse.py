
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("conf.txt")

intf = cisco_cfg.find_objects(r"^interface")

for i in intf:
    print i.text

fa4 = intf[3]

for child in fa4.children:
    print child.text

crypto_pki = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for child in crypto_pki:
    print child.text

child.is_child
child.is_parent
child.parent
child.all_parents
print "Lines containing crypto map & pfs group 2"
crypto_pki = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO",childspec=r"pfs group2")

for child in crypto_pki:
    print child.text

print "Lines containing crypto map but not AES"
crypto_pki = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO",childspec=r"set AES")

for child in crypto_pki:
    print child.text


"""
crypto_pki = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO",childspec=r"pfs group2")

for child in crypto_pki:
    print child.text
int_txt = CiscoConfParse("interface.txt")
main_int = int_txt.find_objects(r"line protocol is")


for i in main_int:
    print i.text

vlan1 = i 

for child in vlan1.children:
    print child.text
"""
