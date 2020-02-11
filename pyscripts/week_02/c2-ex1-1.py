#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

# hostname = input()

host_cisco4 = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
    "session_log": './session_logs/session_log_cisco4.txt',
}

hosts_dict = [host_cisco4]

host_connect = ConnectHandler(**host_cisco4)

# print(host_connect.find_prompt())

print(host_connect.send_command('ping 8.8.8.8'))
