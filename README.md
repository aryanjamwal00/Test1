# Opportunity Management System

## 📌 Overview

A full-stack web application that allows users to register, log in, and manage opportunities through a dynamic dashboard. The system is built using Flask (Python) for the backend and HTML, CSS, and JavaScript for the frontend.

---

## 🚀 Features

* User Authentication (Signup & Login)
* Opportunity Management

  * Create Opportunities
  * View Opportunities
  * Edit Opportunities
  * Delete Opportunities
* User-specific data handling
* Persistent storage using SQLite database
* Responsive UI dashboard

---

## 🛠️ Tech Stack

**Frontend:**

* HTML
* CSS
* JavaScript

**Backend:**

* Flask (Python)

**Database:**

* SQLite

---

## 📂 Project Structure

```
Test1/
│
├── index.html
├── admin.css
├── admin.js
│
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── routes/
│   │   ├── auth.py
│   │   └── opportunity.py
│   └── database.db
```

---

## ⚙️ How to Run the Project

### 1. Navigate to Backend

```
cd backend
```

### 2. Activate Virtual Environment

```
source venv/Scripts/activate   (Git Bash / Windows)
```

### 3. Install Dependencies

```
pip install flask flask_sqlalchemy flask_cors werkzeug itsdangerous
```

### 4. Run Backend Server

```
python app.py
```

Server will run at:

```
http://127.0.0.1:5000
```

---

### 5. Run Frontend

Open:

```
index.html
```

in your browser

---

## 🌐 Deployment

* Frontend is deployed using GitHub Pages
* Backend runs locally using Flask

👉 Note:
The deployed frontend cannot communicate with the backend unless the Flask server is running locally.

---

## 🎥 Demo Functionality

* User Signup
* User Login
* Create Opportunity
* View Opportunities
* Edit/Delete Opportunities
* Data Persistence after reload

---

## 📌 Limitations

* Backend is not deployed online
* API calls require local server to be running

---

## 👨‍💻 Author

Aryan Jamwal

---

## 📎 Repository Link

https://github.com/aryanjamwal00/Test1

## ⚠️ Known Issues / Limitations

* When accessing the project via the GitHub Pages link, users may encounter a **"Server Error"** during actions like login or signup.

* This happens because the frontend (hosted on GitHub Pages) tries to communicate with a backend server running at:

  ```
  http://127.0.0.1:5000
  ```

  which is **only available on the developer's local machine**.

* For other users (e.g., friends or evaluators), `127.0.0.1` refers to **their own system**, where the backend server is not running, resulting in failed API calls.

* Therefore, full functionality (authentication, CRUD operations) works **only when the Flask backend is running locally**.

---

## 💡 Solution / Workaround

To run the project fully:

1. Navigate to backend folder:

   ```
   cd backend
   ```

2. Activate virtual environment:

   ```
   source venv/Scripts/activate
   ```

3. Start Flask server:

   ```
   python app.py
   ```

4. Open frontend:

   ```
   index.html
   ```

---

## 📌 Note

The frontend is deployed for demonstration purposes only.
Due to hosting limitations, the backend is not deployed online.

In a real-world deployment, the backend would be hosted on platforms such as:

* Render / Railway / AWS / Heroku
