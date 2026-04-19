class Client:
    def __init__(self, ip:str, port:int):
        self.IP = ip
        self.PORT = port

    def _str_(self):
        return f'Connection to SERVER at {self.IP}, PORT: {self.PORT}'

    def ping(self):
        print("OK")

    def talk(self, message:str):
        return
