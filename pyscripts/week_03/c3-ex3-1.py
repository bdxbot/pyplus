'''
Read this JSON data in from a file.

From this data structure extract all of the IPv4 and IPv6 addresses that are 
used on this NXOS device. From this data create two lists: 'ipv4_list' and 
'ipv6_list'. The 'ipv4_list' should be a list of all of the IPv4 addresses 
including prefixes; the 'ipv6_list' should be a list of all of the IPv6 
addresses including prefixes.
'''

import json
from pprint import pprint

filename = "/home/day/pyplus/pyscripts/week_03/int_data.json"
with open(filename) as f:
   json_data = json.load(f)

#pprint(json_data.keys())

ipv4_list = []
ipv6_list = []

# dictionary inception, this first layer lets us dig into the first key/value
# pair of interface/ip address
for intface, ip_type in json_data.items(): 
    # this second layer lets us dig into the ip version/ip k/v pair
    for ip_ver, ip in ip_type.items():
        #pprint(v4_v6)
        #pprint(ip)
        #print('=' * 20)
        for ip_addr, prefix in ip.items():
            #pprint(v4_v6)
            #pprint(ip)
            for prefix_length, cidr in prefix.items():
                if ip_ver == 'ipv4':
                    #pprint(ip_addr)
                    #pprint(prefix)
                    #print('=' * 20)
                    #ipv4_list.append(ip_addr)
                    #ipv4_list.append(cidr)
                    ipv4_list.append('{}/{}'.format(ip_addr, cidr))
                elif ip_ver == 'ipv6':
                    ipv6_list.append('{}/{}'.format(ip_addr, cidr))
                    
                    
print(ipv4_list)
print(ipv6_list)
