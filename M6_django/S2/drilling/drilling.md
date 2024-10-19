##### Creación de un proyecto django

1.- crear una carpeta que almacene el proyecto
    dirigirse a la carpeta creada y abrirla en la terminal
2.- crear entorno local
```
python -m venv .venv
```
3.- activar el entorno local o utilizar el entorno global existente cuando se instala python
```
.venv\Scripts\activate.ps1
```
4.- instalar django en el entorno, si esta instalado no es necesario
```
pip list
python.exe -m pip install --upgrade pip
pip install django
```
5.- inicializar proyecto django dentro de la carpeta creada en el primer paso
```
django-admin startproject site_django
django-admin startproject nombre_proyecto
```
6.- ingresar a la carpeta del proyecto creado con django-admin startproject
```
cd nombre_proyecto
django-admin startapp book
```
7.- modificar el archivo settings.py en el proyecto para registrar el aplicativo o app creada en el punto 6, con django-admin startapp
```
INSTALLED_APPS = [
    'book.apps.BookConfig', # agregando la app book al registro de aplicaciones instaladas
]
```
8.- ejecutar migraciones
```
python manage.py migrate
python .\manage.py migrate
```
9.- ejecutar el servidor local para verificar que todo este correcto
> dirigirnos a donde se encuentra el archivo manage.py dentro del proyecto
```
python manage.py runserver
python .\manage.py runserver
```
10.- Buscar ayuda sobre los comandos que podemos ejecutar con python manage.py
```
python manage.py help
python manage.py help <comando>
```
Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver

