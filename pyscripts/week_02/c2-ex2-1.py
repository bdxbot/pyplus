#!/usr/bin/env python

'''
 Create a Netmiko connection to the 'nxos2' device using a global_delay_factor of 2. Execute 'show lldp neighbors detail' and print the returned output to standard output. Execute 'show lldp neighbors detail' a second time using send_command() with a delay_factor of 8. Print the output of this command to standard output. Use the Python datetime library to record the execution time of both of these commands. Print these execution times to standard output.
'''

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

# hostname = input()

host_nxos1 = {
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
    "session_log": './session_logs/session_log_nxos1.txt',
}

hosts_dict = [host_nxos1]

host_connect = ConnectHandler(**host_nxos1, global_delay_factor = 2)

datetime_now = datetime.now()
print('Current DATE and TIME ---------------->: ' + str(datetime_now) + '\n')
output = host_connect.send_command_timing('show lldp neighbor detail')
print(output)
datetime_now = datetime.now()
print('Current DATE and TIME ---------------->: ' + str(datetime_now) + '\n')

datetime_now = datetime.now()
print('Current DATE and TIME ---------------->: ' + str(datetime_now) + '\n')
output = host_connect.send_command_timing('show lldp neighbor detail', delay_factor = 8)
print(output)
datetime_now = datetime.now()
print('Current DATE and TIME ---------->: ' + str(datetime_now) + '\n')

host_connect.disconnect()
