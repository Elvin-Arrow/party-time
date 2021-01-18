import socket, time
import threading
from properties import Properties, ClientConnectionProperties
from threading import Thread
# Constants
kConnectionProperties = Properties()

# Globals
clients = []
threads = []
serverSocket = None
pingingInitiated = False
closeProgram = False

#########################################################################################
####################################### Working Area ####################################
#########################################################################################

# Socket creations and initialization
####################################### Thread 1 ####################################
def createSocket():
    global serverSocket

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def  bindSocket():
    global serverSocket

    # Hey remember bind take a tuple
    serverSocket.bind((kConnectionProperties.HOST, kConnectionProperties.PORT))

    # Listen to the socket
    serverSocket.listen(5)

def acceptConnections():
    global serverSocket
    global clients
    global pingingInitiated
    global closeProgram

    print('Accepting connections...')

    try:    
        while not closeProgram:
            clientConnection, clientAddress = serverSocket.accept()

            # Store the new connection
            client = ClientConnectionProperties(clientConnection=clientConnection, clientAddress=clientAddress)
            clients.append(client)

            # Display the address of the newly connected client
            print("{} just connected".format(client.clientAddress[0]))

            # Serve connection
            createConnectionThread(client.clientConnection)

            if not pingingInitiated:
                thread = Thread(target=pingClients())
                threads.append(thread)
                thread.daemon = True
                thread.start()
                pingingInitiated = True

    except:
        print('Error')

def fireUpSocket():
    global serverSocket

    print('Firing up the server')

    # Create socket
    createSocket()

    # Bind socket
    bindSocket()

    # Accept connection
    acceptConnections()

####################################### Thread 2 #######################################
def pingClients():
    

    while True:
        try:
            # Loop through all the clients and check the active ones
            for i, client in enumerate(clients):
                try:
                    # Ping client
                    client.clientConnection.send(str.encode('@'))
                except:
                    # Delete the inactive client from the list
                    del clients[i]                    
                    continue
        except:
            break

        # 30 second interval between pings
        time.sleep(30)

# Serve Connections
####################################### Thread 3+ #######################################
def serve(conn):
    # Get client ID
    clientId = requestID(conn)

    # Let everyone know who joined
    pingAll(clientId)
    
    # Check if the client is ready to start the party
    isClientReady()
    
    while True:
        try:
            # Listen to the client
            data = conn.recv(1024)
            print(data.decode())

            # TODO Check for play / pause

        except:
                print('Connection closed by client')

def requestID(conn):
    message = 'Key in your identifier'

    conn.sendall(message.encode())

    id = conn.recv(1024)
    
    return id.decode()

def pingAll(clientId):
    global clients

    message = f'Hey... {clientId} just joined the party!'

    # Ping all clients
    for client in clients:
        client.clientConnection.sendall(message.encode())

def isClientReady(conn):
    
    while True:
        message = 'Are you ready for the party?'

        conn.sendall(message.encode())

        isReady = conn.recv(1024)

        if isReady.decode():
            break



def createConnectionThread(conn):
    thread = Thread(target=serve, args=(conn))
    threads.append(thread)
    thread.daemon = True
    thread.start()
    


connectionThread = Thread(target=fireUpSocket)
threads.append(connectionThread)

# Start accepting connections
connectionThread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
    