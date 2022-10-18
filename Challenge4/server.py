#Importing modules
import threading #For multiple conversations simultaneously
import socket 

#Initialising the server
PORT = 8080 #Port to listen on
SERVER = "localhost"  #Server IP (To run on local machine, use "localhost")
ADDR = (SERVER, PORT) #Define the address and format
FORMAT = "utf-8" #Format of the message
DISCONNECT_MESSAGE = "!Disconnect" #Message to disconnect

#Creating the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creating a socket object of IPv4 and TCP
server.bind(ADDR) #Bind the server to the IP address and port

# Define the set of clients and the lock for the set
clients = set() #Set of clients
clients_lock = threading.Lock() #Allows multiple threads to run simultaneously by preventing blockage or use of one thread for other system processes


def handle_client(conn, addr):
    '''Function to handle the client'''
    print(f"[NEW CONNECTION] {addr} Connected") #Prints the address of the client that connected

    try:
        connected = True
        while connected:
            msg = conn.recv(1024).decode(FORMAT) #Receives the message (Max size limit is 1024 bytes) from the client and decodes it
            if not msg: #If the message is empty, break the loop
                break

            if msg == DISCONNECT_MESSAGE: #If the message is the disconnect message, break the loop
                connected = False

            print(f"[{addr}] {msg}")
            with clients_lock:
                for c in clients:
                    c.sendall(f"[{addr}] {msg}".encode(FORMAT))

    finally:
        with clients_lock:
            clients.remove(conn)

        conn.close()


def start():
    '''Function to start the server'''
    print('[SERVER STARTED]!')
    server.listen() # Start listening for connections from incoming clients
    while True:
        conn, addr = server.accept() # Accept the connection from the client
        with clients_lock:
            clients.add(conn) # Add the client to the set of clients
        thread = threading.Thread(target=handle_client, args=(conn, addr)) #Creating a thread for each client
        thread.start() #Starts the thread


start()