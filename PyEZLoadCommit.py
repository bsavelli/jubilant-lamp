from jnpr.junos import Device
from getpass import getpass




pwd = getpass()


a_device = Device(host='50.242.94.227', user='pyclass', password=pwd)
a_device.open()

a_device.facts


from jnpr.junos.utils.config import Config
cfg = Config(a_device)

cfg.lock()

cfg.load("set system host-name pytest", format="set", merge=True)

cfg.rollback(0)


print cfg.diff()

cfg.commit(comment="testing commit comment using PyEZ")

