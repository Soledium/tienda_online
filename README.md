Proyecto Catálogo de Productos Personalizados – Django

- Este proyecto corresponde a una aplicación web desarrollada en Django y Django REST Framework, cuyo objetivo es la construcción de un catálogo de productos personalizados y la gestión de pedidos realizados por clientes.
- El sistema está orientado a la venta de productos personalizables, tales como tazones, zapatillas, poleras y polerones, permitiendo que el cliente suba imágenes de referencia al momento de realizar su pedido. La administración completa del sistema se realiza mediante el panel de administración de Django.


Tecnologías utilizadas

- Python 3
- Django
- Django REST Framework
- Base de datos relacional (SQLite en desarrollo / Sqlite con persistencia a través de volumen)
- Fly.io (despliegue en producción)

Descripción general del sistema

El proyecto contempla:
- Catálogo de productos, organizado por categorías
- Gestión de pedidos personalizados, con subida de imágenes de referencia por parte del cliente
- Administración de insumos, productos y categorías
- Estados de pedido, para el seguimiento del proceso
- API REST, utilizada para la creación, consulta y actualización de pedidos
- Panel de administración de Django, desde donde se gestionan todos los datos del sistema
- El sistema cuenta con un único rol administrador, correspondiente a un superusuario, encargado de gestionar la información y realizar modificaciones sobre productos, insumos, categorías y pedidos.


Entidades principales

- Productos: tazones, zapatillas, poleras y polerones
- Categorías: clasificación de los productos
- Insumos: elementos necesarios para la elaboración de los productos
- Pedidos: solicitudes realizadas por clientes, incluyendo imágenes de referencia
- Administrador: superusuario con acceso total al sistema mediante Django Admin


API REST

- La aplicación expone una API REST que permite:
- Crear pedidos
- Consultar pedidos
- Actualizar el estado de un pedido
- Gestionar información relacionada con los pedidos
- La API está pensada como base para futuras integraciones con interfaces web o móviles.


Deploy en Fly.io

El despliegue de la aplicación se realizó utilizando la plataforma Fly.io, la cual permite ejecutar aplicaciones Django en un entorno productivo de forma sencilla y escalable.

Pasos generales de despliegue
- Clonar el repositorio del proyecto: git clone <URL_DEL_REPOSITORIO> cd <NOMBRE_DEL_PROYECTO>
- Iniciar sesión en Fly.io: fly auth login
- Configurar variables de entorno necesarias: 
    * fly secrets set SECRET_KEY=valor
    * fly secrets set DATABASE_URL=valor

- Ejecutar el despliegue: fly deploy
- Durante el proceso de despliegue se ejecutan automáticamente las migraciones de la base de datos.


Monitoreo y logs

- Fly.io proporciona herramientas de monitoreo y visualización del estado de la aplicación.
En caso de presentarse inconvenientes durante el despliegue o la ejecución, es posible revisar los registros mediante: fly logs
- Además, Fly.io ofrece un panel de monitoreo, accesible desde su plataforma web, donde se puede verificar el estado de la aplicación, consumo de recursos y eventos relevantes.

Entorno de desarrollo local

Para ejecutar el proyecto en entorno local:
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver

- Con ello la aplicación estará disponible en: http://127.0.0.1:8000/

Este proyecto corresponde a una entrega académica, cuyo alcance se limita a las funcionalidades descritas en este documento.