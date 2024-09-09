import socket
import threading
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 9000
ADDRESS = "0.0.0.0"
BUFFER_SIZE = 1024
server.bind((ADDRESS, PORT))

broadcast_list = []


def accept_loop():
    while True:
        server.listen()
        client, client_address = server.accept()
        broadcast_list.append(client)
        start_listening_thread(client)


def start_listening_thread(client):
    client_thread = threading.Thread(target=listen_thread, args=(client,))
    client_thread.start()


def listen_thread(client):
    while True:
        message = client.recv(1024).decode()
        if message == "send file command":
            file_receiving(client)
        else:
            print(f"{message}")
            broadcast(message)


def file_receiving(client):
    file_name = client.recv(BUFFER_SIZE).decode()
    file_size = int(client.recv(BUFFER_SIZE).decode())

    parent_dir = os.getcwd()
    output_directory = "output"
    output_path = os.path.join(parent_dir, output_directory)
    os.mkdir(output_path)

    output_location = os.path.join(output_path, file_name)

    with open(output_location, "wb") as file:
        bytes_received = 0
        while bytes_received < file_size:
            data = client.recv(BUFFER_SIZE)
            if not data:
                break
            file.write(data)
            bytes_received += len(data)

    print(f"file '{file_name}' received and saved.")


def broadcast(message):
    for client in broadcast_list:
        client.send(message.encode())


if __name__ == "__main__":
    accept_loop()
