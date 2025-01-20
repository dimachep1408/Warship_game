import socket, os
import threading, time, ast, json



data_turn = {}
path_to_json = os.path.abspath(__file__ + "/../../data_s.json")

def start_server(start_server = True):
    global client_socket, position_enemy_ships, data_turn, attack_3x3_position

    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    server_socket.bind(("0.0.0.0", 8080))
    data_turn['turn'] = True
    with open(path_to_json, "w") as f:
        json.dump(data_turn, f, indent = 4)
    attack_3x3_position = None
    if start_server == True:


        server_socket.listen()
        print("Wait for connection...")
        
        client_socket, client_info = server_socket.accept()
        print(client_info)


    elif start_server == False:
        server_socket.sendto("Hello".encode(), ("192.168.0.1", 8040))
    
    def getting_message(): 
        print("work")

        global position_enemy_ships, data_turn, position_shot, flag_send_message, rotation_enemy_ships, closed, attack_3x3_position, aimed_strike_position

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
                elif 'attack_3x3' in data:
                    attack_3x3_position = ast.literal_eval(data.split('/')[-1])
                    print(attack_3x3_position)
                elif 'aimed_strike' in data:
                    aimed_strike_position = list(ast.literal_eval(data.split('/')[-1]))
                    print(aimed_strike_position)
                elif "/" in data:
                    position_shot = ast.literal_eval(data.split("/")[-1])
                    print(position_shot)
                elif "!" in data:
                    closed = True
                elif ":" in data:
                    list_pvo_protect_sends = tuple(data.split(":"))
            except Exception as e: 
                print(f"work - {e}")
                return data
            time.sleep(0.2)
    threading.Thread(target = getting_message).start()

    

    