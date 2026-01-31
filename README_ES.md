# Student Management API 🎓

¡Saludos!, Este es nuestro Sistema API RESTful desarrollado por los estudiantes Luis Yovera C.I: 31.281.660 y Liz Falcon C.I: 30.924.770, este sistema se encarga de la gestión
de información estudiantil mediante el uso de operaciones CRUD con validación y persistencia en la base de datos.

##  Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Framework:** FastAPI
* **Base de Datos:** SQLite
* **ORM:** SQLAlchemy
* **Validación de Datos:** Pydantic
* **Servidor:** Uvicorn

## Instrucciones de Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

1.  **Descargar el repositorio:**

    Puedes descargar el zip del repositorio y extraerlo o usar el siguiente comando:

    ```bash
    git clone <TU_LINK_DE_GITHUB_AQUI>
    cd student-management-api
    ```

2.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

##  Cómo Ejecutar el Proyecto

1.  **Inicializar la Base de Datos:**
    En el caso de que se quiera iniciar una base de datos con tablas nuevas, se tiene que usar primero este comando, en caso de no ser asi
    se puede saltar este paso

    ```bash
    py -m app.database.init_db
    ```

2.  **Iniciar el Servidor:**
    Ejecuta el siguiente comando para levantar la API:
    ```bash
    py -m uvicorn app.main:app --reload
    ```
    
    El servidor iniciará en: `http://127.0.0.1:8000`

## Documentación Interactiva (Swagger UI)

Este proyecto incluye documentación automática generada con **Swagger/OpenAPI**.

Una vez encendido el servidor, visita la siguiente URL en tu navegador para ver y probar los endpoints:

**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

*(Aquí podrás probar los métodos GET, POST, PUT, DELETE directamente desde el navegador).*

## Ejemplos de Uso de Endpoints

La API expone los siguientes endpoints bajo el prefijo `/api/students`:

### 1. Obtener todos los estudiantes (GET)
* **Endpoint:** `/api/students/`
* **Descripción:** Retorna la lista de estudiantes.
* **Filtros Opcionales:**
    * `?major=Ingenieria` (Filtrar por carrera)
    * `?semester=4` (Filtrar por semestre)
    * `?is_active=true` (Filtrar activos/inactivos)

### 2. Crear un estudiante (POST)
* **Endpoint:** `/api/students/`
* **Body (JSON):**
    ```json
    {
      "first_name": "Juan",
      "last_name": "Perez",
      "email": "juan.perez@example.com",
      "major": "Ingenieria en Sistemas",
      "semester": 1,
      "gpa": 3.5,
      "enrollment_date": "2024-01-30"
    }
    ```

### 3. Obtener un estudiante por ID (GET)
* **Endpoint:** `/api/students/{id}`
* **Ejemplo:** `/api/students/1`

### 4. Actualizar estudiante (PUT)
* **Endpoint:** `/api/students/{id}`
* **Descripción:** Actualiza solo los campos enviados (Partial Update).

### 5. Eliminar estudiante (DELETE)
* **Endpoint:** `/api/students/{id}`
* **Descripción:** Realiza un "Soft Delete" (cambia el estado `is_active` a `false`).

##  Uso de IA Generativa

* Sobre el uso de IA Para este proyecto, utilicé Gemini como un 'compañero de estudio'. Me ayudó principalmente a:
* Entender errores extraños que me daba la consola.
* Mejorar la redacción de este documento.
* Revisar que mi código siguiera buenas prácticas (como usar nombres en inglés).

* **Herramienta utilizada:** Gemini (Google).
* **Propósito:** La IA fue utilizada como asistente de programación ("Pair Programmer") para:
    * Refactorización y limpieza del código en general.
    * Explicación de conceptos sobre SQLAlchemy y FastAPI.
    * Generación de estructura base.
    * Debugging y corrección de errores de sintaxis.
* **Verificación:** Todo el código generado fue revisado, probado y validado manualmente por el estudiante para asegurar su correcto funcionamiento y cumplimiento de los requisitos.

## Estándares de Codificación

Este proyecto sigue estrictamente los lineamientos de nomenclatura y estilo solicitados:

* **Nomenclatura de Variables y Funciones:** `snake_case` (Ej: `create_student`, `user_id`).
* **Nomenclatura de Clases:** `PascalCase` (Ej: `Student`, `StudentResponse`).
* **Nomenclatura de Constantes:** `UPPER_SNAKE_CASE` (Ej: `SQLALCHEMY_DATABASE_URL`).
* **Nombres de Archivos:** `snake_case.py` (Ej: `student_routes.py`, `db_config.py`).
* **Idioma:** Todo el código fuente (nombres de variables, funciones, comentarios y archivos) está escrito en **Inglés**.