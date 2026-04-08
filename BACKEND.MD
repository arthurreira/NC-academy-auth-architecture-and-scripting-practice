# Backend Specification

Authentication & Account Management API

## Overview

The backend provides an API responsible for authentication, user account management, and secure communication with the database. It handles credential validation, session management, and user data updates.

The backend exposes endpoints used by the frontend application to perform authentication and account operations.

---

## Technology Stack

The backend system is built using the following technologies:

- Node.js
- Express.js
- SQL database
- Arcjet security and rate limiting

---

# System Responsibilities

The backend is responsible for:

- User authentication
- Account creation
- Session management
- Secure password handling
- User account updates
- Rate limiting and request protection
- Communication with the SQL database

---

# API Structure

The API is organized into logical groups.

Primary route groups include:

- Authentication routes
- User account routes

---

# Authentication Routes

Authentication routes handle account creation and user login.

Base path: /auth

---

## Signup Endpoint

### Endpoint



### POST /auth/signup 



### Purpose

Creates a new user account.

### Request Data

The request contains user credentials required to create an account.

Fields include:

- Email
- Password

### Behavior

- Validates input fields
- Checks if the email is already registered
- Creates a new user record in the database
- Stores the password securely
- Starts an authenticated session
- Returns success response to the client

### Error Cases

Possible errors include:

- Email already exists
- Invalid input data
- Server error during account creation



## Login Endpoint

### Endpoint


### POST /auth/login


### Purpose

Authenticates an existing user.

### Request Data

The request includes login credentials.

Fields include:

- Email
- Password

### Behavior

- Validates input fields
- Checks if the user exists
- Verifies the password
- Creates an authenticated session
- Returns authentication success

### Error Cases

Possible errors include:

- Invalid credentials
- User not found
- Rate limit triggered
- Authentication failure

---

# User Routes

User routes allow authenticated users to access and modify account information.

Base path:/auth/login
 


These routes require a valid authenticated session.

---

## Get Current User

### Endpoint

### /user

### Purpose

Returns the currently authenticated user information.

### Behavior

- Verifies authentication session
- Retrieves user data from the database
- Returns account information

### Response Data

User information includes:

- User ID
- Email

---

## Update Email

### Endpoint
