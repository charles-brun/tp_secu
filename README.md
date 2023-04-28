# TP Scapy

With `tp_server.py` on your 'server' and `tp_client.py` on your 'client', you can copy the content of a file of your 'client' to your 'server', using discret ICMP messages (with delay between encrypted packets).

## Setup

### 'Server' device

- customize `tp_server.py` according to your needs :
    - IP address of your 'client'
    - path of the destination file
- if the device has python3 installed (otherwise get it first) : `pip install scapy simple-file-checksum cryptography`

### 'Client' device

- customize `tp_client.py` according to your needs :
    - IP address of your 'server'
    - path of the source file
    - limits of the random delay value
- if the device has python3 installed (otherwise get it first) : `pip install scapy simple-file-checksum cryptography`

## Use

- execute `tp_server.py` on your 'server'
- execute `tp_client.py` on your 'client'