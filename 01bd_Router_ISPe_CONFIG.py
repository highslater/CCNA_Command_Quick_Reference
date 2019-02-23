#!/usr/bin/env python3

##01bd_Router_ISPe_CONFIG


import getpass
import telnetlib

HOST = input("Enter HOST ADDRESS: ")
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
tn.write(b"permit 10.0.0.0 0.0.0.255\n")
tn.write(b"exit\n")
##### 02 Configure Ethernet 0/1
tn.write(b"interface e0/1\n")
tn.write(b"description Ethernet NAT LINK to NETWORK 192.168.1.0 /24 ADDRESS DHCP\n")
tn.write(b"ip address dhcp\n")
tn.write(b"ip nat outside\n")
tn.write(b"no shutdown\n")
tn.write(b"exit\n")
##### 03 Configure ip nat
tn.write(b"ip nat inside source list ALLOW_NAT interface e0/1 overload\n")
##### Configure SERIAL 2/0
tn.write(b"interface serial 2/0\n")
tn.write(b"description Serial LINK to R1 NETWORK 172.16.20.0 /24\n")
tn.write(b"ip address 172.16.20.1 255.255.255.0\n")
tn.write(b"no shutdown\n")
tn.write(b"exit\n")

tn.write(b"exit\n")
tn.write(b"cop r s\n")
tn.write(b"\n")
tn.write(b"exit\n")
print("\n\n\n*** START ***")
print(tn.read_all().decode('ascii'))
print("*** COMPLETE ***\n\n\n")
