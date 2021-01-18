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
        # data = input('What to send?\n')
        # clientSocket.sendall(data.encode())
        
        serverMessage = clientSocket.recv(1024)

        serverMessage = serverMessage.decode()

        if serverMessage == '@':
            continue

        if serverMessage == 'messaged':
            message = clientSocket.recv(1024)
            print(message.decode())
        else:
        # print(serverMessage.decode())
            input(f'{serverMessage}\n')


        # flag = False if input('Close connection?\n') == 'y' else True

    clientSocket.close()
except:
    print('Error connecting...')




