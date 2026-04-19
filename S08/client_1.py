import socket

PORT = 8081
IP = "127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

client.send(str.encode("HELLO FROM THE CLIENT!!!"))
client.close()
