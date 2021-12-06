# first of all import the socket library
import socket
import random

# next create a socket object
s = socket.socket()

# reserve a port on your computer
# in our case it is 12345 but it can be anything
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))

print("socket bound to " + str(port))

# a forever loop until we interrupt it or
# an error occurs
while True:

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # Establish connection with client.
    connection, address = s.accept()
    print('Got connection from', address)

    # receive encoded data from client and decode it
    data = connection.recv(1024)
    data_decoded = data.decode()

    print("Message: " + data_decoded)

    # generate one-time password (otp)
    otp = random.randint(1000, 9999)
    print(f"OTP = {otp}")

    # receive otp from the client
    received_otp = int(connection.recv(1024).decode())

    # verify that generated otp is same as received otp from client
    if received_otp == otp:
        connection.send('Access granted'.encode())
    else:
        connection.send('Access denied'.encode())

    # Close the connection with the client
    connection.close()

    # break the loop (i.e terminate the server) if the message sent is exit
    if data_decoded == "exit":
        break

