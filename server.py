import socket
import threading

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 9000
ADDRESS = "0.0.0.0"
my_socket.bind((ADDRESS, PORT))

broadcast_list = []


def accept_loop():
    while True:
        my_socket.listen()
        client, client_address = my_socket.accept()
        broadcast_list.append(client)
        start_listening_thread(client)


def start_listening_thread(client):
    client_thread = threading.Thread(target=listen_thread, args=(client,))
    client_thread.start()


def listen_thread(client):
    while True:
        message = client.recv(1024).decode()
        print(f"{message}")
        broadcast(message)


def broadcast(message):
    for client in broadcast_list:
        client.send(message.encode())


accept_loop()
