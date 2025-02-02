from flask import Flask, render_template, redirect, request
from comentarios import *

from controller import mostrarcomentario


app = Flask(__name__)
unMenu = [("/", "Inicio"), ("/recetas", "Recetas"), ("/nosotros", "Nosotros"), ("/contacto", "Contacto")]

@app.route("/")
def cargarIndex():
    return render_template("index.html", unMenu=unMenu)

@app.route("/recetas")
def cargarRecetas():
    return render_template("recetas.html", unMenu=unMenu)

@app.route("/nosotros")
def cargarNosotros():
    return render_template("nosotros.html", unMenu=unMenu)

@app.route("/contacto")
def cargarContacto():
    return render_template("contacto.html", unMenu=unMenu)

@app.route("/recetas/maryland")
def receta1():
    return render_template("maryland.html")

@app.route("/recetas/polloperuano")
def receta2():
    return render_template("polloperuano.html")

@app.route("/recetas/chupecamarones")
def receta3():
    return render_template("chupecamarones.html")

@app.route("/recetas/pasticho")
def receta4():
    return render_template("pasticho.html")

@app.route("/comentarios")
def cargarcomentario():
    title="Comentario"
    return render_template("comentarios.html", title=title)
