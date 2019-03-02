#!/usr/bin/env python3

##06_NTP.py


import getpass
import telnetlib

user = input("Enter your remote account: ")
password = getpass.getpass()
Routers = open("Routers.txt")
Switches = open("Switches.txt")

for file in (Routers, Switches):
    print(file.name)
    for line in file:
        HOST = line.strip()
        tn = telnetlib.Telnet(HOST)
        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
##### Check NTP configuration
        tn.write(b"show ntp associations\n")
        tn.write(b"show ntp config\n") if (file == Routers) else None
        tn.write(b"show ntp information\n")
        tn.write(b"show ntp packets\n")
        tn.write(b"show ntp status\n")
##### Configure NTP
        tn.write(b"configure terminal\n")
        if HOST == "10.0.0.1":
            tn.write(b"clock timezone EST -5\n")
            tn.write(b"clock summer-time DST recurring\n")
            tn.write(b"ip domain-lookup\n")
            tn.write(b"ntp server 0.pool.ntp.org\n")
            tn.write(b"ntp server 1.pool.ntp.org\n")
            tn.write(b"ntp server 2.pool.ntp.org\n")
            tn.write(b"ntp server 3.pool.ntp.org\n")
            tn.write(b"ntp master\n")
        else:
            tn.write(b"ntp server 1.0.0.1\n")
            tn.write(b"clock timezone EST -5\n")
            tn.write(b"clock summer-time DST recurring\n")
##### EXIT, WRITE MEMORY, and LOGOUT
        tn.write(b"exit\n")
        tn.write(b"exit\n")
        tn.write(b"cop r s\n")
        tn.write(b"\n")
        tn.write(b"exit\n")
        print("\n*** START ***")
        print("****"+ line + "\n")
        print(tn.read_all().decode('ascii'))
        print("*** COMPLETE ***")
        print("****"+ line + "\n")
