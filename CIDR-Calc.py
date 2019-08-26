"""
Every once in a while we'll need to calculate a CIDR range, and why not do it in python to make things easier for us
This program takes a CIDR range and displays all the IP addresses in the specified range, in addition it also calculates the sum of all the addresses
This script can be useful in either running nessus scans and you need to specify a range from a file or something

"""
import ipaddress
count = 0 
print("---------------------------------------\n")
print("CIDR Range Calculator\nDisplay all IP addresses from a given CIDR\n")
CIDR = input("Please enter a CIDR range to calculate: \n")
print("Calculating subnet: \n", CIDR)
net = ipaddress.ip_network(CIDR)
for a in net:
        print(a)
        count = count + 1
print("The total of the ranges is: \n",count)
print("\nDone")
