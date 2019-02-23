#!/usr/bin/env python3


##Switch_Default.py

import getpass
import telnetlib

#####Enter LOGIN Credentials
user = input("Enter your remote account: ")
password = getpass.getpass()
HOST = input("Enter HOST Address :")


tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

print("STARTING")
#####Write to startup config
#####Issue RELOAD command
tn.write(b"reload in 001\n")
print("RELOAD Command Given")
#tn.read_until(b"Proceed with reload?  [confirm]")
tn.write(b"\n")
print("CONFIRMED 1")
tn.write(b"\n")
print("CONFIRMED 2")
#####Output: >>>>> Commands Entered
tn.write(b"exit\n")
print("\n***** START *****")
print("*****")
print(tn.read_all().decode('ascii'))
print("***** COMPLETE *****")
print("*****")

