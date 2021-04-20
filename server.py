import socket

messages = []
users = []


def handle_client(client):
    message = (client.recv(1024)).decode()
    print(message)
    handle_client_message(client, message)


def handle_client_message(client, message):
    global messages
    global users
    message_params = message.split("/")
    if message_params[0] == "join":
        users.append(message_params[1])
        server_response = "You joined successfully!"
    elif message_params[0] == "send":
        messages.append(message_params[1] + " > " + message_params[2])
        server_response = "Message sent."
    elif message_params[0] == "users":
        server_response = " ".join(users)
    elif message_params[0] == "refresh":
        server_response = "\n".join(messages)
    else:
        server_response = "INVALID INSTRUCTION."
    client.send(server_response.encode())


if __name__ == '__main__':
    server_socket = socket.socket()
    print("Socket created successfully.")
    server_socket.bind(('127.0.0.1', 12345))
    print("Binding done.")
    print("Listening...")
    server_socket.listen(1)
    while True:
        client_socket, address = server_socket.accept()
        print("Client " + address[0] + " connected successfully.")
        handle_client(client_socket)
