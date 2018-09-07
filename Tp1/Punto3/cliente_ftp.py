from ftplib import FTP

ftp = FTP('')

ftp.connect('192.168.0.22',1026)
ftp.login()
ftp.cwd('/Facu/Comunicaciones_de_Datos/comdatos2018/Tp1/Punto3') #replace with your directory
ftp.retrlines('LIST')

def downloadFile():
 filename = 'hola.txt' #replace with your file in the directory ('directory_name')
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

downloadFile()