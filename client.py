from email import message_from_binary_file
from socket import *
import os

def clear(): os.system('cls')
serverName ="26.97.210.21"
serverPort = 27000
clientSocket = socket(AF_INET, SOCK_STREAM)
conn = (serverName, serverPort)

clientSocket.connect(conn)
message, serverAddress = clientSocket.recvfrom(1500)
message = message.decode()
ficar = True
while ficar:
    
    if message.startswith('/hear'):
        if '/clear' in message: clear()
        message = ' '.join((message.split(' '))[1:])
        print(message)
        
    elif message.startswith('/say'):
        if '/clear' in message: clear()
        message = ' '.join((message.split(' '))[1:])
        message =input(message)
        clientSocket.send(message.encode())
    
    message, serverAddress = clientSocket.recvfrom(1500)
    message = message.decode()

print(message.decode())
clientSocket.send(message.encode())

clientSocket.close()