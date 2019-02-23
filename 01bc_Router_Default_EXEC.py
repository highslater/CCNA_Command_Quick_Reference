#!/usr/bin/env python3

##01bc_Router_Default_LOGIN


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
#####Output: >>>>> Commands Entered
    print("\n***** START *****")
    print("*****" + line)
    print(tn.read_all().decode('ascii'))
    print("***** COMPLETE *****")
    print("*****" + line)


