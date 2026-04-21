import socket
import termcolor

class Client:
    def __init__(self, ip:str, port:int):
        self.IP = ip
        self.PORT = port

    def __str__(self):
        return f'Connection to SERVER at {self.IP}, PORT: {self.PORT}'

    def ping(self):
        print("OK")

    def talk(self, message):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect((self.IP, self.PORT))

        soc.send(str.encode(message))

        response = soc.recv(2048).decode("utf-8")
        soc.close()
        return response

