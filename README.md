# Proyecto 2 Bases de Datos 1

## 💻 Creando una aplicación web para la visualización y manejo de bases de datos

Para este proyecto se realizo una aplicación web utilizando Python y Flask con algunas de sus extensiones y HTML y CSS para la construcción de las páginas a mostrar en la web para la visualizacion y manejo de bases de datos en PostgreSQL.

## 👩‍💻 Proceso para correr la aplicación desde tu dispositivo

`Entorno Virtual`: Primero debe asegurarse de tener Python instalado en su computadora. Teniendolo ya instalado en un cmd se debe correr el siguiente comando:
```bash
pip install virtualenv
```
Si deseas confirmar que este se installo correctamente corre el comando a continuación y te debería de mostrar `virtualenv==20.21.0` en la lista. (La version dependera de la fecha en que lo hayas instalado.
```bash
pip freeze
```
`Clonar el repositorio`: Luego de tener ya el entorno virtual instalado puedes proceder a clonar el repositorio con el siguiente comando:
```bash
git clone https://github.com/LINDAINES213/API_REST_BD_P2.git
``` 
`Configurar Base de Datos`: Dentro del repositorio se encuentra el archivo `proyecto2.dump` el cual debes subir como un restore en una base de datos creada en pgAdmin. Luego en el archivo .env, incluido tambien en el repositorio, debes de cambiar los datos que sean necesarions, como la contraseña, nombre de la base de datos, usuario, etc. El secret key se debe dejar tal y como esta.
```bash
SECRET_KEY = PROYECTO2_BD
PGSQL_HOST = localhost
PGSQL_USER = postgres
PGSQL_PASSWORD = TU_CONTRASEÑA
PGSQL_DATABASE = NOMBRE_BASE_DE_DATOS
```

`React y ESLint`: Al código se le implementaron las siguientes reglas de ESLint como base 
```bash
'plugin:react/recommended', 'airbnb-base'
``` 
pero tiene algunas extra añadidas. <br><br>
`Script ESLint`: En el repositorio se proporciona un script (.eslintrc.json) para ver si el código de react contiene errores. Para probarlo se dirige a la carpeta donde se encuentre el archivo con extension .jsx que desee analizar y se corre el comando 
```bash
npx eslint nombre-archivo.jsx
```
Recuerde siempre estar dentro de la carpeta donde este el archivo .jsx a analizar
```bash
cd nombre-carptea
```

Realizado por: Linda Jimenez
