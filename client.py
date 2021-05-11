import socket
import sys

IP = '127.0.0.1'
PORT = 12345
COUNTER = 0


def send_to_server(command):
    server = socket.socket()
    server.connect((IP, PORT))
    server.send(command.encode())
    response = (server.recv(1024)).decode()
    server.close()
    return response


def run_menu(name):
    command = int(input("Choose one of the options:\n" +
                        "1.Send message\n" +
                        "2.Refresh\n" +
                        "3.Users' list\n" +
                        "4.Exit\n"))
    handle_command(command, name)


def handle_command(command, name):
    global COUNTER
    if command == 1:
        message = input("Enter your message:")
        to_send = "send" + "/" + name + "/" + message
        print(send_to_server(to_send))
    elif command == 2:
        to_send = "refresh" + "/" + str(COUNTER)
        response_params = send_to_server(to_send).split("/")
        COUNTER += int(response_params[0])
        print(response_params[1])
    elif command == 3:
        print(send_to_server("users"))
    elif command == 4:
        print("Bye!")
        to_send = "exit" + "/" + username
        print(send_to_server(to_send))
        sys.exit(0)
    print()


if __name__ == '__main__':

    username = input("Enter your name:")
    send_to_server("join" + "/" + username)
    print("Welcome " + username + " !")
    while True:
        run_menu(username)
