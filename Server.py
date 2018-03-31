import socket, sys

#INET STREAMing socket
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 1337

s.bind((host, port))

s.listen(5)

print("Listening")

(client, addr) = s.accept()


while True:
    data = client.recv(1024).decode()
    print(data)
    r = 'Received'
    client.send(r.encode())
