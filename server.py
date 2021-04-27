import socket

messages = []


def handle_client(client):
    message = (client.recv(1024)).decode()
    print(message)
    server_response = get_server_response(message)
    client.send(server_response.encode())


def get_server_response(message):
    global messages
    message_params = message.split("/")
    if message_params[0] == "send":
        messages.append(message_params[1] + " > " + message_params[2])
        server_response = "Message sent."
    elif message_params[0] == "refresh":
        server_response = "\n".join(messages)
    else:
        server_response = "INVALID INSTRUCTION."
    return server_response


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
