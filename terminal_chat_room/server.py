import socket
import threading


# Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESYZE = 1024

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# Create two blank lists to store connected client sockects and their names
client_socket_list = []
client_name_list = []


def broadcast_message(message):
    """ Send a message to ALL clients connected to server """
    for client_socket in client_socket_list:
        client_socket.send(message)


def recieve_message_from_client(client_socket):
    """ Recieve an incoming message from a specific client and forward the message to be broadcast"""
    while True:
        try:
            # Get the name of the given client
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            # Receive message from the client
            message = client_socket.recv(BYTESYZE).decode(ENCODER)
            message = f"\033[1;92m\t{name}: {message}\033[0m".encode(ENCODER)
            broadcast_message(message)
        except:
            # Find the  index of the client socket in our list
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            # Remove the client socket and name from list
            client_socket_list.remove(client_socket)
            client_name_list.remove(name)

            # Close the client socket
            client_socket.close()

            # Broadcast that the client has left the chat
            broadcast_message(f"\033[5;91m\t{name} has a left the chat!\033[0m".encode(ENCODER))
            break


def connect_client():
    """ Connect an incoming client to the server """

    while True:
        # Accept any incoming client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected with {client_address}...")

        # Sed a name flag to prompt the client for ther name
        client_socket.send("NAME".encode(ENCODER))
        client_name = client_socket.recv(BYTESYZE).decode(ENCODER)

        # Add new client socket and client name to appropriate lists
        client_socket_list.append(client_socket)
        client_name_list.append(client_name)

        # Update the server, individual client, and ALL clients
        print(f"Name of new client is {client_name}\n")  # Server
        client_socket.send(f"{client_name}, you have connect to the server!".encode(
            ENCODER))  # Individual client
        broadcast_message(
            f"{client_name} has joined the chat!".encode(ENCODER))

        # Now that a new client has connected, start a thread
        receive_thread = threading.Thread(target=recieve_message_from_client, args=(client_socket,))
        receive_thread.start()


if __name__ == "__main__":
    # Start the server
    print("Server is listening for incoming connections...\n")
    connect_client()
