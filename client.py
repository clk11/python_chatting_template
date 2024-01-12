import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("mothership ip", 5050))

while True:
    inp = input("Introduce the message to send : ")
    if inp == "q":
        break
    client_socket.send(inp.encode('utf-8'))
