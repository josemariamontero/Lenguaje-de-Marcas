from flask import Flask, render_template,abort,request
app = Flask(__name__)	


@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio2.html")

@app.route('/respuesta',methods=["POST"])
def respuesta():
    nombre=request.form.get("nombre")
    nota = request.form.get("nota")
    nota = int(nota)
    return render_template("resultado.html", nombre=nombre, nota=nota)	

app.run(debug=True)