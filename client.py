import socket

IP = '127.0.0.1'
PORT = 12345


if __name__ == '__main__':
    server = socket.socket()
    server.connect((IP, PORT))
    print("Connected to server!")
    message = "My chat-application works!"
    server.send(message.encode())
    response = server.recv(1024).decode()
    print(response)
    server.close()