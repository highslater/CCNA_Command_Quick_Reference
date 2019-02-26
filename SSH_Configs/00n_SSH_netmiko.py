#!/usr/bin/env python3


##00n_SSH_netmiko.py



from netmiko import ConnectHandler
import time

file = open('rt_test_list.txt')

for line in file:
    D = eval(line)[1]
    R = eval(line)[0]
    print("\n\n****** SSH : user = (" + D['username'] + ")")
    print("CONNECTING to :  " + R + "  <  at  >  " +  D['ip'])
    net_connect = ConnectHandler(**D)
    print("\t      >   CONNECTED\n")
    output_0 = net_connect.send_command('show ip route | i via')
    output_1 = net_connect.send_command('show ip interface brief | include up')
    output_2 = net_connect.send_command('show run | s eigrp')
    output_3 = net_connect.send_command('show run | s ip access-list')
    print("\nOUTPUT BEGINS >\n\n")
#    print(output_0 + "\n\n")
#    print(output_2 + "\n\n")
#    print(output_3 + "\n\n")
    print(output_1 + "\n")
    print("\n< OUTPUT ENDS")
    print("\n\n********* SSH : user = (" + D['username'] + ")")
    print("DISCONNECTING from :  " + R + "  <  at  >  " + D['ip'])
#    time.sleep(2)
    print("\t\t   <   DISCONNECTED\n\n")
