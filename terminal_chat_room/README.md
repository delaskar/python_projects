# **Chat Terminal Room**

## **Introduction**
Chat Terminal is a simple chat application that allows clients to connect to a server and communicate with each other. The application consists of two Python files - serve.py and client.py - that handle the server and client logic respectively.

## **Getting Started**
To use the application, you will need to have **Python 3.10** installed on your machine. You can download Python from the official website: https://www.python.org/downloads/

Once you have Python installed, you can clone the Chat Terminal repository from GitHub using the following command:

`git clone https://github.com/<username>/Chat-Terminal.git`

Once you have cloned the repository, you can navigate to the root directory of the project and run the server using the following command:

`python3 server.py`

You should see a message indicating that the server is listening for incoming connections.

Next, open two terminal more window and navigate to the root directory of the project again. Run the client using the following command:

`python3 client.py`

## **Usage**
When you run the client, you will be prompted to enter your name. Once you have entered your name, you can start sending messages to other clients. Messages sent by clients are broadcasted to all other clients that are connected to the server. If what you want is to connect more clients what you should do is open a new terminal and run the file `client.py`
