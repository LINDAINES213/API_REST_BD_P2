from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from database.db import get_connection
from datetime import datetime, timedelta

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

# LOG IN
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
                elif logged_user.tipo == "bodega":
                    return redirect(url_for('iniciobodega'))
            else:
                flash("Invalid password...")
                return render_template('auth/index.html')
        else:
            flash("Contrasena o usuario incorrectos...")
            return render_template('auth/index.html')
    else:
        return render_template('auth/index.html')
    
#SIGN IN
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
    
#INICIOS
    
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

#FUNCIONES MENU

@app.route('/medicamentos')
@login_required
def medicamentos():
    return render_template('medicamentos.html')

@app.route('/medicamentos2')
@login_required
def medicamentos2():
    return render_template('medicamentos2.html')

@app.route('/anadirmedicamentos')
@login_required
def anadirmedicamentos():
    return render_template('anadirmedicamento.html')

#CREACION

@app.route('/anadirmedicamentos2', methods=['POST'])
@login_required
def anadirmedicamentos2():
    try:
        id = request.form['id']
        nombre = request.form['nombre']
        fecha_vencimiento = request.form['fecha_vencimiento']
        cantidad_actual = request.form['cantidad_actual']
        cantidad_necesaria = request.form['cantidad_necesaria']
        hospital = request.form['hospital']

        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO medicamentos VALUES (%s, %s, %s, %s, %s, %s)""", 
                           (id, nombre, fecha_vencimiento, cantidad_actual, cantidad_necesaria, hospital))
            connection.commit()                
        cursor.close()
        return render_template('confirmaciones.html',)
    
    except Exception as ex:
        return render_template('medicamentos.html')
    
@app.route('/editarmedicamento')
@login_required
def editarmedicamento():
    return render_template('editarmedicamento.html')

#EDICION

@app.route('/editarmedicamento2', methods=['POST'])
@login_required
def editarmedicamento2():
    try:
        id = request.form['id']
        nombre = request.form['nombre']
        fecha_vencimiento = request.form['fecha_vencimiento']
        cantidad_actual = request.form['cantidad_actual']
        cantidad_necesaria = request.form['cantidad_necesaria']
        hospital = request.form['hospital']

        with connection.cursor() as cursor:
                cursor.execute("""UPDATE medicamentos SET id = %s, nombre = %s, fecha_vencimiento = %s, cantidad_actual = %s, cantidad_necesaria = %s, hospital = %s
                                WHERE id = %s""", (id, nombre, fecha_vencimiento, cantidad_actual, cantidad_necesaria, hospital, id))
                connection.commit()
        cursor.close()
        return render_template('confirmaciones2.html',)

    except Exception as ex:
        return render_template('editarmedicamento.html')


#SOLICITUD DEL MES PARA BUSCAR
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

@app.route('/expediente')
@login_required
def expediente():
    return render_template('expediente.html')

#SOLICITUD DEL DPI PARA BUSCAR E IMPRIME BUSQUEDAS
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
    
@app.route('/crearexpediente')
@login_required
def crearexpediente():
    return render_template('crearexpediente.html')

#CREACION

@app.route('/crearexpediente2', methods=['POST'])
@login_required
def crearexpediente2():
    try:
        id_paciente = request.form['id_paciente']
        dpi = request.form['dpi']
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        imc = request.form['imc']
        altura = request.form['altura']
        peso = request.form['peso']
        adiccion = request.form['adiccion']
        enfermedades_hereditarias = request.form['enfermedades_hereditarias']
        tratamientos = request.form['tratamientos']
        medico_asignado = request.form['medico_asignado']
        hospital_asignado = request.form['hospital_asignado']
        enfermedades = request.form['enfermedades']
        evolucion_enfermedad = request.form['evolucion_enfermedad']
        fecha_ingreso = request.form['fecha_ingreso']
        fecha_salida = request.form['fecha_salida']
        hora_atencion = request.form['hora_atencion']
        

        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO pacientes VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                           (id_paciente, dpi, nombre, telefono, direccion, imc, altura, peso, adiccion, enfermedades_hereditarias, tratamientos, medico_asignado, hospital_asignado, enfermedades, evolucion_enfermedad, fecha_ingreso, fecha_salida, hora_atencion))
            connection.commit()                
        cursor.close()
        return render_template('confirmaciones.html',)
    
    except Exception as ex:
        return render_template('crearexpediente.html')

@app.route('/editarexpediente')
@login_required
def editarexpediente():
    return render_template('editarexpediente.html')

#EDICION

@app.route('/editarexpediente2', methods=['POST'])
@login_required
def editarexpediente2():
    try:
        id_paciente = request.form['id_paciente']
        dpi = request.form['dpi']
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        imc = request.form['imc']
        altura = request.form['altura']
        peso = request.form['peso']
        adiccion = request.form['adiccion']
        enfermedades_hereditarias = request.form['enfermedades_hereditarias']
        tratamientos = request.form['tratamientos']
        medico_asignado = request.form['medico_asignado']
        hospital_asignado = request.form['hospital_asignado']
        enfermedades = request.form['enfermedades']
        evolucion_enfermedad = request.form['evolucion_enfermedad']
        fecha_ingreso = request.form['fecha_ingreso']
        fecha_salida = request.form['fecha_salida']
        hora_atencion = request.form['hora_atencion']

        with connection.cursor() as cursor:
                cursor.execute("""UPDATE pacientes SET id_paciente = %s, dpi = %s, nombre = %s, telefono = %s, direccion = %s,
                                imc = %s, altura = %s, peso = %s, adiccion = %s, enfermedades_hereditarias = %s, tratamientos = %s, 
                                medico_asignado = %s, hospital_asignado = %s, enfermedades = %s, evolucion_enfermedad = %s, 
                                fecha_ingreso = %s, fecha_salida = %s, hora_atencion = %s
                                WHERE id_paciente = %s""", (id_paciente, dpi, nombre, telefono, direccion, imc, altura, peso, adiccion, enfermedades_hereditarias, tratamientos, medico_asignado, hospital_asignado, enfermedades, evolucion_enfermedad, fecha_ingreso, fecha_salida, hora_atencion, id_paciente))
                connection.commit()
        cursor.close()
        return render_template('confirmaciones2.html',)

    except Exception as ex:
        return render_template('editarmedicamento.html')


#MUESTRA LA BITACORA DE CAMBIOS
@app.route('/bitacora')
@login_required
def bitacora():
    with connection.cursor() as cursor:
        cursor.execute("""SELECT * FROM bitacora""")
        rows = cursor.fetchall()
        return render_template('bitacora.html', rows=rows) 
    
# CREACION Y EDICION USUARIOS

@app.route('/usuarios')
@login_required
def usuarios():
    with connection.cursor() as cursor:
        cursor.execute("""SELECT id_medico, dpi, m.nombre, telefono, direccion, num_colegiado, especialidades, hospital, h.nombre, fecha_contratacion, correo, contrasena FROM medicos m
                                LEFT JOIN hospitales h ON m.hospital = h.codigo
                                ORDER BY id_medico""")
        rows = cursor.fetchall()
    return render_template('usuarios.html', rows=rows)

@app.route('/crearusuario')
@login_required
def crearusuario():
    return render_template('crearusuario.html')

#CREACION

@app.route('/usuarios2', methods=['POST'])
@login_required
def usuarios2():
    try:
        id_medico = request.form['id_medico']
        dpi = request.form['dpi']
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        num_colegiado = request.form['num_colegiado']
        especialidades = request.form['especialidades']
        hospital = request.form['hospital']
        fecha_contratacion = request.form['fecha_contratacion']
        correo = request.form['correo']
        contrasena = request.form['contrasena']

        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO medicos VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                           (id_medico, dpi, nombre, telefono, direccion, num_colegiado, especialidades, hospital, fecha_contratacion, correo, contrasena))
            connection.commit()                
        cursor.close()
        return render_template('confirmaciones.html',)

    except Exception as ex:
        return render_template('usuarios.html')

@app.route('/editarusuario')
@login_required
def editarusuario():
    return render_template('editarusuario.html')

#EDICION

@app.route('/usuarios3', methods=['POST'])
@login_required
def usuarios3():
    try:
        id_medico = request.form['id_medico']
        dpi = request.form['dpi']
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        num_colegiado = request.form['num_colegiado']
        especialidades = request.form['especialidades']
        hospital = request.form['hospital']
        fecha_contratacion = request.form['fecha_contratacion']
        correo = request.form['correo']
        contrasena = request.form['contrasena']

        with connection.cursor() as cursor:
                cursor.execute("""UPDATE medicos SET id_medico = %s, dpi = %s, nombre = %s, telefono = %s, direccion = %s, num_colegiado = %s, especialidades = %s, hospital = %s, fecha_contratacion = %s, correo = %s, contrasena = %s
                                WHERE id_medico = %s""", (id_medico, dpi, nombre, telefono, direccion, num_colegiado, especialidades, hospital, fecha_contratacion, correo, contrasena, id_medico))
                connection.commit()
        cursor.close()
        return render_template('confirmaciones2.html',)

    except Exception as ex:
        return render_template('usuarios.html')



@app.route('/traslados')
@login_required
def traslados():
    return render_template('traslados.html')

#MUESTRA TRASLADOS
@app.route('/trasladosT')
@login_required
def trasladosT():
    with connection.cursor() as cursor:
        cursor.execute("""SELECT t.idtraslado, t.idmedico, m.nombre,  t.hospital_anterior, h.nombre, t.hospital_nuevo, o.nombre, fecha_traslado FROM traslados t
                        LEFT JOIN medicos m on t.idmedico = m.id_medico
                        LEFT JOIN hospitales h on t.hospital_anterior = h.codigo 
						LEFT JOIN hospitales o on t.hospital_nuevo = o.codigo""")
        rows = cursor.fetchall()
    return render_template('traslados2.html', rows=rows)
    
#PIDE DATOS PARA NUEVOS TRASLADOS
@app.route('/traslados2', methods=['POST'])
@login_required
def traslados2():
    try:

        idtraslado = request.form['idtraslado']
        idmedico = request.form['idmedico']
        hospital_anterior = request.form['hospital_anterior']
        hospital_nuevo = request.form['hospital_nuevo']
        fecha_traslado = request.form['fecha_traslado']

        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO traslados (idtraslado, idmedico, hospital_anterior, hospital_nuevo, fecha_traslado)
                                    VALUES (%s, %s, %s, %s, %s)""", (idtraslado, idmedico, hospital_anterior, hospital_nuevo, fecha_traslado))
            connection.commit()
            with connection.cursor() as cursor:
                cursor.execute("""SELECT t.idtraslado, t.idmedico, m.nombre,  t.hospital_anterior, h.nombre, t.hospital_nuevo, o.nombre, fecha_traslado FROM traslados t
                        LEFT JOIN medicos m on t.idmedico = m.id_medico
                        LEFT JOIN hospitales h on t.hospital_anterior = h.codigo 
						LEFT JOIN hospitales o on t.hospital_nuevo = o.codigo """)
                rows = cursor.fetchall()
            return render_template('traslados2.html', rows=rows)
    except Exception as ex:
        return render_template('traslados.html')
    

@app.route('/reportesadministrativos')
@login_required
def reportesadministrativos():
    return render_template('reportesadministrativos.html')

#MUESTRAN LOS REPORTES QUE SE SOLICITEN
@app.route('/reporte1')
@login_required
def reporte1():
    with connection.cursor() as cursor:
        cursor.execute("""SELECT nombre, tipo, mortalidad, ubicacion_geografica FROM enfermedades
                        ORDER BY mortalidad desc
                        limit 10""")
        rows = cursor.fetchall()
        return render_template('reporte1.html', rows=rows)

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
    
#IDENTIFICA QUE OPCION SE ELIGIO PARA MOSTRAR EL REPORTE
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