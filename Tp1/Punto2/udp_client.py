import socket

UDP_IP = '192.168.1.7'
UDP_PORT = 5006

# Crea un socket de internet (AF_INET) ipv4 usando el protocolo UDP (SOCK_DGRAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Pide al usuario que ingrese un mensaje para enviar al server
data = raw_input("Ingrese mensaje a enviar: ")

# Envia el mensaje al servidor
client_socket.sendto(data, (UDP_IP, UDP_PORT))
