from flask import Flask, render_template,abort,request
app = Flask(__name__)   


@app.route('/',methods=["GET","POST"])
def inicio():
    return render_template("inicio.html")

#@app.route('/multiplicar',methods=["POST"])
#def suma():
#    numero = request.form.get("numero")
 #   try:
#        numero = int(numero)
#    except:
#        abort(404)
#    return render_template("multiplicacion.html", numero=numero)    

app.run(debug=True)
