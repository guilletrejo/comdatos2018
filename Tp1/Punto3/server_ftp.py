from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


authorizer = DummyAuthorizer() # Crea el objeto que sirve para autorizar (dar permisos...)
authorizer.add_user("user", "12345", "/home/guilletrejo", perm="elradfmw") # Agrega credenciales de un usuario
authorizer.add_anonymous("/home/guilletrejo", perm="elradfmw")  # Permite usuarios anonimos


# Objeto que gestiona el servidor (autorizacion, conexion, max. intentos de login, time out, etc.)
handler = FTPHandler
handler.authorizer = authorizer

# Crea el server y lo deja abierto siempre.
server = FTPServer(("192.168.0.22", 1026), handler)
server.serve_forever()