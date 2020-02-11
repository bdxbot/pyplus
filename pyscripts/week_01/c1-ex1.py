#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

# hostname = input()

host_connect = ConnectHandler(
    host = 'nxos1.lasthop.io',
    # host = hostname,
    username = 'pyclass',
    password = getpass(),
    device_type = 'cisco_nxos',
    # session_log = 'session_log.txt',
)

print(host_connect.find_prompt())
