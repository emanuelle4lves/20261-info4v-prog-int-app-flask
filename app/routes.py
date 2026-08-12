from app import app
from flask import render_template, redirect, flash
from app.forms.login_form import LoginForm
from app.controllers.AuthenticationControllers import AuthenticationController
from app.models import usuario
from app import db


@app.route("/")
def home():
    usuario = {
        "nome": "Leo",
        "produtos": ["Banana", "Abacaxi", "Melancia"]
    }
    esta_logado = True
    return render_template("index.html", 
                           pessoa = usuario, 
                           usuario_logado = esta_logado)

@app.route("/sobre")
def sobre():
    return "Página Sobre"

@app.route("/index2")
def index2():
    return render_template('index2.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        if AuthenticationController.login(formulario):
            flash("Login efetuado com sucesso!")
            return redirect('/')
        else:
            flash("Erro nas credenciais.")
            return redirect('/login')
    return render_template('login.html', title='Login', form=formulario)

@app.route('/dados')
def dados():
    usuario = Usuario (username = 'manualves', email = 'manu@manu.com')
    db.session.add(usuario)
    db.session.commit()

    return