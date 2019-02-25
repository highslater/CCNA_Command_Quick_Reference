#!/usr/bin/env python3

##00_Router_ISPe_CONFIG


import getpass
import telnetlib

HOST = input("Enter IP Address for ISPe: ")
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
##### 01 Configure  ip access-list
tn.write(b"ip access-list standard ALLOW_NAT\n")
tn.write(b"permit 10.0.0.0 0.0.255.255\n")
tn.write(b"permit 172.16.10.0 0.0.0.255\n")
tn.write(b"permit 172.16.20.0 0.0.0.255\n")
tn.write(b"permit 172.16.30.0 0.0.0.255\n")
tn.write(b"permit 172.16.40.0 0.0.0.255\n")
tn.write(b"exit\n")
##### 02 Configure Ethernet 0/0
tn.write(b"interface e0/0\n")
tn.write(b"description Ethernet LINK to NETWORK 10.0.0.0 /24\n")
tn.write(b"ip address 10.0.0.1 255.255.255.0\n")
tn.write(b"ip nat inside\n")
tn.write(b"no shutdown\n")
tn.write(b"exit\n")
##### 03 Configure Ethernet 0/1
tn.write(b"interface e0/1\n")
tn.write(b"description Ethernet NAT LINK to NETWORK 192.168.1.0 /24 ADDRESS DHCP\n")
tn.write(b"ip address dhcp\n")
tn.write(b"ip nat outside\n")
tn.write(b"no shutdown\n")
tn.write(b"exit\n")
##### 04 Configure ip nat
tn.write(b"ip nat inside source list ALLOW_NAT interface e0/1 overload\n")
##### 05 Configure SERIAL 2/0
tn.write(b"interface serial 2/0\n")
tn.write(b"description Serial LINK to R1 NETWORK 172.16.20.0 /24\n")
tn.write(b"ip address 172.16.20.1 255.255.255.0\n")
tn.write(b"ip nat inside\n")
tn.write(b"no shutdown\n")
tn.write(b"exit\n")
##### 06 Configure SERIAL 2/1
tn.write(b"interface serial 2/1\n")
tn.write(b"description Serial LINK to R2 NETWORK 172.16.10.0 /24\n")
tn.write(b"ip address 172.16.10.1 255.255.255.0\n")
tn.write(b"ip nat inside\n")
tn.write(b"no shutdown\n")
tn.write(b"exit\n")
##### 07 Configure Loopback 0
tn.write(b"interface loopback 0\n")
tn.write(b"ip address 1.0.0.1 255.255.255.255\n")
tn.write(b"no shutdown\n")
tn.write(b"exit\n")
##### 08 Configure RIPv2
tn.write(b"router rip\n")
tn.write(b"passive-interface e0/0\n")
tn.write(b"passive-interface e0/1\n")
tn.write(b"network 172.16.0.0 \n")
tn.write(b"network 1.0.0.0\n")
tn.write(b"default-information originate\n")
tn.write(b"exit\n")
##### Configure EIGRP
tn.write(b"router eigrp 90\n")
tn.write(b"network 172.16.0.0 0.0.255.255\n")
tn.write(b"network 1.0.0.1 0.0.0.0\n")
tn.write(b"passive-interface e0/0\n")
tn.write(b"passive-interface e0/1\n")
tn.write(b"eigrp router-id 1.0.0.1\n")
tn.write(b"no auto-summary\n")
tn.write(b"shutdown\n")
tn.write(b"exit\n")
##### Configure OSPF
tn.write(b"router ospf 110\n")
tn.write(b"network 172.16.0.0 0.0.255.255 area 0\n")
tn.write(b"network 1.0.0.1 0.0.0.0 area 0\n")
tn.write(b"passive-interface e0/0\n")
tn.write(b"passive-interface e0/1\n")
tn.write(b"router-id 1.0.0.1\n")
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

