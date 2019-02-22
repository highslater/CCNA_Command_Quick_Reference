#!/usr/bin/env python3

#Routers.config.py


print("\n\n*****     Opening File     *****\n\n")

f = open("Routers.txt")
print("Routers:")

for line in f:
    print("\t\tConfiguring Router With IP Address: " + line)

f.close()

print("\n\n*****     Closing File     *****\n\n")
