# **Python Chat Application**
A simple chat application built using Python's socket library. The application allows multiple clients to connect to a central server and exchange messages with each other. The server broadcasts messages from each client to all other clients connected to it.

#

## **Getting started**

### **Prerequisites:**
    Python 3.10

If you ***don't have python installed***, you should go to the official page and download python version 3.10. You can go to the following link to download python from the official page:

- <a href="https://www.python.org/downloads/">**Python Website**</a>

### **Installing**

1. Clone the repository to your local machine
2. Navigate to the project directory using the terminal/command prompt
3. Create a virtual environment with the following command:
    - `python3 -m venv env`

4. Activate the virtual environment with the following command:
    - `source env/bin/activate`

5. Run `pip install -r requirements.txt` to install the required dependencies.

#
**NOTE:** The **socket**, **tkinter**, **threading** libraries come built-in by default in **python**. That is, when you install python on your computer or virtual machine, python installs these libraries automatically.
#

## **Running the application.**

Open two terminal/command prompt windows...

In the first window, navigate to the project directory and run:
- `python run_server.py`

In the second window, navigate to the project directory and run 
- `python run_client.py`

Enter your username and start sending messages.

### **How it works**
The application consists of two scripts: **run_server.py** and **run_client.py**.

***Server script:***
The server script (run_server.py) creates a server socket that listens for incoming client connections. When a client connects, the server prompts them to enter a username. The server then adds the client to a list of connected clients and starts a new thread to listen for incoming messages from that client. When a message is received from a client, the server broadcasts it to all other clients connected to it.

The server script can be found in the ***util*** directory, in a file called ***server.py***.

***Client script:***
The client script (run_client.py) creates a client socket that connects to the server socket. When the client connects, they are prompted to enter a username. The client then starts a new thread to listen for incoming messages from the server. When a message is received from the server, the client displays it in the chat window.

The client script can be found in the **util** directory, in a file called **chat_client_gui.py**.

### **How to find your Host IP**

If you don't know the number of your **Host IP**, you can find out by running this small script in the terminal or just create a python file inside the editor and run the following code:

```
import socket

host_ip = socket.gethostbyname(socket.gethostname())
print("The host IP address is: " + host_ip)
```
### **Default port number**

The default port number used in the application is: **12345**.