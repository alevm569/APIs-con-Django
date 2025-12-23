# Python-APIs — Django REST Framework & Spotify
Este proyecto consiste en el desarrollo de una API REST utilizando Django y Django REST Framework (DRF), cuyo objetivo es gestionar usuarios y sus preferencias musicales, así como integrar una API externa (Spotify) para realizar búsquedas de artistas y canciones.
El proyecto se desarrolló como parte de una práctica académica, reutilizando y adaptando la lógica implementada previamente con **FastAPI**, pero ahora aplicándola en el ecosistema de **Django**.

## Estructura del Proyecto

```
music_api_django/
│── manage.py
│
│── music_api_django/
│   ├── settings.py
│   ├── urls.py
│
│── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
│── preferences/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
│── spotify/
│   ├── spotify_client.py
│   ├── views.py
│   ├── urls.py
│
│── requirements.txt
│── .env
```
## Instalación de Dependencias

```bash
pip install -r requirements.txt
```
## Configuración de Variables de Entorno

Crear un archivo `.env` siguiendo esta estructura:

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=
DB_PASSWORD=
DB_NAME=music_api_db

SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=
```

## Base de datos

Modelos principales
#### Usuario (User)
- username
- email
- full_name
- created_at

#### Preferencias (Preference)
- user (relación con User)
- genre
- favorite_artists (JSON)
- favorite_tracks (JSON)
- created_at

## Serializers
Funciones:
- Convertir datos entre objetos Django y formato JSON
- Validar los datos de entrada antes de almacenarlos en la base de datos.
Validaciones:
- Correos electrónicos y nombres de usuario únicos.
- Verificación de que los campos JSON sean listas.
- Manejo automático de errores HTTP 400.

## Endpoints de la API
### Users
| Método | Endpoint | Descripción |
|--------------|--------------|--------------|
| POST       | /api/users/       | Crear un usuario      |
| GET       | /api/users/       | Listar usuarios       |
| GET       | /api/users/{id}/       | Obtener un usuario       |
| PUT       | /api/users/{id}/       | Actualizar un usuario       |

### Preferences
| Método | Endpoint | Descripción |
|--------------|--------------|--------------|
| POST       | /api/users/{user_id}/preferences/       | Crear preferencias      |
| GET       | /api/users/{user_id}/preferences/       | Listar preferencias       |
| DELETE       | /api/users/{user_id}/preferences/{pref_id}/       | Eliminar una preferencia       |

### Spotify
```
GET /api/spotify/search?q=arctic+monkeys&type=artist
GET /api/spotify/search?q=505&type=track
GET /api/spotify/users/{id}/favorites/
```
## Ejecución del proyecto
Instalar dependencias:
```
pip install -r requirements.txt
```

Aplicar migraciones:
```
python manage.py migrate
```

Ejecutar servidor:
```
python manage.py runserver
```

## Conclusiones y Observaciones
- El uso de serializers facilita la validación y el manejo de errores.
- La arquitectura modular del proyecto mejora la mantenibilidad y escalabilidad.
- Una de las principales conclusiones técnicas obtenidas durante el desarrollo de este proyecto es que Django y Django REST Framework simplifican considerablemente la implementación de operaciones CRUD en comparación con otros frameworks. Esto se debe a que Django proporciona un ORM robusto, una gestión automática de migraciones y una integración nativa con serializers y vistas, lo que reduce significativamente la cantidad de código necesario para realizar operaciones comunes sobre la base de datos.
- DRF ofrece herramientas que facilitan la validación de datos, el manejo de errores HTTP y la serialización automática de objetos, permitiendo que el desarrollador se enfoque más en la lógica de negocio que en tareas repetitivas o de bajo nivel.

## URL: 
https://github.com/alevm569/APIs-con-Django
