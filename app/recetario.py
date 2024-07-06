from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    title="Inicio"
    return render_template("index.html",title=title)

@app.route("/contacto")
def contacto():
    title="Contacto"
    return render_template("contacto.html",title=title)

@app.route("/recetas")
def recetas():
    title="Recetas"
    return render_template("recetas.html", title=title)

@app.route("/nosotros")
def nosotros():
    title="Nosotros"
    return render_template("nosotros.html", title=title)

#@app.route('/agregar_comentario', methods=['POST'])
#def agregar_comentario():
#    nombre = request.form.get('nombre')
#    comentario = request.form.get('comentario')
#    comentarios.append({'nombre': nombre, 'texto': comentario})
#    return render_template('comentarios.html', comentarios=comentarios)
