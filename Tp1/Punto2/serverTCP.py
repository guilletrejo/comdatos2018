'''
   Socket server TCP
'''
 
import socket
 
TCP_IP= ''  
TCP_PORT = 5003             
BUFFER_SIZE= 4096

#Creación del Socket,AF_INET socket de internet(IPv4),SOCK_STREAM orientado a protocolo TCP
server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                                    
 
#Enlazo el socket a una direccion IP y un puerto(donde estará "escuchando")
server_socket.bind((TCP_IP,TCP_PORT))

#Cantidad de peticiones que maneja en cola el socket
server_socket.listen(1)

#Obtenemos es la direccion y el puerto desde la que se hace la petición
conn, addr = server_socket.accept()

print ("Connection address:", addr)

while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data.decode())
    conn.send(data)  # Echo
conn.close()
