import socket

IP = '127.0.0.1'
PORT = 12345


if __name__ == '__main__':
    server = socket.socket()
    server.connect((IP, PORT))
    print("Connected to server!")
    while True:
        message = input("Enter your message:")
        server.send(message.encode())
        print("Your message is sent.")
        response = server.recv(1024).decode()
        print(response)
