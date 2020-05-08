'''
2a. Create a list where each of the list elements is a dictionary representing
one of the network devices in the lab. Do this for at least four of the lab
devices. The dictionary should have keys corresponding to the device_name,
host (i.e. FQDN), username, and password. Use a fictional username/password
to avoid checking the lab password into GitHub.

2b. Write the data structure you created in part 2a out to a YAML file. Use
expanded YAML format. How could you re-use this YAML file later when creating
Netmiko connections to devices?
'''

import yaml
from pprint import pprint

cisco3 = {"device_name": "cisco3", "host": "cisco3.lasthop.io", "username": "fake_user", "password": "fake_password"}
arista1 = {"device_name": "arista1", "host": "arista1.lasthop.io", "username": "fake_user", "password": "fake_password"}
srx2 = {"device_name": "srx2", "host": "srx2.lasthop.io", "username": "fake_user", "password": "fake_password"}
nxos1 = {"device_name": "nxos1", "host": "nxos1.lasthop.io", "username": "fake_user", "password": "fake_password"}

device_list = [cisco3, arista1, srx2, nxos1]

pprint(device_list)

# explicit_start=True adds the --- at the top of the YAML file
# default_flow_styles=False expands the data, True collapses the data
yaml.dump(device_list, explicit_start=True, default_flow_style=False)
