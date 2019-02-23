#!/usr/bin/env python3

##01a_Router_Default


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
##### Configure MOTD Banner
    tn.write(
    b"banner motd &\n\n\n"\
    b" CCNA Command Quick Reference\n\n&\n")
##### Configure LOGIN Banner
    tn.write(
    b"banner login &\n\n"\
    b" UNAUTHORIZED ACCESS TO THIS DEVICE IS PROHIBITED\n\n"\
    b"   You must have explicit, authorized permission to access or configure this device.\n"\
    b"   Unauthorized attempts and actions to access or use this system may result in civil and/or\n"\
    b"   criminal penalties.\n"\
    b"   All activities performed on this device are logged and monitored.\n\n"\
    b" UNAUTHORIZED ACCESS TO THIS DEVICE IS PROHIBITED\n\n\n&\n")
##### Configure EXEC Banner
    tn.write(
    b"banner exec &\n\n"\
    b"     *****     With Great Power Comes Great Resposibility     *****\n\n&")
##### Configure Default SECURITY
    tn.write(b"service password-encryption\n")
    tn.write(b"enable secret cisco\n")
    tn.write(b"username ccna privilege 15 secret cisco\n")
    tn.write(b"ip domain-lookup\n")
    tn.write(b"ip name-server 192.168.1.1\n")
    tn.write(b"ip http server\n")
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

