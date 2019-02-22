#!/usr/bin/env python3

##01bb_Router_Default_LOGIN


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
tn.write(
b"banner login &\n\n"\
b" UNAUTHORIZED ACCESS TO THIS DEVICE IS PROHIBITED\n\n"\
b"   You must have explicit, authorized permission to access or configure this device.\n"\
b"   Unauthorized attempts and actions to access or use this system may result in civil and/or\n"\
b"   criminal penalties.\n"\
b"   All activities performed on this device are logged and monitored.\n\n"\
b" UNAUTHORIZED ACCESS TO THIS DEVICE IS PROHIBITED\n\n\n &\n")




tn.write(b"exit\n")
tn.write(b"exit\n")
tn.write(b"cop r s\n")
tn.write(b"\n")
tn.write(b"exit\n")
print("\n\n\n*** START ***")
print(tn.read_all().decode('ascii'))
print("*** COMPLETE ***\n\n\n")

