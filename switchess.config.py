#!/usr/bin/env python3

#switchess.config.py


print("\n\n*****     Opening File     *****\n\n")

f = open("Switches.txt")
print("Switchess:")

for line in f:
    print("\t\tConfiguring Switch With IP Address: " + line)

f.close()

print("\n\n*****     Closing File     *****\n\n")
