# FastAPI Notes Application

This is a notes application built using Python's FastAPI framework. Users can sign up, log in, create notes, and retrieve them based on their user ID. This README provides instructions on how to set up the environment, install dependencies, and run the application.

## Features

- **User Signup**: Register new users with a username and password.
- **User Login**: Authenticate users and generate a dummy token.
- **Create Notes**: Authenticated users can create notes associated with their account.
- **Retrieve Notes**: Users can retrieve all notes they've created.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python 3.x**. You can download it from [python.org](https://www.python.org/downloads/).

## Installation

Follow these steps to set up your environment and install the required dependencies:

### 1. Clone the Repository

```bash
git clone https://github.com/luqmansarwar012/python_notes_app.git

cd python_notes_app
```

### 2. Create a Virtual Environment

It’s recommended to use a virtual environment to manage dependencies. You can create one using \`venv\`:

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

- On **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

With the virtual environment activated, install the required packages listed in \`requirements.txt\`:

```bash
pip install -r requirements.txt
```

## Database Setup

The application uses SQLAlchemy as the ORM to interact with the database. You can modify the database URL in \`database.py\`

### Database Migration

If it's the first time you're running the application, you'll need to initialize the database:

```bash
# Create the database tables
python -m create_db.py
```

## Usage

Once the installation is complete, you can run the application with:

```bash
fastapi dev main.py
```

The application will be available at `http://127.0.0.1:8000/`.

## API Endpoints

### User Endpoints

- **POST /user/signup**: Create a new user
- **POST /user/login**: Log in and retrieve a token

### Notes Endpoints

- **POST /note/create**: Create a new note
- **GET /note/get/{user_id}**: Retrieve all notes for a specific user
