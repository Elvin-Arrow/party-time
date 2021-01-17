import socket, time
from properties import Properties, ClientConnectionProperties
from threading import Thread
# Constants
kConnectionProperties = Properties()

# Globals
clients = []
threads = []
serverSocket = None

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

    print('Accepting connections...')

    try:    
        clientConnection, clientAddress = serverSocket.accept()

        # Store the new connection
        client = ClientConnectionProperties(clientConnection=clientConnection, clientAddress=clientAddress)
        clients.append(client)

        # Display the address of the newly connected client
        print("{} just connected".format(client.clientAddress[0]))

        # Serve connection
        createThread(client.clientConnection)

    except:
        print('Error')

def fireUpSocket():
    global serverSocket

    # Create socket
    createSocket()

    # Bind socket
    bindSocket()

    # Accept connection
    acceptConnections()

####################################### Thread 2 #######################################
def ping_clients():
    

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
        time.sleep(5)

# Serve Connections
####################################### Thread 3+ #######################################
def serve(conn):
    while True:
        try:
            data = conn.recv(1024)
            print(data.decode())

            response = 'Hey just received a message from you saying: {}'.format(data.decode())

            conn.sendall(response.encode())
        except:
            print('Connection closed by client')

def createThread(conn):
    thread = Thread(target=lambda : serve(conn))
    threads.append(thread)
    thread.daemon = True
    thread.start()


connectionThread = Thread(target=fireUpSocket)