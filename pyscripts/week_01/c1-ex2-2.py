#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

# hostname = input()

host_nxos1 = {
    "host": 'nxos1.lasthop.io',
    # "host" = hostname,
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
    # session_log: 'session_log_nxos1.txt',
}


host_nxos2 = {
    "host": 'nxos2.lasthop.io',
    # "host" = hostname,
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
    # session_log: 'session_log_nxos2.txt',
}

hosts = [host_nxos1, host_nxos2]

# net_connect = ConnectHandler(**host_nxos1)
for x in hosts:
    net_connect = ConnectHandler(**x)
    print(net_connect.find_prompt())
    # print(x)    

# print(host_connect.find_prompt())
# print(net_connect.find_prompt())
