import socket
import io
import threading

connected = False

message = ""

client_socket_var = ""

def connect_client(ip, port):
    global connected, client_socket

    client_socket = socket.socket(family= socket.AF_INET, type = socket.SOCK_STREAM)



    client_socket.connect((f"{ip}", port))

    client_socket_var = client_socket

    print("server connected")

    def getting_message():
        global message
        while True:
            data = client_socket.recv(1024).decode()
            print(data)
            message += "connected"
            return data
    threading.Thread(target = getting_message).start()
    
    connected = True

    