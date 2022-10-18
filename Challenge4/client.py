#Importing modules
import socket
import time

#Defining the server to the client
PORT = 5050
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


def connect():
    '''Function to connect to the server'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creating a socket object of IPv4 and TCP
    client.connect(ADDR) #Connect to the server address
    return client #Return a client object


def send(client, msg):
    '''Function to send a message to the server'''
    message = msg.encode(FORMAT) #Encode the message
    client.send(message) #Send the message to the server


def start():
    '''Function to start the client'''
    answer = input('Would you like to connect (yes/no)? ')
    if answer.lower() != 'yes':
        return

    connection = connect() 
    while True:
        msg = input("Message (q for quit): ")

        if msg == 'q':
            break

        send(connection, msg)

    send(connection, DISCONNECT_MESSAGE) #Send the disconnect message to the server
    time.sleep(1)
    print('Disconnected')


start()