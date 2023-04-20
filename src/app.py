from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from database.db import get_connection
from datetime import datetime, timedelta

from config import config

# Models:
from models.ModelUser import ModelUser
from models.MedicamentosModel import MedicamentosModel

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
                if logged_user.tipo == "medico".lower():
                    return redirect(url_for('iniciomedicos'))
                elif logged_user.tipo == "admin".lower():
                    return redirect(url_for('inicioadmin'))
                    #return redirect(url_for('reportesadministrativos'))
                elif logged_user.tipo == "bodega":
                    return redirect(url_for('iniciobodega'))
                #return redirect(url_for('home'))
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
            email = request.form['email']
            password = request.form['password']
            tipo = request.form['tipo']
            username = request.form['username']

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO usuario (email, password, tipo, username)
                                VALUES (%s, %s, %s, %s)""", (email, password, tipo, username))
                connection.commit()
            cursor.close()
            return render_template('auth/index.html')
        else:
            return render_template('auth/signin.html')
        
    except Exception as ex:
        return render_template('auth/signin.html')
    

    
@app.route('/iniciomedicos')
@login_required
def iniciomedicos():
    return render_template('iniciomedicos.html')

@app.route('/inicioadmin')
@login_required
def inicioadmin():
    return render_template('inicioadmin.html')

@app.route('/iniciobodega')
@login_required
def iniciobodega():
    return render_template('iniciobodega.html')

@app.route('/reportesadministrativos')
@login_required
def reportesadministrativos():
    return render_template('reportesadministrativos.html')

@app.route('/medicamentos')
@login_required
def medicamentos():
    return render_template('medicamentos.html')

@app.route('/expediente')
@login_required
def expediente():
    return render_template('expediente.html')

@app.route('/medicamentos2')
@login_required
def medicamentos2():
    return render_template('medicamentos2.html')

@app.route('/busquedam', methods=['GET', 'POST'])
@login_required
def busquedam():
    try:
        if request.method == 'POST':
            fecha_actual = datetime.utcnow().strftime('%Y-%m-%d')
            fecha_vencimiento = datetime.now().date() + timedelta(days=15)
            mes = request.form['mes']
            if not mes:
                error = 'El campo de búsqueda es obligatorio.'
                return render_template('medicamentos.html', error=error)
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT nombre, fecha_vencimiento, cantidad_actual, cantidad_necesaria FROM medicamentos WHERE extract(month from fecha_vencimiento) = %s", (mes,))
                resultados = cursor.fetchall()
            cursor.close()
            return render_template('medicamentos2.html', resultados=resultados, fecha_actual=fecha_actual, fecha_vencimiento=fecha_vencimiento)
            
        else:
            return render_template('medicamentos.html')
    except Exception as ex:
        return render_template('medicamentos.html')
    

@app.route('/busquedaexpedientes', methods=['GET', 'POST'])
@login_required
def busquedaexpedientes():
    try:
        if request.method == 'POST':
            dpi = request.form['dpi']
            if not dpi:
                error = 'El campo de búsqueda es obligatorio.'
                return render_template('expediente.html', error=error)
            
            with connection.cursor() as cursor:
                cursor.execute("""SELECT p.dpi, p.nombre, enfermedades_hereditarias, tratamientos, enfermedades, 
                                evolucion_enfermedad, m.nombre, h.nombre, fecha_ingreso, fecha_salida, hora_atencion 
                                FROM pacientes p
                                LEFT JOIN medicos m on p.medico_asignado = m.id_medico
                                LEFT JOIN hospitales h on p.hospital_asignado = h.codigo
                                WHERE p.dpi = %s""", (dpi,))
                resultados = cursor.fetchall()
            cursor.close()
            return render_template('expediente2.html', resultados=resultados)
            
        else:
            return render_template('expediente.html')
    except Exception as ex:
        return render_template('expediente.html')


@app.route('/reporte2')
@login_required
def reporte2():
    with connection.cursor() as cursor:
        cursor.execute("""SELECT m.nombre, COUNT(p.id_paciente) AS pacientes_atendidos FROM medicos m
                        LEFT JOIN pacientes p on m.id_medico = medico_asignado
                        GROUP BY  m.nombre
                        ORDER BY pacientes_atendidos desc
                        LIMIT 10""")
        rows = cursor.fetchall()
        return render_template('reporte2.html', rows=rows)

@app.route('/reporte1')
@login_required
def reporte1():
    with connection.cursor() as cursor:
        cursor.execute("""SELECT nombre, tipo, mortalidad, ubicacion_geografica FROM enfermedades
                        ORDER BY mortalidad desc
                        limit 10""")
        rows = cursor.fetchall()
        return render_template('reporte1.html', rows=rows)
    
@app.route('/reporte3')
@login_required
def reporte3():
    with connection.cursor() as cursor:
        cursor.execute("""SELECT nombre, imc, altura, peso, count(pacientes.hospital_asignado) as ingresos_hospital FROM pacientes
                        GROUP BY nombre, imc, altura, peso
                        ORDER BY ingresos_hospital DESC
                        LIMIT 5;""")
        rows = cursor.fetchall()
        return render_template('reporte3.html', rows=rows)

@app.route('/reporte4')
@login_required
def reporte4():
    with connection.cursor() as cursor:
        cursor.execute("""SELECT nombre, cantidad_actual, hospital FROM medicamentos
                        WHERE cantidad_actual <= 15;""")
        rows = cursor.fetchall()
        return render_template('reporte4.html', rows=rows)

@app.route('/reporte5')
@login_required
def reporte5():
    with connection.cursor() as cursor:
        cursor.execute("""SELECT h.nombre, COUNT(p.id_paciente) AS pacientes_atendidos FROM hospitales h
                        LEFT JOIN pacientes p on h.codigo = hospital_asignado
                        GROUP BY h.nombre
                        ORDER BY pacientes_atendidos desc
                        LIMIT 3""")
        rows = cursor.fetchall()
        return render_template('reporte5.html', rows=rows)

@app.route('/generarreporte', methods=['POST'])
@login_required
def generarreporte():
    reporte = request.form['reporte']
    if reporte == 'reporte1':
        return redirect('/reporte1')
    elif reporte == 'reporte2':
        return redirect('/reporte2')
    elif reporte == 'reporte3':
        return redirect('/reporte3')
    elif reporte == 'reporte4':
        return redirect('/reporte4')
    elif reporte == 'reporte5':
        return redirect('/reporte5')
    else:
        return redirect('/inicioadmin')



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