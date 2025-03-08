# AI-Powered Q&A Agent

## Overview
This is a simple AI-powered chatbot application built using Django (backend) and React (frontend). The chatbot uses an AI model to process user queries and provide intelligent responses while maintaining conversation history.

## Technologies Used
- **Backend**: Python 3.13, Django 5.2, Django REST Framework
- **Frontend**: React (JavaScript)
- **AI Model**: Integrated via Groq API
- **Ngrok**: Used for exposing the local server to the internet

---

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/MuhammadShahbazRaza/chatbot_backend.git
cd chatbot_backend
```

### 2. Backend Setup (Django)

#### Install Dependencies
Ensure you have Python 3.13 installed. Then, set up a virtual environment and install dependencies:
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

#### Run Database Migrations
```sh
python manage.py migrate
```

#### Start the Django Server
```sh
python manage.py runserver
```
By default, Django will run on `http://127.0.0.1:8000/`.

#### Expose the API using Ngrok
Open a new terminal and run:
```sh
ngrok http 8000
```
This will provide a public `https://xxxxx.ngrok-free.app` URL. **Copy this URL**, as you will need to update it in the React frontend.

---

### 3. Frontend Setup (React)

#### Install Dependencies
Ensure Node.js and npm are installed, then navigate to the frontend folder:
```sh
cd frontend  # Adjust the path if needed
npm install
```

#### Update API Endpoint
Open `App.jsx` and replace the `API_URL` with your Ngrok endpoint:
```js
const API_URL = "https://xxxxx.ngrok-free.app/chat/"; // Replace with your actual Ngrok URL
```

#### Start the React App
```sh
npm run dev
```
This will start the development server, accessible at `http://localhost:5173/`.

---

## Usage
- Open the React app in your browser.
- Type a message in the input box and send it.
- The chatbot will respond, and the conversation history will be maintained.

---

## Troubleshooting
- **Ngrok endpoint not working?** Restart `ngrok http 8000` and update the new endpoint in React.
- **Backend issues?** Ensure all dependencies are installed and migrations are applied.
- **Frontend not connecting?** Check `API_URL` in `app.jsx` and restart the React app.

---

