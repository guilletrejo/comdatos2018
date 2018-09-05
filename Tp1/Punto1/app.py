from flask import Flask, request


app = Flask(__name__)

ip = "192.168.0.27"
puerto = 5001

#Metodo GET simple

@app.route("/")
def index():
    return "Bienvenidos al practico 1\n"

#Metodo GET con parametro

@app.route("/autenticacion")
def aut():
    user1=request.args.get("user")
    return user1 + "\n"

#Metodo POST

@app.route("/suma",methods=["GET","POST"])
def sum():
     num1=request.form.get("num1")
     num2=request.form.get("num2")
     return "El resultado de la suma es {}\n".format(str(int(num1)+int(num2)))

app.run(ip,puerto)
