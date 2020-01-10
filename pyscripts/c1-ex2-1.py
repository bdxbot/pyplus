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
    # session_log: 'session_log.txt',
}

net_connect = ConnectHandler(**host_nxos1)

# print(host_connect.find_prompt())
print(net_connect.find_prompt())
