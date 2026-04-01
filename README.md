# AirKey 🔑

> Отвори вратата с едно движение. (Open the door with one movement.)

AirKey is an innovative smart access system that provides keyless entry using gesture recognition. This project aims to replace traditional keys, access cards, and chips by offering a more intuitive, hygienic, and secure access method for homes, buildings, and vehicles.

## Features ✨

* **Gesture Control**: Unlock doors simply by performing a predefined hand gesture in front of the sensor.
* **Enhanced Security & Hygiene**: Touchless operation eliminates the problem of lost keys and lowers the risk of spreading germs.
* **Contact Management System**: Integrated backend for handling customer inquiries and demo requests directly from the website, with status tracking (Pending, In Progress, Finished).

## Tech Stack 🛠️

* **Backend**: Python, Django 6.0.3
* **Database**: PostgreSQL
* **Frontend**: HTML5, CSS3, Bootstrap 5.3.0
* **Configuration**: Environment variables (`django-environ`)

## Project Structure 📁

* `airkey/` - Main Django configuration folder (`settings.py`, `urls.py`, etc.).
* `core/` - Application handling the landing page and core views.
* `contacts/` - Application responsible for the contact form and storing visitor inquiries in the database.
* `templates/` - HTML templates for the frontend.
* `static/` - Static assets including CSS, images, and JavaScript.

## Setup & Installation 🚀

1. **Clone the repository** and navigate to the project root:
   ```bash
   cd AirKey
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: Ensure requirements are exported if not already present)*

4. **Environment Variables**:
   Create a `.env` file in the same directory as `manage.py` containing your configuration:
   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key_here
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   The application will be accessible at `http://127.0.0.1:8000/`.

## Team 👥
* **Иван Тасев** (Ivan Tasev) – Designer
* **Деница Ганчева** (Denitsa Gancheva) – Manager
* **Петър Бухчев** (Petar Buhchev) – Programmer
* **Илияна Николова** (Iliyana Nikolova) – Sales
