import tkinter as tk
import socket
import threading
from PIL import Image, ImageTk
from tkinter import DISABLED, VERTICAL, END, NORMAL
from util import ICON_PATH


class ChatClientGUI:
    def __init__(self):
        # Define socket constants
        self.ENCODER = 'utf-8'
        self.BYTESIZE = 1024
        self.client_socket = None

        # Define window
        self.root = tk.Tk()
        self.root.title("Chat Client")
        icon = ImageTk.PhotoImage(Image.open(ICON_PATH))
        self.root.iconphoto(True, icon)
        self.root.geometry("700x700")
        self.root.resizable(0, 0)

        # Define fonts and colors
        self.my_font = ('SimSun', 14)
        self.black = "#010101"
        self.light_green = "#1fc742"
        self.root.config(bg=self.black)

        # Create Frames
        self.info_frame = tk.Frame(self.root, bg=self.black)
        self.output_frame = tk.Frame(self.root, bg=self.black)
        self.input_frame = tk.Frame(self.root, bg=self.black)
        self.info_frame.pack()
        self.output_frame.pack(pady=10)
        self.input_frame.pack()

        # Create widgets
        self.name_label = tk.Label(self.info_frame, text="Client Name:",
                                   font=self.my_font, fg=self.light_green, bg=self.black)
        self.name_entry = tk.Entry(
            self.info_frame, borderwidth=3, font=self.my_font)
        self.ip_label = tk.Label(self.info_frame, text="Host IP:",
                                 font=self.my_font, fg=self.light_green, bg=self.black)
        self.ip_entry = tk.Entry(
            self.info_frame, borderwidth=3, font=self.my_font)
        self.port_label = tk.Label(
            self.info_frame, text="Port Num:", font=self.my_font, fg=self.light_green, bg=self.black)
        self.port_entry = tk.Entry(
            self.info_frame, borderwidth=3, font=self.my_font, width=10)
        self.connect_button = tk.Button(
            self.info_frame, text="Connect", font=self.my_font, bg=self.light_green, borderwidth=5, command=self.connect)
        self.disconnect_button = tk.Button(self.info_frame, text="Disconnect", font=self.my_font,
                                           bg=self.light_green, borderwidth=5, width=10, state=DISABLED, command=self.disconnect)

        # Grid widgets
        self.name_label.grid(row=0, column=0, padx=2, pady=10)
        self.name_entry.grid(row=0, column=1, padx=2, pady=10)
        self.port_label.grid(row=0, column=2, padx=2, pady=10)
        self.port_entry.grid(row=0, column=3, padx=2, pady=10)
        self.ip_label.grid(row=1, column=0, padx=2, pady=5)
        self.ip_entry.grid(row=1, column=1, padx=2, pady=5)
        self.connect_button.grid(row=1, column=2, padx=4, pady=5)
        self.disconnect_button.grid(row=1, column=3, padx=4, pady=5)

        # Output Frame Layout
        self.my_scrollbar = tk.Scrollbar(self.output_frame, orient=VERTICAL)
        self.my_listbox = tk.Listbox(self.output_frame, height=20, width=55, borderwidth=3, bg=self.black,
                                     fg=self.light_green, font=self.my_font, yscrollcommand=self.my_scrollbar.set)
        self.my_scrollbar.config(command=self.my_listbox.yview)

        self.my_listbox.grid(row=0, column=0)
        self.my_scrollbar.grid(row=0, column=1, sticky="NS")

        # Input Frame Layout
        self.input_entry = tk.Entry(
            self.input_frame, width=45, borderwidth=3, font=self.my_font)
        self.send_button = tk.Button(self.input_frame, text="Send", borderwidth=5, width=10,
                                     font=self.my_font, bg=self.light_green, state=DISABLED, command=self.send_message)
        self.input_entry.grid(row=0, column=0, padx=5, pady=5)
        self.send_button.grid(row=0, column=1, padx=5, pady=5)

    # Define Methods

    def verify_connection(self, name):
        """ Verify that server connection is valid and pass required information """

        # The server will send a NAME flag if a valid connection is made
        flag = self.client_socket.recv(self.BYTESIZE).decode(self.ENCODER)

        if flag == "NAME":
            # The connection was made, send client name and await verification
            self.client_socket.send(name.encode(self.ENCODER))
            message = self.client_socket.recv(
                self.BYTESIZE).decode(self.ENCODER)

            if message:
                # Sever sent verification, connection is valid
                self.my_listbox.insert(0, message)

                # Change button/entry states
                self.connect_button.config(state=DISABLED)
                self.disconnect_button.config(state=NORMAL)
                self.send_button.config(state=NORMAL)

                self.name_entry.config(state=DISABLED)
                self.ip_entry.config(state=DISABLED)
                self.port_entry.config(state=DISABLED)

                # Create a thread to continuosly recieve messages from the server
                recieve_thread = threading.Thread(target=self.recieve_message)
                recieve_thread.start()
            else:
                # No verification message was recieved
                self.my_listbox.insert(
                    0, "Connection not verified. Goodbye...")
                self.client_socket.close()
        else:
            # No name flag was sent, connection was refused
            self.my_listbox.insert(0, "Connection refused. Goodbye...")
            self.client_socket.close()

    def connect(self):
        """ Connect to a server at a given ip/port address """

        # Clear any previous chats
        self.my_listbox.delete(0, END)

        # Get the required connection information
        name = self.name_entry.get()
        ip = self.ip_entry.get()
        port = self.port_entry.get()

        # Only try to make a connection if all three fields are filled in
        if name and ip and port:
            # Condition for connection are met, try for connection
            self.my_listbox.insert(
                0, f"{name} is waiting to connect to {ip} at {port}...")

            # Crate a client socket to connect to the server
            self.client_socket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((ip, int(port)))

            # Verify that the connection is valid
            self.verify_connection(name)
        else:
            # Connections for connection were not met
            self.my_listbox.insert(
                0, "Insufficient information for connection...")

    def disconnect(self):
        """ Disconnect from the server """

        # Close the socket
        self.client_socket.close()

        # Change button / entry states
        self.connect_button.config(state=NORMAL)
        self.disconnect_button.config(state=DISABLED)
        self.send_button.config(state=DISABLED)

        self.name_entry.config(state=NORMAL)
        self.ip_entry.config(state=NORMAL)
        self.port_entry.config(state=NORMAL)

    def send_message(self):
        """ Send a message to the server to be broadcast """

        # Send the message to the server
        message = self.input_entry.get()
        self.client_socket.send(message.encode(self.ENCODER))

        # Clear the input entry
        self.input_entry.delete(0, END)

    def recieve_message(self):
        """ Recieve an incoming message from the server """

        while True:
            try:
                # Recieve an incoming message from the server
                message = self.client_socket.recv(
                    self.BYTESIZE).decode(self.ENCODER)
                self.my_listbox.insert(0, message)
            except:
                # An error occured, disonnect from the server
                self.my_listbox.insert(0, "Closing the connection. Goodbye...")
                self.disconnect()
                break

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    chat_client_gui = ChatClientGUI()
    chat_client_gui.run()
