from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
#authorizer.add_user("user", "12345", "/home/guilletrejo", perm="elradfmw")
authorizer.add_anonymous("/home/guilletrejo", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("192.168.0.22", 1026), handler)
server.serve_forever()