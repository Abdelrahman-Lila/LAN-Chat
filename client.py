import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 9000
ADDRESS = "localhost"
my_socket.connect((ADDRESS, PORT))

my_socket.send("The message you want to send".encode())
