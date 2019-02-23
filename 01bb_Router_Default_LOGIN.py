#!/usr/bin/env python3

##01bb_Router_Default_LOGIN


import getpass
import telnetlib

user = input("Enter your remote account: ")
password = getpass.getpass()

f= open("Routers.txt")

for line in f:
    tn = telnetlib.Telnet(line)
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
#####Output: >>>>> Commands Entered
    print("\n***** START *****")
    print("*****" + line)
    print(tn.read_all().decode('ascii'))
    print("***** COMPLETE *****")
    print("*****" + line)


