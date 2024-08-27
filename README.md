# PYTHON-ENTREGA-FINAL-LUIS-COSSENET

# Texto formateado con Markdown:

<h1>Entrega Final.</h1>

- La plantilla html, es con base en el proyecto que entregué de desarrollo WEB, comisión 57650.
- En esta entrega final, apliqué todo el concepto de la tercera entrega y final, donde el sitio WEB se implementó con :
- Django
- Proyecto MagicoBQ
- Aplicaciones: AppMagico, users, blog.
- Contiene los conceptos herencia, static, bloques.
- Se utilizo vistas basadas en clases y vistas basadas en funciones.
- Se implementó el uso de la base de datos con SQLite3, donde se crearon las tablas de la base de datos y se insertaron datos en las tablas.
- Se utilizo templates para la creación de las páginas HTML.
- Se implemento carpeta pages dentro de templates.

- Para el CRUD desde admin se utilizo el admin.py, donde se crearon las clases de los modelos de las tablas de la base de datos.
- Esto se personalizo con list_display, list_filter, search_fields, date_hierarchy.

- Se implemento el uso de middleware, donde se creo un archivo middleware.py, para la validación de los usuarios que ingresan a la WEB.
- *El uso del middleware se utilizo para optimizar el uso de mixin y el decorador @login_required, para la validación de los usuarios que ingresan a la WEB.

- Se implemento el tiempo de sesion estableciendolo en settings.py, con la variable SESSION_COOKIE_AGE = 7200, donde se establece el tiempo de 7200 segundos.

- Se implemento avatar en el perfil del usuario, el cual se carga editando el perfil del usuario.
- El perfil se accede desde el menu de la WEB, presionando sobre el nombre del usuario, esto solo cuando esta logueado.

Models/Tablas:

- ESTADOS
- TIPO DOCUMENTO
- EMPRESA
- CARGOS
- CATEGORY
- SUBCATEGORY
- POST

Web Principal:

- Se creó la página principal de la WEB, donde se muestra el menú de la WEB.
- Se encuentra link con imagenes de la WEB, haciendo static, bloques y herencia.
- En el menu esta la opcion de CRUD, donde se puede ver la lista de los registros de las tablas de la base de datos.

- El video se anexara en la carpeta VideoEntrega de la raiz del proyecto.
- Video Python
- https://1drv.ms/f/s!AoI-wmCwLSV2iuwBUMXFrIhFCSDOlQ?e=OtCIRU

- Despliegue Docker:
- docker-compose up --build --force-recreate

- detener Docker
- docker-compose down

Luis Cossenet
