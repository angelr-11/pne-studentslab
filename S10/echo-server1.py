import socket
import termcolor

PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))
ls.listen()

print("The server is configured!")

while True:
    print("Waiting for connection...")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        print("A client has connected to the server!")

        msg_raw = cs.recv(2048)
        msg = termcolor.colored(msg_raw.decode(), "green")
        print(f"Message received: {msg}")

        response = f"Echo: {msg}"
        cs.send(response.encode())
        cs.close()
