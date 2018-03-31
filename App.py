import socket

class Connection(object):

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 1337
    role = None

    def __init__(self):
        #Initiates role as client or server
        
        #TODO - Allow one to set the IP (And port?) on creation, ez 
        
        if self.client_connect():
            self.role = 'Client'
        else:
            self.role = 'Server'
            self.server_setup()

    def client_connect(self):
        # Tries to connect to an established server
        # Returns True if a connection is established
        # Returns False if it couldnt connect    

        try:
            self.socket.connect((self.host, self.port))
            self.socket.send("Yos".encode())

            # TODO - Keep the socket alive and still return the bool
            # Currently returns (I hypothesise that that somehow closes the connection? Either way a broke pipe appears)
            # Might work to run the function on another thread o:
            # Stack overflow is God
            # https://stackoverflow.com/questions/5110911/python-sockets-keep-socket-alive 

            return True
        except Exception:
            #Overwrite socket
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            return False
            

    def server_setup(self):
        #Binds the socket to the chosen IPAddr and Port and listens for a connection 
        print(self.host, self.port)
        self.socket.bind((self.host, self.port))

        self.socket.listen(1) # One connection maximum

        print("Listening")

        (client, addr) = self.socket.accept()

        # TODO - Currently just pauses in a loop, move the socket to another thread to be ran in the background?
        while True:
            data = client.recv(1024).decode()
            print(data)
            r = 'Received'
            client.send(r.encode())

    def send(self, message):
        self.socket.send(message.encode())
        data = ''
        data = self.socket.recv(1024).decode()
        print(data)







class Pong(object):
    # When the connections are setup we can create a lightweight pong game
    # Or even rock paper scissors
    # Just something to showcase the connectivity haha
    def __init__():
        pass

    def setup_connection():
        pass




#Application start point
if __name__ == "__main__":
    c = Connection()