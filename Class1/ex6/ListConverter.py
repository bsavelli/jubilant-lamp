#!/usr/bin/env python

import yaml
import json

ex6_list = ['Cisco']
ex6_list.append('Juniper')
ex6_list.append('Arista')
ex6_list.append({})
ex6_list[-1]['Ethernet'] = 'Cat6'
ex6_list[-1]['Fiber'] = 'Single Mode SR'
ex6_list.append(range(5))
print ex6_list  

with open("ex6_YAML.yml", "w") as f:
    f.write(yaml.dump(ex6_list, default_flow_style=False))

with open("ex6_JSON.json", "w") as f:
    json.dump(ex6_list, f) 

