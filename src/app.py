from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from database.db import get_connection

from config import config

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

app = Flask(__name__)

csrf = CSRFProtect()
connection = get_connection()
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(connection, id)

@app.route('/')
def index():
    return redirect(url_for('signin'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['email'], request.form['password'], request.form['tipo'])
        logged_user = ModelUser.login(connection, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Invalid password...")
                return render_template('auth/index.html')
        else:
            flash("Contrasena o usuario incorrectos...")
            return render_template('auth/index.html')
    else:
        return render_template('auth/index.html')
    
@app.route('/signin', methods=['GET','POST'])
def signin():
    try:
        if request.method == 'POST':
            # Obtenemos los datos del formulario
            email = request.form['email']
            password = request.form['password']
            tipo = request.form['tipo']
            username = request.form['username']

            # Creamos el cursor para realizar la consulta
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO usuario (email, password, tipo, username)
                                VALUES (%s, %s, %s, %s)""", (email, password, tipo, username))
                #affected_rows = cursor.rowcount
                connection.commit()
            cursor.close()
            return render_template('confirmaciones.html')
        else:
            flash("Error en el registro")
            return render_template('auth/signin.html')
    except Exception as ex:
        return render_template('auth/signin.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()