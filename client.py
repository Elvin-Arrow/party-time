import socket
from properties import Properties

# Contants
connectionProperties = Properties()

# Create a socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect via socket
try: 
    clientSocket.connect((connectionProperties.HOST, connectionProperties.PORT))

    flag = True
    while flag:
        data = input('What to send?\n')
        clientSocket.sendall(data.encode())

        response = clientSocket.recv(1024)

        print('Server just returned: {}'.format(response.decode()))

        flag = False if input('Close connection?\n') == 'y' else ''

    clientSocket.close()
except:
    print('Error connecting...')




