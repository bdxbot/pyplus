#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

# hostname = input()

host_cisco3 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
    "session_log": './session_logs/session_log_cisco3.txt',
}

hosts = [host_cisco3]

for x in hosts:
    net_connect = ConnectHandler(**x)
    print(net_connect.find_prompt())
    print(net_connect.send_command('show version'))
