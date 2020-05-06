'''
Using the below ARP data, create a five element list. Each list element should
be a dictionary with the following keys: "mac_addr", "ip_addr", "interface". 
At the end of this process, you should have five dictionaries contained inside 
a single list.
'''

import re
from pprint import pprint

arp_data = '''
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
'''

# the above returns a '' string if you do .splitlines(), so first we must remove
# that '' with .strip()
arp_data = arp_data.strip()

# we then take the string and create a list with .splitlines(), at each /n,
# a new element is created
arp_data = arp_data.splitlines()

#pprint(arp_data)
#pprint(arp_data[2])
#pprint(arp_data[3])

# now that the arp data is in a list, we need to make a new list to dump the 
# info we want into the new list
new_list = []

# we now need to iterate over the orignal list and grab the info we want. 
# from there we can dump it into the new list.
for entry in arp_data:
    #pprint(entry)
    # first we need to remove the headers by using regex to match all 
    # characters between Protocol and Interface
    if re.search(r"^Protocol.*Interface", entry):
        continue
    # for each entry in arp_data, we need to split each column into its own
    # item. we can do that using .split(), which will take the string from each
    # list element in arp_data and split it at every space
    
    # TODO: figure out what this is doing
    proto, ip_addr, age, mac_addr, learn, intface = entry.split()
    new_dict = {"mac_addr": mac_addr, "ip_addr": ip_addr, "interface": intface}
    new_list.append(new_dict)

pprint(new_list)
