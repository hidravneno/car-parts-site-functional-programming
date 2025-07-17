# CarPartsSitee

## How to Run the Project

Follow these steps to install and run the CarPartsSitee project in your local environment:

### 1. Prerequisites

- Python 3.10 or higher
- pip
- Git
- [Optional] Recommended virtual environment (venv, virtualenv, etc.)

### 2. Clone the repository

```bash
git clone https://github.com/hidravneno/CarPartsSitee.git
cd CarPartsSitee
```

### 3. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Set up environment variables

Copy the `.env.example` file to `.env` and fill in the required values (e.g., email configuration).  
If `.env.example` does not exist, create a `.env` file with the necessary variables.

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create a superuser to access the admin panel

```bash
python manage.py createsuperuser
```

Follow the prompts to enter username, email, and password.

### 8. Run the development server

```bash
python manage.py runserver
```

Open your browser and go to:  
http://127.0.0.1:8000/

### 9. (Optional) Load sample data or set up inventory from the admin panel

Go to http://127.0.0.1:8000/admin with the superuser you created.

---


## Programación funcional en CarPartsSitee

Este proyecto aplica principios de programación funcional en Python y Django:

- Uso de funciones puras para el procesamiento de datos (ver `accounts/utils.py`, `products/utils.py`, `pages/utils.py`).
- Uso de funciones de orden superior como `map`, `filter` y `reduce` para transformaciones y agregaciones.
- Composición de funciones pequeñas para construir lógica más compleja.
- Preferencia por la inmutabilidad y el estilo declarativo.


---


### ¿Para qué sirve este resumen de rutas?

Esta sección te permite ubicar rápidamente en qué archivos y líneas del proyecto se está aplicando la programación funcional. Así, cualquier desarrollador puede identificar, entender y extender el uso de este paradigma en el código de forma sencilla y ordenada.

### ¿Dónde se aplica la programación funcional en este proyecto?

**accounts/utils.py**
- Línea 2: `get_emails(users)` — Usa map para obtener emails.
- Línea 6: `get_active_usernames(users)` — Usa filter y map para usernames activos.
- Línea 14: `is_valid_email(email)` — Función pura.
- Línea 19: `filter_active_users(users)` — Usa filter para usuarios activos.
- Línea 24: `get_usernames(users)` — Usa map para usernames.

**products/utils.py**
- Línea 2: `get_parts_by_category(parts, category)` — Usa filter para filtrar por categoría.
- Línea 6: `get_available_part_names_by_category(parts, category)` — Usa filter y map para nombres de partes disponibles por categoría.
- Línea 14: `filter_available_parts(parts)` — Usa filter para partes disponibles.
- Línea 20: `get_part_names(parts)` — Usa map para nombres de partes.
- Línea 25: `total_stock(parts)` — Usa reduce para sumar stock.

**pages/utils.py**
- Línea 2: `get_page_urls(pages)` — Usa map para URLs.
- Línea 6: `filter_pages_by_date(pages, date)` — Usa filter para filtrar por fecha.
- Línea 12: `filter_public_pages(pages)` — Usa filter para páginas públicas.
- Línea 17: `get_page_titles(pages)` — Usa map para títulos.

**products/views.py**
- Líneas 25, 32, 37, 38, 39, 40, 74, 83, 88: Uso de funciones funcionales (`get_parts_by_category`, `get_part_names`, `filter`, etc.) para filtrar, transformar y agregar datos en las vistas de inventario y listado.

**accounts/views.py**
- Línea 8: Importa y usa funciones funcionales (`is_valid_email`, `get_emails`, `get_active_usernames`).
- Líneas 20-21: Uso de `get_emails` y `get_active_usernames` en la lógica de registro.

**pages/views.py**
- Líneas 6-10: Ejemplo comentado de uso de funciones funcionales (`filter_public_pages`, `get_page_titles`, `get_page_urls`).




- Media files (product images) are stored in the `/media/` folder.
- To customize the design, edit the files in `/static` and `/templates`.
- If you have questions or issues, check the code documentation or contact the developer.

---

You’re all set! You can now use CarPartsSitee on your local environment.