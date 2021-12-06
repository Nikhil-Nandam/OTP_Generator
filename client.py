# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# try to connect to the server on local computer
try:
    s.connect(('127.0.0.1', port))
except ConnectionRefusedError:
    print("Server refused to connect!!")
    exit()

# send an encoded message to the server
data = "exit"   # "Hello Server!"
s.send(data.encode())

# receive data from the server and decoding to get the string.
print(s.recv(1024).decode())

# close the connection
s.close()


