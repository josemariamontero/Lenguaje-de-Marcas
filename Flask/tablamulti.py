from flask import Flask, render_template
app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html")

@app.route("/tabla/<int:numero>/",methods=["GET","POST"])
def tabla(numero):
	numero = int(numero)
	return render_template("inicio.html",numero=numero)


app.run(debug=True)