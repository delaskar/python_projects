import socket

host_ip = socket.gethostbyname(socket.gethostname())

print("La dirección IP del host es: " + host_ip)
