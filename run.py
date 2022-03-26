# Imports
from scapy.all import *
from pprint import pprint
import operator
from tqdm import tqdm, trange

# Parameters
interface = "eth0"                      # Interface you want to use
dns_source = "172.20.10.2"                 # IP of that interface


with open("dns_list.txt", "r") as f:
    file  = f.read()

dns_destination = file.split()

time_to_live = 128                                                                 # IP TTL 
query_name = "www.google.com"                                                          # DNS Query Name
query_type = 255 # DNS Query Types

# Initialise variables
results = []
packet_number=0
total_response = 0
total_request = 0

ans = []

# Loop through all query types then all DNS servers

for j in trange(0, len(dns_destination)):
    packet_number += 1

    # Craft the DNS query packet with scapy
    packet = IP(src=dns_source, dst=dns_destination[j], ttl=time_to_live) / UDP() / DNS(rd=1, qd=DNSQR(qname=query_name, qtype=query_type))
        
        # Sending the packet
    try:
        query = sr1(packet,iface=interface,verbose=False, timeout=8)
        
        if len(query)/len(packet) > 5:
            ans.append(dns_destination[j])
            print("Got one")
    except:
        pass
        
with open("new_dns.txt", "w") as f:
    for item in ans:
        f.write(item + "\n")
