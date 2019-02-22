#!/usr/bin/env python3

##03aa_Router_OSPF


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


##### Configure Loopback 0
tn.write(b"interface loopback 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"exit\n")

##### Configure OSPF
tn.write(b"router ospf 110\n")
tn.write(b"network 0.0.0.0 0.0.0.0 area 0\n")
tn.write(b"passive-interface e0/1\n")
tn.write(b"router-id 1.1.1.1\n")
tn.write(b"exit\n")

##### EXIT, WRITE MEMORY, and LOGOUT
tn.write(b"exit\n")
tn.write(b"exit\n")
tn.write(b"cop r s\n")
tn.write(b"\n")
tn.write(b"exit\n")
print("\n\n\n*** START ***")
print(tn.read_all().decode('ascii'))
print("*** COMPLETE ***\n\n\n")

