# Student Management API

Greetings! This is our RESTful API System developed by students **Luis Yovera (CI: 31.281.660)** and **Liz Falcon (CI: 30.924.770)**. This system handles student information management through **CRUD** operations, featuring data validation and database persistence.

##  Technologies Used

* **Language:** Python 3.10+
* **Framework:** FastAPI
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Data Validation:** Pydantic
* **Server:** Uvicorn

## Installation Instructions

Follow these steps to configure the project in your local environment:

1.  **Download the repository:**

    You can download the repository zip file and extract it, or use the following command:

    ```bash
    git clone <https://github.com/LuisYovera04/student-management-api/tree/main>
    cd student-management-api
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

##  How to Run the Project

1.  **Initialize the Database:**
    If you want to initialize a database with new tables, you must use this command first. If the database already exists, you can skip this step.

    ```bash
    py -m app.database.init_db
    ```

2.  **Start the Server:**
    Run the following command to launch the API:
    ```bash
    py -m uvicorn app.main:app --reload
    ```
    
    The server will start at: `http://127.0.0.1:8000`

## Interactive Documentation (Swagger UI)

This project includes automatic documentation generated with **Swagger/OpenAPI**.

Once the server is running, visit the following URL in your browser to view and test the endpoints:

 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

*(Here you can test GET, POST, PUT, DELETE methods directly from your browser).*

##  Endpoint Usage Examples

The API exposes the following endpoints under the prefix `/api/students`:

### 1. Get all students (GET)
* **Endpoint:** `/api/students/`
* **Description:** Returns the list of students.
* **Optional Filters:**
    * `?major=Ingenieria` (Filter by major)
    * `?semester=4` (Filter by semester)
    * `?is_active=true` (Filter by active/inactive status)

### 2. Create a student (POST)
* **Endpoint:** `/api/students/`
* **Body (JSON):**
    ```json
    {
      "first_name": "Juan",
      "last_name": "Perez",
      "email": "juan.perez@example.com",
      "major": "Systems Engineering",
      "semester": 1,
      "gpa": 3.5,
      "enrollment_date": "2024-01-30"
    }
    ```

### 3. Get a student by ID (GET)
* **Endpoint:** `/api/students/{id}`
* **Example:** `/api/students/1`

### 4. Update student (PUT)
* **Endpoint:** `/api/students/{id}`
* **Description:** Updates only the provided fields (Partial Update).

### 5. Delete student (DELETE)
* **Endpoint:** `/api/students/{id}`
* **Description:** Performs a "Soft Delete" (changes the `is_active` status to `false`).

##  Generative AI Usage

* **About AI usage:** For this project, I used **Gemini** as a "study companion". It helped me mainly to:
    * Understand strange console errors.
    * Improve the wording of this document.
    * Review that my code followed good practices (such as using English naming conventions).

* **Tool used:** Gemini (Google).
* **Purpose:** The AI was used as a "Pair Programmer" assistant for:
    * General code refactoring and cleanup.
    * Explanation of concepts regarding SQLAlchemy and FastAPI.
    * Base structure generation.
    * Debugging and syntax error correction.
* **Verification:** All generated code was manually reviewed, tested, and validated by the student to ensure correct functionality and compliance with requirements.

##  Coding Standards

This project strictly follows the requested naming and style guidelines:

* **Variables and Functions Naming:** `snake_case` (Ex: `create_student`, `user_id`).
* **Class Naming:** `PascalCase` (Ex: `Student`, `StudentResponse`).
* **Constant Naming:** `UPPER_SNAKE_CASE` (Ex: `SQLALCHEMY_DATABASE_URL`).
* **File Naming:** `snake_case.py` (Ex: `student_routes.py`, `db_config.py`).
* **Language:** All source code (variable names, functions, comments, and files) is written in **English**.