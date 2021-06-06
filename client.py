from socket import *

client = socket(AF_INET, SOCK_STREAM)

client_IP = "localhost"
client_port = int(input("Input Port Number: "))

with client as c:
    c.connect((client_IP, client_port))
    msg = ""

    while msg != "/q":
        received = c.recv(2048)
        msg = input(">")
        c.sendall(str.encode(msg))



print("Closing client.")
