import socket

if __name__ == '__main__':
    server_socket = socket.socket()
    print("Socket created successfully.")
    server_socket.bind(('127.0.0.1', 12345))
    print("Binding done.")
    print("Listening...")
    server_socket.listen()
    while True:
        client_socket, address = server_socket.accept()
        print("Client " + address[0] + " connected successfully.")
        message = (client_socket.recv(1024)).decode()
        print(message, end="\n\n")
        response = input("Enter your message:")
        client_socket.send(response.encode())
        print("Your message is sent.")
