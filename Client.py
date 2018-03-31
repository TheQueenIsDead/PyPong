import socket

#INET STREAMing socket
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 1337

s.connect((host, port))

def send(message):
    s.send(message.encode())
    data = ''
    data = s.recv(1024).decode()
    print(data)
    

while True:
    message = input("Send: ")
    send(message)
