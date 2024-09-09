import socket
import threading
import tqdm
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 9000
ADDRESS = "localhost"
BUFFER_SIZE = 1024
client.connect((ADDRESS, PORT))

nickname = input("Choose your nickname: ").strip()
while not nickname:
    nickname = input("You entered an invalid nickname: ").strip()

print(
    "-" * 45
    + "\n"
    + 'enter "send file command" if need to send a file'
    + "\n"
    + "-" * 45
)


def thread_sending():
    while True:
        message_to_send = input("")
        if message_to_send != "send file command":
            message_with_nickname = nickname + ": " + message_to_send
            client.send(message_with_nickname.encode())
        else:
            file_sending()


def file_sending():
    file_path = input("Enter the file path to send: ")
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    client.send("send file command".encode())
    client.send(file_name.encode())
    client.send(str(file_size).encode())

    with open(file_path, "rb") as file:
        while True:
            data = file.read(BUFFER_SIZE)
            if not data:
                break
            client.send(data)
    print(f"File '{file_name}' sent successfully")


def thread_receiving():
    while True:
        message = client.recv(1024)
        print(message.decode())


if __name__ == "__main__":
    thread_send = threading.Thread(target=thread_sending)
    thread_receive = threading.Thread(target=thread_receiving)

    thread_send.start()
    thread_receive.start()
