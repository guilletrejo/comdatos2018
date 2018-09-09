import socket

TCP_IP = '192.168.0.27'
TCP_PORT = 5003
BUFFER_SIZE = 4096

# Crea un socket de internet (AF_INET) ipv4 usando el protocolo TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta el cliente indicando la IP y PUERTO del server
client_socket.connect((TCP_IP, TCP_PORT))

while 1:

	# Pide al usuario que ingrese un mensaje para enviar al server
	data = raw_input("Ingrese mensaje a enviar: ")

	# Envia un mensaje al servidor
	client_socket.send(data)

	# Recibe la respuesta del servidor
	data = client_socket.recv(BUFFER_SIZE)

	if data == "exit" : break

	print "Respuesta: \n", data

client_socket.close() 
