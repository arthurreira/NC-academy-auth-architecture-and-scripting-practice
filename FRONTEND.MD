# Frontend Specification

Authentication & User Dashboard UI

## Overview

The frontend application provides a user interface for customer authentication and account management. Users can create an account, log in, and manage their account settings through a dashboard.

The application consists of authentication views and a user dashboard. Access to the dashboard is restricted to authenticated users.

---

## Technology Stack

The frontend interface is built using the following technologies:

- React
- TailwindCSS
- shadcn/ui component library
- Zod validation
- Arcjet rate limiting (handled by backend)

---

# Application Views

The frontend consists of the following views:

1. Login  
2. Signup  
3. Dashboard  

Each view is described below.

---

# Authentication Views

Authentication views are accessible to users who are not logged in.

---

## Login View

### Purpose

Allows an existing user to authenticate using their credentials.

### Components

Login form containing:

- Email field
- Password field
- Login button
- Link to signup page

### Behavior

- User enters email and password.
- Form validates input before submission.
- If credentials are correct, the user is redirected to the dashboard.
- If authentication fails, an error message is displayed using sonner from shadcn ui.

### Validation

Input validation includes:

- Email must be a valid email format
- Password must meet minimum length requirements 8 characters,bumbers,symbols...

### Navigation

- Link to signup view for users without an account.
- Link to login view for users with account to login.
- Link to dashboard when logged in.


---

## Signup View

### Purpose

Allows a new user to create an account.

### Components

Signup form containing:

- Email field
- Password field
- Signup button
- Link to login page

### Behavior

- User enters email and password.
- Form validates input before submission.
- Upon successful account creation, the user is redirected to the dashboard.

### Validation

Input validation includes:

- Email must be valid
- Password must meet minimum length requirements

### Navigation

- Link to login view for existing users.

---

# Dashboard View

## Purpose

The dashboard allows authenticated users to manage their account information.

Only authenticated users can access this view.

---

# Dashboard Layout

The dashboard contains account management sections.

Main sections include:

1. Account information  
2. Security settings  
3. Session control  

---

## Account Information Section

### Purpose

Displays user account information and allows the user to update their email address.

### Components

- Current email display
- Email update input
- Save changes button

### Behavior

- User can enter a new email address.
- Input is validated before submission.
- If successful, the updated email is reflected in the account information.

---

## Security Settings Section

### Purpose

Allows the user to change their account password.

### Components

Password update form containing:

- Current password field
- New password field
- Confirm new password field
- Update password button

### Behavior

- User enters current password and a new password.
- Password inputs are validated.
- If successful, the password is updated.

---

## Session Control

### Purpose

Allows the user to end their authenticated session.

### Components

- Logout button

### Behavior

- Clicking logout ends the user session.
- User is redirected to the login view.

---

# Form Validation

All forms perform input validation before submission.

Validation rules include:

- Email must follow a valid email format
- Password must meet defined minimum length
- Password confirmation must match the new password when updating credentials

Validation errors are displayed to the user.

---

# Error Handling

The UI must display clear feedback for errors, including:

- Invalid login credentials
- Email already in use
- Incorrect password when updating credentials
- Validation failures

Error messages are displayed near the relevant input fields or as form-level feedback.

---

# Security Considerations

Security mechanisms affecting the UI include:

- Backend rate limiting applied to authentication requests
- Secure handling of authentication sessions
- Protection of authenticated routes from unauthorized access

---

# Navigation Flow

User flows through the application follow these paths.

### New User Flow

Signup → Dashboard

### Returning User Flow

Login → Dashboard

### Authenticated User Flow

Dashboard → Update Account Settings → Logout → Login

---

# Access Control

The dashboard view is restricted to authenticated users.

If an unauthenticated user attempts to access the dashboard, they are redirected to the login view.