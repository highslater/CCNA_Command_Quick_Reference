#!/usr/bin/env python3

##03_Router_R3_CONFIG


import getpass
import telnetlib

HOST = input("Enter IP Address of R3: ")
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
##### Configure SERIAL 2/0
tn.write(b"interface serial 2/0\n")
tn.write(b"description Serial LINK to R1 NETWORK 172.16.40.0 /24\n")
tn.write(b"ip address 172.16.40.2 255.255.255.0\n")
tn.write(b"no shutdown\n")
tn.write(b"exit\n")
##### Configure ETHERNET 0/0
tn.write(b"interface ethernet 0/0\n")
tn.write(b"description Ethernet LINK to MANAGEMENT NETWORK 10.0.0.0 /24\n")
tn.write(b"ip address 10.0.0.8 255.255.255.0\n")
tn.write(b"no shutdown\n")
tn.write(b"exit\n")
##### Configure ETHERNET 0/1
tn.write(b"interface ethernet 0/1\n")
tn.write(b"description Ethernet LINK to LAN NETWORK 10.0.4.0 /24\n")
tn.write(b"ip address 10.0.4.1 255.255.255.0\n")
tn.write(b"no shutdown\n")
tn.write(b"exit\n")
##### 07 Configure Loopback 0
tn.write(b"interface loopback 0\n")
tn.write(b"ip address 3.3.3.3 255.255.255.255\n")
tn.write(b"no shutdown\n")
tn.write(b"exit\n")
##### 08 Configure RIPv2
tn.write(b"router rip\n")
tn.write(b"network 10.0.0.0\n")
tn.write(b"network 172.16.0.0\n")
tn.write(b"network 3.0.0.0\n")
tn.write(b"exit\n")
##### Configure EIGRP
tn.write(b"router eigrp 90\n")
tn.write(b"network 10.0.4.1 0.0.0.0\n")
tn.write(b"network 172.16.40.2 0.0.0.0\n")
tn.write(b"network 3.3.3.3 0.0.0.0\n")
tn.write(b"passive-interface e0/0\n")
tn.write(b"passive-interface e0/1\n")
tn.write(b"eigrp router-id 3.3.3.3\n")
tn.write(b"no auto-summary\n")
tn.write(b"no shutdown\n")
tn.write(b"exit\n")
##### Configure OSPF
tn.write(b"router ospf 110\n")
tn.write(b"network 10.0.4.1 0.0.0.0 area 0\n")
tn.write(b"network 172.16.40.2 0.0.0.0 area 0\n")
tn.write(b"network 3.3.3.3 0.0.0.0 area 0\n")
tn.write(b"passive-interface e0/0\n")
tn.write(b"passive-interface e0/1\n")
tn.write(b"router-id 3.3.3.3\n")
tn.write(b"shutdown\n")
tn.write(b"exit\n")
#####
tn.write(b"exit\n")
tn.write(b"cop r s\n")
tn.write(b"\n")
tn.write(b"exit\n")
print("\n\n\n*** START ***")
print(tn.read_all().decode('ascii'))
print("*** COMPLETE ***\n\n\n")

