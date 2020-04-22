#!/usr/bin/env python

'''
On both the NXOS1 and NXOS2 switches configure five VLANs including VLAN names (just pick 5 VLAN numbers between 100 - 999). Use Netmiko's send_config_from_file() method to accomplish this. Also use Netmiko's save_config() method to save the changes to the startup-config.
'''

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

host_nxos1 = {
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    #"fast_cli": True,
    "session_log": './session_logs/session_log_nxos1.txt',
}

host_nxos2 = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    #"fast_cli": True,
    "session_log": './session_logs/session_log_nxos2.txt',
}

host_connect = ConnectHandler(**host_nxos1)

configure_vlans = [
    'vlan 100',
    'vlan 101',
    'vlan 102',
]

#datetime_now = datetime.now()
#print('Current DATE and TIME ---------------->: ' + str(datetime_now) + '\n')

#output = host_connect.send_config_set(configure_name_server)
output = host_connect.send_config_from_file(config_file = 'pyscripts/week_02/vlans.txt')
print(output)
print('\n')

host_connect.disconnect()
