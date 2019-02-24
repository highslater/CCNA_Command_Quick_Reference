#!/usr/bin/env python3

##01bf_Router_R2_CONFIG


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
##### Configure SERIAL 2/0
tn.write(b"interface serial 2/0\n")
tn.write(b"description Serial LINK to ISPe NETWORK 172.16.20.0 /24\n")
tn.write(b"ip address 172.16.20.2 255.255.255.0\n")
tn.write(b"no shutdown\n")
tn.write(b"exit\n")

##### Configure ETHERNET 0/0
tn.write(b"interface ethernet 0/0\n")
tn.write(b"description Ethernet LINK to LAN NETWORK 10.0.1.0 /24\n")
tn.write(b"ip address 10.0.1.1 255.255.255.0\n")
tn.write(b"no shutdown\n")
tn.write(b"exit\n")

##### Configure ETHERNET 0/1
tn.write(b"interface ethernet 0/1\n")
tn.write(b"description Ethernet LINK to LAN NETWORK 10.0.0.0 /24\n")
tn.write(b"ip address 10.0.0.3 255.255.255.0\n")
tn.write(b"no shutdown\n")
tn.write(b"exit\n")

tn.write(b"exit\n")
tn.write(b"cop r s\n")
tn.write(b"\n")
tn.write(b"exit\n")
print("\n\n\n*** START ***")
print(tn.read_all().decode('ascii'))
print("*** COMPLETE ***\n\n\n")

