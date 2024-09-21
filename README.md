# Twitter-like App

This repository is based on the YouTube tutorial **"Create a Twitter-like App with Python, Django, JavaScript, and React"**. It is a full-stack web application that mimics core functionalities of Twitter, using **Django** for the backend and **React** for the frontend.

## Features

- User authentication (login/logout)
- Tweet creation, deletion, and display
- Like and unlike tweets
- Follow and unfollow users
- Timeline view showing tweets from followed users
- Dynamic front-end powered by React and JavaScript
- Backend powered by Django REST framework

## Tech Stack

- **Backend**: Python, Django, Django REST Framework
- **Frontend**: React, JavaScript
- **Database**: SQLite (default, can be switched to PostgreSQL or another DB engine)
- **Styles**: CSS, Bootstrap (optional)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/twitter-like-app.git
   cd twitter-like-app
   ```

2. **Backend Setup**:
   - Create a virtual environment:
     ```bash
     python3 -m venv env
     source env/bin/activate  # On Windows: env\Scripts\activate
     ```
   - Install backend dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Apply migrations and run the server:
     ```bash
     python manage.py migrate
     python manage.py runserver
     ```

3. **Frontend Setup**:
   - Navigate to the `frontend` folder:
     ```bash
     cd frontend
     ```
   - Install frontend dependencies:
     ```bash
     npm install
     ```
   - Start the frontend development server:
     ```bash
     npm start
     ```

4. **Access the App**:
   Open your browser and go to `http://localhost:8000/` to view the application.

## API Endpoints

This application uses Django REST Framework to create API endpoints for managing tweets, likes, and user information.


## Contributing

If you want to contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Push your branch (`git push origin feature-branch`)
5. Open a Pull Request


---

Feel free to adjust any details as needed!
