#!/usr/bin/env python

'''
Use Netmiko and the send_config_set() method to configure the following on the Cisco3 router.

ip name-server 1.1.1.1
ip name-server 1.0.0.1
ip domain-lookup

Experiment with fast_cli=True to see how long the script takes to execute (with and without this option enabled).

Verify DNS lookups on the router are now working by executing 'ping google.com'. Verify from this that you receive a ping response back.
'''

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

host_cisco3 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    "fast_cli": True,
    "session_log": './session_logs/session_log_cisco3.txt',
}

hosts_dict = [host_cisco3]

host_connect = ConnectHandler(**host_cisco3)

configure_name_server = [
    'ip name-server 1.1.1.1',
    'ip name-server 1.0.0.1',
    'ip domain-lookup'
]

datetime_now = datetime.now()
print('Current DATE and TIME ---------------->: ' + str(datetime_now) + '\n')

output = host_connect.send_config_set(configure_name_server)
print(output)
print('\n')

datetime_now = datetime.now()
print('Current DATE and TIME ---------------->: ' + str(datetime_now) + '\n')

output = host_connect.send_command('ping google.com')
print(output)
print('\n')

datetime_now = datetime.now()
print('Current DATE and TIME ---------------->: ' + str(datetime_now) + '\n')

host_connect.disconnect()
