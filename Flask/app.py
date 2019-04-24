
from flask import Flask, render_template
app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html")

@app.route("/<operador>/<int:numero1>/<int:numero2>",methods=["GET","POST"])
def calculadora(operador,numero1,numero2):
	if operador == "+":
		resultado = numero1 + numero2
	elif operador == "-":
		resultado = numero1 - numero2
	elif operador == "*":
		resultado = numero1 * numero2
	elif operador == "division":
		resultado = numero1 / numero2
	return render_template("numeros.html",operador=operador,numero1=numero1,numero2=numero2,resultado=resultado)

app.run(debug=True)