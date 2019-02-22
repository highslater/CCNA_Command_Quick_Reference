#!/usr/bin/env python3


##Switch_Default.py

import getpass
import telnetlib

#####Enter LOGIN Credentials
user = input("Enter your remote account: ")
password = getpass.getpass()
f = open("Switches.txt")

for line in f:

    tn = telnetlib.Telnet(line)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

#####Configure Default Security Settings
    tn.write(b"conf t\n")
    tn.write(b"no ip routing\n")
    tn.write(b"enable secret cisco\n")
    tn.write(b"username ccna privilege 15 secret cisco\n")
    tn.write(b"ip domain-lookup\n")
    tn.write(b"ip domain-name gns3.com\n")
    tn.write(b"line console 0\n")
    tn.write(b"logging synchronous\n")
    tn.write(b"exec-timeout 0 0\n")
    tn.write(b"login local\n")
    tn.write(b"line vty 0 4\n")
    tn.write(b"logging synchronous\n")
    tn.write(b"exec-timeout 0 0\n")
    tn.write(b"login local\n")
    tn.write(b"line aux 0\n")
    tn.write(b"logging synchronous\n")
    tn.write(b"exec-timeout 0 0\n")
    tn.write(b"login local\n")
    tn.write(b"exit\n")

#####Create 10 vlans and MANAGEMENT Vlan
    for n in range(2, 11):
        num = str(n).encode('ascii') + b"\n"
        tn.write(b"vlan " + num)
        tn.write(b"name vlan__" + num)

    tn.write(b"vlan 99\n")
    tn.write(b"name MANAGEMENT\n")

#####Exit, Copy Configuration, and LOGOUT
    tn.write(b"exit\n")
    tn.write(b"exit\n")
    tn.write(b"cop r s\n")
    tn.write(b"\n")
    tn.write(b"exit\n")
    tn.write(b"logout\n")


#####Output: >>>>> Commands Entered
    print("\n***** START *****")
    print("*****" + line)
    print(tn.read_all().decode('ascii'))
    print("***** COMPLETE *****")
    print("*****" + line)

