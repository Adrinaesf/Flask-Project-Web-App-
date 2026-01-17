# Flask Sign-Up Project – Intro to Flask & Python

## Overview

This project is a beginner-friendly introduction to **Flask**, Python’s lightweight web framework.  
The goal is not just to make a sign-up page work, but to understand how Flask applications are structured and how the frontend and backend communicate.

### This project covers:
- Flask routing  
- Handling form submissions  
- Using templates (HTML)  
- Passing messages from backend → frontend  
- Thinking in terms of requests, responses, and users  

---

## How to Think About a Flask App

A Flask app has **three main parts**:

### 1. Frontend (HTML / CSS / JS)
- What the user sees  
- Forms, buttons, input fields  
- Displays messages (errors, success alerts, etc.)

### 2. Backend (Flask + Python)
- Handles logic  
- Receives data from the frontend  
- Validates input  
- Talks to the database  
- Decides what response to send back  

### 3. Database
- Stores users and their information  
- Uses relationships (like foreign keys) to connect data to a specific user  

---

## Request → Response Flow (Very Important)

When a user signs up:

1. User fills out the sign-up form  
2. User clicks **Submit**  
3. Browser sends a **POST request** to Flask  
4. Flask:
   - Reads the form data  
   - Checks if it’s valid  
   - Creates the user (or rejects it)  
5. Flask sends a response back  
6. The template displays:
   - A success message **or**
   - An error message  

**Flask does nothing automatically** — every message you see must be sent explicitly from Python to HTML.

---

## Why Messages Only Appear With Certain Code

Messages (like **“User created successfully”** or **“Email already exists”**) only appear when:

- The backend adds them to the response  
- The template renders them  

If you remove the message logic from the `sign_up` route, Flask has nothing to send — so nothing appears on the page.

This is intentional. Flask keeps **logic** and **presentation** separate.

---

## How Flask Knows Which User the Message Is For

Flask does **not** guess the user.

It knows because:
- The request belongs to one browser session  
- The message is attached to that response  
- Only that user receives it  

If you’re using a database:
- Users are identified by an `id`  
- Related data uses **foreign keys**

Example:
```text
user.id → messages.user_id
