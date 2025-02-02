## 🚀 FAQ Management System

## Description
This is a Django-based FAQ management system that supports multi-language translations, a WYSIWYG editor for answers, and a REST API for managing FAQs. It also includes caching with Redis for improved performance.

---
## Features
1. Multilingual Support: FAQ content is available in multiple languages (English, Hindi, Bengali, Telugu, Tamil, Malayalam, Kannada).
2. WYSIWYG Editor: Rich text editor for FAQ answers (using django-ckeditor).
3. Automatic Translation: Translates FAQ questions and answers using Google Translate API during object creation.
4. Caching: Caching with Redis for faster API responses.
5. REST API: Endpoints for managing and retrieving FAQs with language support.
6. Django Admin: Admin panel to manage FAQs and their translations easily.

## Table of Contents
1. [Installation](#installation)
2. [API Usage](#api-usage)
3. [Contribution Guidelines](#contribution-guidelines)
4. [License](#license)

---

## 🛠️ Installation

### Prerequisites
- Python 3.9 or higher
- Docker and Docker Compose 
- Redis (for caching)

### Steps

#### **Local Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/Chetana1911/BharatFD_FAQs_Management_System.git
   cd faq_project



2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source  `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the Redis server. If you're using Docker, you can run Redis using:

    ```bash
    docker-compose up -d
    ```

5. Apply migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser for Django Admin:

    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

Now you can access the project at `http://localhost:8000`.

## 📡 API Usage

The system exposes a **REST API** to manage and retrieve FAQs.

### Endpoints

1. **GET /api/faqs/**: Get a list of FAQs.
    - Example: `curl http://localhost:8000/api/faqs/`
    - Supports language selection with the `?lang=<language_code>` query parameter.

    **Example Requests:**
    ```bash
    # Fetch FAQs in English (default)
    curl http://localhost:8000/api/faqs/

    # Fetch FAQs in Hindi
    curl http://localhost:8000/api/faqs/?lang=hi

    # Fetch FAQs in Bengali
    curl http://localhost:8000/api/faqs/?lang=bn
    ```

## 🛠️ Caching

The API uses **Redis** for caching FAQ translations. By default, the cache is stored in `redis://127.0.0.1:6379/1`.

## 🖥️ Admin Panel

You can access the Django admin panel at `http://localhost:8000/admin/`.
- Login with the superuser credentials you created earlier.
- Manage FAQs and their translations.

## Docker Support

This project comes with a `Dockerfile` and `docker-compose.yml` file for containerized deployment.

### Running with Docker

1. Build and run the containers:

    ```bash
    docker-compose up --build
    ```

2. The application will be available at `http://localhost:8000`.

## 🧪 Tests

To run tests, make sure to activate your virtual environment and run:

```bash
pytest
```

Unit Tests

Unit tests are included to test:
	•	Model methods (for translation and caching).
	•	API responses (ensure that the FAQ data is correctly returned in different languages).

Git Commit Messages

Follow conventional commit message practices:
	•	feat: Add multilingual FAQ model
	•	fix: Improve translation caching
	•	docs: Update README with API examples

Ensure atomic commits with clear commit messages.

## 🤝 Contributing
## We welcome contributions! Follow these steps:
1. Fork the Repository.
2. Create a Branch:
```bash
git checkout -b feature-name
```
3.Your Changes.
4.Commit Your Changes:
```bash
git commit -m "feat: Add feature"
git commit -m "fix: Fix bug"
git commit -m "docs: Update documentation"
```
5.Push to Your Fork:
```bash
git push origin feature-name
```

6.Open a Pull Request.


## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
