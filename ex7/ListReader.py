#!/usr/bin/env python

import yaml
import json

ex7_list = ['Cisco']
ex7_list.append('Juniper')
ex7_list.append('Arista')
ex7_list.append({})
ex7_list[-1]['Ethernet'] = 'Cat6'
ex7_list[-1]['Fiber'] = 'Single Mode SR'
ex7_list.append(range(5))

with open("ex7_YAML.yml", "w") as f:
    f.write(yaml.dump(ex7_list, default_flow_style=False))


with open("ex7_YAML.yml") as f:
    yaml_list = yaml.load(f)
print "yaml_list Completed"

with open("ex7_JSON.json") as f:
    json_list = json.load(f)
print "json_list Completed"

from pprint import pprint as pp
pp(json_list)
