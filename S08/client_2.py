import socket

PORT = 8080
IP = "127.0.0.1"

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((IP, PORT))

soc.send(str.encode("HELLO FROM THE CLIENT !!!"))

msg = soc.recv(2048)
print("MESSAGE FROM THE SERVER:\n")
print(msg.decode("utf-8"))

soc.close()