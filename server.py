from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

server_IP = "localhost"
server_port = int(input("Input Port Number: "))

############################
# Code structure below cited from:
# https://realpython.com/python-sockets/
############################

with server as s:
    s.bind((server_IP, server_port))
    s.listen(1)  # listen for 1 connection

    print("Server listening on", server_IP, "on port", server_port)

    conn, addr = s.accept()

    with conn:
        print("Connected by " + str(addr))
        print("Waiting for message from client..")
        conn.sendall(b"Type /q to quit\nEnter message to send..")

        while 1:
            recv = conn.recv(2048)
            if not recv or recv.decode() == "/q":
                break
            print(recv.decode())
            msg = input("> ")
            conn.sendall(str.encode(msg))

print("*** Closing server ***")