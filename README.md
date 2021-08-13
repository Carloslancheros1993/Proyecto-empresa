###Sistema de facturacion de productos###

##Installar Django
pip install Django==2.2

##Instalar Django rest framework para construir el proyecto
pip install djangorestframework

##Crear usuario para poder usar el ORM de Django
python manage.py createsuperuser

##Creaar proyecto en Django
django-admin start project sistemaFacturaion .

##Installar 'rest_framework' en settings del proyecto
En INSTALLED_APPS agregar 'rest_frameework'

#Migrar todos los archivos que vienen con django
python manage.py migrate

##Crear las aplicaciones que va a contener el proyecto con sus respectivas llaves foraneas y pk.
python manage.py starapp clients
python manage.py starapp bills
python manage.py starapp products
python manage.py starapp billsProducts

##Installar las aplicaciones en settings del proyecto
INSTALLED_APPS = [
    'clients.apps.ClientsConfig'

##Crear modelos
Crear la estructura de cada una de las aplicaciones en el archivo models de la
carpeta de cada aplicación


##Resgistar aplicacion para poderla visualizar en el ORM
Agregar modelo al admin de Django
admin.site.register(Client)

##Realizar migraciones
python manage.y makemigrations
python manage.py migrate

##Crear visualizacion de las aplicaciones
Crear archivo serializers.py dentro de la carpeta de cada app y creo codigo para la visualización de las apps
Ir a el archivos views.py y con ayuda de generics creo la logica para crear el CRUD de cada una de las aplicaciones

##ListCreateAPIView
Provee metodo get y post

##RetriveUpdateDestroyAPIView
Provee los metodos de get, put, delete y patch

##Crear archivos urls en cada aplicacion para proyectar vistas
Crear archivo urls.py en la carpeta de cada app e import las vistas creadas anteriormente

##Crear ruta para el ORM
Creo la ruta de como llegar a mi app en el servidor
path('clients/', include('clients.urls'))


##Probar cada una de las peticiones en el ORM o en POSTMAN
http://127.0.0.1:8000/clients/

python manage.py starapp billsProducts

##ENDPOINT REGISTRAR UN USUARIO

##Installar jwt
pip install djangorestframework-simplejwt

##Configurar jwt en el proyecto
Con ayuda de la documentacion de jwt para django escribo codigo en settings del proyecto

##Creo endpoints de registro
En archivo urls.py del proyecto agrego las rutas para el registro de los usuarios

##Comprobar registro
Verificar codigo usando la ruta http://127.0.0.1:8000/api/token/ y los parametros asignados para el registro,
aqui usar el usuario del ORM y la contraseña

##USO DE ENCABEZADOS
Al crear un usuario copiar el token de la parte refresh, dirijirse a headers de Postman
en key escribir authorization y en value Bearer y justo al lado de Bearer pasar el token

##ENDPOITN PARA REGISTRAR UN USUARIO E INICIAR SESIÓN

##Crear nueva app users

##Crear serializers.py
Crear codigo con los parametros que usare para el registro del usuario

##Crear vistas
Para este registro e inició de sesion me apoye usando viewset y DefaultRouter para crea
