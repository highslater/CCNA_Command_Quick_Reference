#!/usr/bin/env python3

##01bc_Router_Default_LOGIN


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

##### Configure EXEC Banner
tn.write(b"conf t\n")
tn.write(
b"banner exec &\n\n"\
b"     *****     With Great Power Comes Great Resposibility     *****\n\n&")

tn.write(b"exit\n")
tn.write(b"exit\n")
tn.write(b"cop r s\n")
tn.write(b"\n")
tn.write(b"exit\n")
print("\n\n\n*** START ***")
print(tn.read_all().decode('ascii'))
print("*** COMPLETE ***\n\n\n")

