'''
   Socket server UDP
'''

import socket

UDP_IP= "192.168.0.27"
UDP_PORT= 5006

#Creación del Socket,AF_INET socket de internet(IPv4),SOCK_DGRAM orientado a protocolo UDP
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
                                                              
#Enlazo el socket a una direccion IP y un puerto(donde estará "escuchando")                                                             
client_socket.bind((UDP_IP,UDP_PORT))

while True:
#Obtenemos la direccion y el puerto desde la que se hace la petición
    data, addr = client_socket.recvfrom(4096) #Tamaño del buffer 4096
    print ("received message: ", data.decode())