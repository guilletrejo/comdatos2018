from ftplib import FTP

ftp = FTP() #Creacion del objeto FTP

ftp.connect('192.168.0.22',1026)    #Conexion al servidor FTP
ftp.login("user","12345")                         #Se logea al servidor de forma anonima
ftp.cwd('/Downloads') #SubPath del servidor, el servidor define el path raiz
ftp.retrlines('LIST')               #Lista de objetos de ese path raiz

def downloadFile():
 filename = input("Elija el archivo a descargar:") #Seleccion del archivo a descargar
 localfile = open(filename, 'wb')                  #Creacion del archivo en el cliente
 ftp.retrbinary('RETR ' + filename, localfile.write, 8192)
 ftp.quit()
 localfile.close()

downloadFile()