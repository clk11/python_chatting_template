import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("mothership ip", 5050))
server_socket.listen(5)

def handle_client(client_socket, addr):
    print(f"{addr} joined the chat !")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        decoded_data = data.decode('utf-8')
        print(f"{addr} says: {decoded_data}")

    print(f"Connection from {addr} closed.")
    client_socket.close()


print("Server is listening for incoming connections.")

while True:
    client_socket, addr = server_socket.accept()
    client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_handler.start()
