import socket, threading


# Define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESYZE = 1024


# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))


def send_message():
    """ Send message to the server to be broadcast """
    while True:
        message = input("")
        client_socket.send(message.encode(ENCODER))


def recieve_message_from_server():
    """ Recieve an incoming message from the server """

    while True:
        try:
            # Receive an incoming messsage from the server
            message = client_socket.recv(BYTESYZE).decode(ENCODER)

            # Check for the name flag, else show the message
            if message == "NAME":
                name = input("What is your name?: ")
                client_socket.send(name.encode(ENCODER))
            else:
                print(message)
        except:
            # An error acurred, close the connection
            print("An error ocurred...")
            client_socket.close()
            break


# Create threads to continuosly send and receive message
receive_thread =threading.Thread(target=recieve_message_from_server)
send_thread = threading.Thread(target=send_message)

# Start the client 
receive_thread.start()
send_thread.start()
