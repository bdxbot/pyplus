#!/usr/bin/env python

'''
Use the extended 'ping' command and Netmiko on the 'cisco4' router. This should prompt you for additional information as follows:

cisco4#ping
Protocol [ip]: 
Target IP address: 8.8.8.8
Repeat count [5]: 
Datagram size [100]: 
Timeout in seconds [2]: 
Extended commands [n]: 
Sweep range of sizes [n]: 
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/4 ms

a. Use send_command_timing() to handle the additional prompting from this 'ping' command. Specify a target IP address of '8.8.8.8'

b. Use send_command() and the expect_string argument to handle the additional prompting. Once again specify a target IP address of '8.8.8.8'.
'''

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
# print(host_connect.send_command('ping 8.8.8.8'))

output = host_connect.send_command('ping', expect_string=r'\:')
output += host_connect.send_command('\n', expect_string=r'\:')
output += host_connect.send_command('8.8.8.8', expect_string=r'\:')
output += host_connect.send_command('\n', expect_string=r'\:')
output += host_connect.send_command('\n', expect_string=r'\:')
output += host_connect.send_command('\n', expect_string=r'\:')
output += host_connect.send_command('\n', expect_string=r'\:')
output += host_connect.send_command('\n', expect_string=r'\:')


host_connect.disconnect()

print(output)
