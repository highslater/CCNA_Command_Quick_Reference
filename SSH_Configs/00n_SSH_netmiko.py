#!/usr/bin/env python

##00n_SSH_netmiko.py

import paramiko
import time

ip_address = "10.0.0.1"
username = "ccna"
password = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# THE COMMAND BELOW DOES NOT WORK UNCOMMENT THE LINE BELOW TO GET THIS WORKING.
#ssh_client.connect(hostname=ip_address,username=username,password=password)
ssh_client.connect(hostname=ip_address,username=username,password=password, look_for_keys=False, allow_agent=False)

time.sleep(1)
print("\n\n****** SSH")
print("CONNECTING to >  "), ip_address
time.sleep(2)
print("\t      >   CONNECTED")
remote_connection = ssh_client.invoke_shell()
remote_connection.send("configure terminal\n")
remote_connection.send("no int loop 10\n")
#remote_connection.send("ip address 10.10.10.10 255.255.255.255\n")
remote_connection.send("end\n")
remote_connection.send("wr\n")
time.sleep(1)
print("\n\nOUTPUT BEGINS >")
output = remote_connection.recv(65535)
print("\n" + output)
print("\n\n< OUTPUT ENDS")
print("\n\n********* SSH")
print("DISCONNECTING from <  "), ip_address
time.sleep(2)
print("\t\t   <   DISCONNECTED\n\n")
ssh_client.close
