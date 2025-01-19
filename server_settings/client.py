import socket
import io
import threading
import time, ast, json, os

data_turn = {}
path_to_json = os.path.abspath(__file__ + "/../../data_c.json")
connected = False


def connect_client(ip = None, port = None):
    global connected, client_socket, position_enemy_ships, data_turn
    client_socket = socket.socket(family= socket.AF_INET, type = socket.SOCK_STREAM)

    client_socket.connect((ip, port))

    data_turn['turn'] = False
    with open(path_to_json, "w") as f:
        json.dump(data_turn, f, indent = 4)



    print("server connected")

    def getting_message(): 
        print("work")
        global position_enemy_ships, data_turn, position_shot, flag_send_message, rotation_enemy_ships, closed, list_pvo_protect_sends
        while True: 
            try: 
                data = client_socket.recv(1024).decode()
                flag_send_message = True
                print(data) 
                if 'position' in data:
                    position_enemy_ships = ast.literal_eval(data.split('/')[-1])
                    print(type(position_enemy_ships))
                elif 'rotation' in data:
                    rotation_enemy_ships = ast.literal_eval(data.split('/')[-1])
                elif 'turn' in data:
                    data_turn['turn'] = True
                    with open(path_to_json, "w") as f:
                        json.dump(data_turn, f, indent = 4)
                elif "/" in data:
                    position_shot = ast.literal_eval(data.split("/")[-1])
                    print(position_shot)
                elif "!" in data:
                    closed = True
                elif ":" in data:
                    list_pvo_protect_sends = data
            except Exception as e: 
                print(f"work - {e}")
                return data
            time.sleep(1)

    threading.Thread(target = getting_message).start()


    connected = True