import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 9000
ADDRESS = "localhost"
my_socket.connect((ADDRESS, PORT))

while True:
    message_to_send = input("Enter your message: ")
    my_socket.send(message_to_send.encode())
