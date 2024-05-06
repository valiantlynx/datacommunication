from socket import *

serverPort = 12000

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverSocket.bind(("", serverPort))

"""Why this and line 6 are needed

    An error occurs because the socket is not in listening mode when accept is called.
    Without setting the socket to listen mode, calling accept on it will raise an error because it cannot accept connections.

    note:
        Always call listen() on a TCP socket before calling accept().
        Setting SO_REUSEADDR is optional but useful to avoid address reuse errors   
"""
serverSocket.listen(1)

print("The server is ready to recieve")
while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024)
    modifiedMessage = message.decode().upper()
    connectionSocket.send(modifiedMessage.encode())
    connectionSocket.close()