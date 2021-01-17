class Properties:
    def __init__(self, host = '127.0.0.1', port = 12000):
        self.__host = host
        self.__port = port
        
    
    @property
    def HOST(self):
        return self.__host

    @property
    def PORT(self):
        return self.__port

class ClientConnectionProperties:
    __beingServed = False

    def __init__(self, clientConnection, clientAddress):
        self.__clientConnection = clientConnection
        self.__clientAddress = clientAddress

    @property
    def clientConnection(self):
        return self.__clientConnection

    @property
    def clientAddress(self):
        return self.__clientAddress

    @property
    def beingServed(self):
        return self.__beingServed

    def toggleBeingServed(self):
        self.__beingServed = not self.__beingServed

        return self.__beingServed