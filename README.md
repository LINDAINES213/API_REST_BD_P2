# Proyecto 2 Bases de Datos 1

## 💻 Creando una aplicación web para la visualización y manejo de bases de datos

Para este proyecto se realizo una aplicación web utilizando Python y Flask con algunas de sus extensiones y HTML y CSS para la construcción de las páginas a mostrar en la web para la visualizacion y manejo de bases de datos en PostgreSQL. <br><br>
Video de como funciona la aplicacion: https://drive.google.com/file/d/1b461yfjPNCawR5vm8zQ08teqe9ZNMOJe/view?usp=sharing

## 👩‍💻 Proceso para correr la aplicación desde tu dispositivo

`Entorno Virtual`: Primero debe asegurarse de tener Python instalado en su computadora. Teniendolo ya instalado en un cmd se debe correr el siguiente comando:
```bash
pip install virtualenv
```
Si deseas confirmar que este se installo correctamente corre el comando a continuación y te debería de mostrar `virtualenv==20.21.0` en la lista. (La version dependera de la fecha en que lo hayas instalado).
```bash
pip freeze
```
`Clonar el repositorio`: Luego de tener ya el entorno virtual instalado puedes proceder a clonar el repositorio con el siguiente comando:
```bash
git clone https://github.com/LINDAINES213/API_REST_BD_P2.git
``` 
`Configurar Base de Datos`: Dentro del repositorio se encuentra el archivo `proyecto2.dump` el cual debes subir como un restore en una base de datos creada en pgAdmin. Luego en el archivo .env, incluido tambien en el repositorio, debes de cambiar los datos que sean necesarions, como la contraseña, nombre de la base de datos que le colocaste en pgAdmin, usuario, etc. El secret key se debe dejar tal y como esta.
```bash
SECRET_KEY = PROYECTO2_BD
PGSQL_HOST = localhost
PGSQL_USER = postgres
PGSQL_PASSWORD = TU_CONTRASEÑA
PGSQL_DATABASE = NOMBRE_BASE_DE_DATOS
```
Igualmente el el archivo `config.py` se debe de cambiar estos datos:
```bash
class Config:
    SECRET_KEY = 'PROYECTO2_BD'

class DevelopmentConfig(Config):
    DEBUG = True
    PGSQL_HOST = 'localhost'
    PGSQL_USER = 'postgres'
    PGSQL_PASSWORD = 'TU_CONTRASEÑA'
    PGSQL_DATABASE = 'NOMBRE_BASE_DE_DATOS'

config = {
    'development': DevelopmentConfig
}
```
`Creando el entorno virtual`: Dentro de la carpeta del proyecto, puede ser dentro de la terminal de Visual Studio Code o desde el cmd de su computadora, escriba el siguiente comando para crear el entorno virtual que va a utilizar para correr el programa:
```bash
virtualenv venv 
```
`Corriendo el programa`: Al tener la base de datos ya configurada con la API correctamente deberria de dejar que se pueda correr, por lo que en Visual Studio Code se abre el proyecto y se abre una nueva terminal, de preferencia que sea de tipo Command Prompt y correr los siquientes comandos:
```bash
.\venv\Scripts\activate #Para activar el entorno virtual
```
```bash
python .\src\app.py #Para correr la API
```
Con esto la terminal deberia de mostrarse asi <br><br>
![image_2023-05-16_150245050](https://github.com/LINDAINES213/API_REST_BD_P2/assets/77686175/811acd93-475e-494a-a4aa-467bbfa35058) <br><br>
Donde se muestra el link donde se esta corriendo la aplicacion web y se puede visualizar, el caso de la fotografia es este
```bash
http://127.0.0.1:5000
```
Con esto ya se deberia de poder correr la aplicacion completa, en caso de no querer crear un usuario puede utilizar este para tener acceso a todas las funcionalidades de la aplicacion: 
```bash
Correo: lijv1333@gmail.com
Contraseña: ines13
Tipo de usuario: admin
```

En caso de no correr correctamente verificar que los pasos anteriores se realizaron correctamente.
