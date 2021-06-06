from socket import *

client = socket(AF_INET, SOCK_STREAM)

client_IP = "localhost"
client_port = int(input("Input Port Number: "))

############################
# Code structure below cited from:
# https://realpython.com/python-sockets/
############################

with client as c:
    c.connect((client_IP, client_port))
    msg = ""

    while msg != "/q":
        received = c.recv(2048)
        print(received.decode())
        msg = input("> ")
        c.sendall(str.encode(msg))

print("*** Closing client ***")
