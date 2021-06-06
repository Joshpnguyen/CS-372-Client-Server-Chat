from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

server_IP = "localhost"
server_port = int(input("Input Port Number: "))


with server as s:
    s.bind((server_IP, server_port))
    s.listen(1)  # listen for 1 connection

    print("Server listening on", server_IP, "on port", server_port)

    conn, addr = s.accept()

    with conn:
        print("Connected by " + str(addr))
        print("Waiting for message from client..")
        conn.sendall(b"Type /q to quit")
        conn.sendall(b"Enter message to send..")

        while 1:
            msg = conn.recv(2048)
            if not msg:
                break
            print(msg.decode())
