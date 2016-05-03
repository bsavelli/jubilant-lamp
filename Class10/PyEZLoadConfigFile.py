from jnpr.junos import Device
from getpass import getpass




pwd = getpass()


a_device = Device(host='50.242.94.227', user='pyclass', password=pwd)
a_device.timeout = 120 
a_device.open()

a_device.facts


from jnpr.junos.utils.config import Config
cfg = Config(a_device)

cfg.lock()

cfg.load("set system host-name pytest", format="set", merge=True)

cfg.rollback(0)


print cfg.diff()

cfg.commit(comment="testing commit comment using PyEZ")



'''loading from a file'''

cfg.load(path="test_config.conf", format="text", merge=True)


'''loading from a file but this time using the replace option'''

cfg.load(path="test_replace.conf", format="text", merge=False)

'''loading from an .xml file'''

cfg.load(path="test_config.xml", format="xml", merge=True)

'''overwriting from an .xml file'''

cfg.load(path="full_config.xml", format="xml", overwrite=True)

