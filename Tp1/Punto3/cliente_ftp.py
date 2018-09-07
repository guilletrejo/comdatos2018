from ftplib import FTP

ftp = FTP() #Creacion del objeto FTP

<<<<<<< HEAD
ftp.connect('192.168.0.22',1026)    #Conexion al servidor FTP
ftp.login()                         #Se logea al servidor de forma anonima
ftp.cwd('/Downloads') #SubPath del servidor, el servidor define el path raiz
ftp.retrlines('LIST')               #Lista de objetos de ese path raiz
=======
ftp.connect('192.168.0.22',1026)
ftp.login()
ftp.cwd('/Facu/Comunicaciones_de_Datos/comdatos2018/Tp1/Punto3') #replace with your directory
ftp.retrlines('LIST')
>>>>>>> a91b50ca274d85ad5b76d13c4e0affab1d56ae61

def downloadFile():
 filename = input("Elija el archivo a descargar:") #Seleccion del archivo a descargar
 localfile = open(filename, 'wb')                  #Creacion del archivo en el cliente
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

downloadFile()