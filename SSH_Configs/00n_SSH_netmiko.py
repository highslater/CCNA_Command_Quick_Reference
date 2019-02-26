#!/usr/bin/env python3


##00n_SSH_netmiko.py



from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.1',
    'username': 'ccna',
    'password': 'cisco',
}

print("\n\n****** SSH : user = (" + R1['username'] + ")")
print("CONNECTING to >  " + R1['ip'])

net_connect = ConnectHandler(**R1)

print("\t      >   CONNECTED\n")

output_0 = net_connect.send_command('show ip route | i via')
output_1 = net_connect.send_command('show ip interface brief | include up')
output_2 = net_connect.send_command('show run | s eigrp')
output_3 = net_connect.send_command('show run | s ip access-list')

print("\nOUTPUT BEGINS >\n\n")
print(output_0 + "\n\n")
print(output_2 + "\n\n")
print(output_3 + "\n\n")
print(output_1 + "\n")
print("\n< OUTPUT ENDS")
print("\n\n********* SSH : user = (" + R1['username'] + ")")
print("DISCONNECTING from <  " + R1['ip'])
print("\t\t   <   DISCONNECTED\n\n")
