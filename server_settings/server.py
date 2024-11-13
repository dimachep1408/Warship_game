import socket
import threading

message = ""

server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)



def start_server(start_server = True):
    global message, server_socket

    if start_server == True:

        server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", 8000))
        server_socket.listen()
    elif start_server == False:
        server_socket.sendto("Hello".encode(), ("192.168.0.1", 8000))
    print("Wait for connection...")
    def getting_message():
        global message
        while True:
            server_socket.listen()
            client_socket, client_info = server_socket.accept()
            data = client_socket.recv(1024).decode()
            print(data)
            print("hello")
            # client_socket.close()
            message += "connected"
            return data
    threading.Thread(target = getting_message).start()

    

    
