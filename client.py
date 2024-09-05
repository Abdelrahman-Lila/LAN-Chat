import socket
import threading

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 9000
ADDRESS = "localhost"
my_socket.connect((ADDRESS, PORT))


def thread_sending():
    while True:
        message_to_send = input("Enter your message: ")
        my_socket.send(message_to_send.encode())


def thread_receiving():
    while True:
        message = my_socket.recv(1024)
        print(message.decode())


thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)

thread_send.start()
thread_receive.start()
