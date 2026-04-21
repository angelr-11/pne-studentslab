import socket
import termcolor

PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))
ls.listen()

print("The server is configured!")

counter = 0
connections = []

while True:
    print("Waiting for connection...")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        print("The following clients connected to the server:")
        for i,j in enumerate(connections, start=1):
            print(f"Client {i}: {j}")

        exit()
    else:
        counter += 1
        print(f"Connection {counter}. Client IP, PORT: {client_ip_port}")
        connections.append(client_ip_port)

        msg_raw = cs.recv(2048)
        msg = termcolor.colored(msg_raw.decode(), "green")
        print(f"Message received: {msg}")

        response = f"Echo: {msg}"
        cs.send(response.encode())
        cs.close()