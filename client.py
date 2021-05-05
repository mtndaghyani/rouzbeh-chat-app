import socket
import sys

IP = '127.0.0.1'
PORT = 12345


def send_to_server(command, *args):
    server = socket.socket()
    server.connect((IP, PORT))
    to_send = command + "/" + "/".join(args)
    server.send(to_send.encode())
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
    if command == 1:
        message = input("Enter your message:")
        print(send_to_server("send", name, message))
    elif command == 2:
        print(send_to_server("refresh"))
    elif command == 3:
        print(send_to_server("users"))
    elif command == 4:
        print("Bye!")
        print(send_to_server("exit", username))
        sys.exit(0)
    print()


if __name__ == '__main__':

    username = input("Enter your name:")
    send_to_server("join", username)
    print("Welcome " + username + " !")
    while True:
        run_menu(username)
