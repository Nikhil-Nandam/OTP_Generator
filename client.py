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

# input the mobile number
print('Enter your mobile number: ')
number = input().strip()

# send an encoded message to the server
data = f"Hello Server! Mobile number is {number}"
s.send(data.encode())

print('Enter OTP received on your mobile: ')

# input the otp
otp = 0
try:
    otp = int(input().strip())
except ValueError:
    print('Enter valid OTP')
    exit()

# send the entered otp to server
s.send(str(otp).encode())

# receive data from the server and decoding to get the string.
print(s.recv(1024).decode())

# close the connection
s.close()


