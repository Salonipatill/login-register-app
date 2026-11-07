
## API Documentation

## 1. Introduction

API documentation expllains how to use the APIs of an application. it describes the available endpoints, HTTP methods, request data, response , status code, authentication, and error handling.

This document also explain how to connect the frontend with the FastAPI backend.

## 2. API Overview

The application uses the following technologies:

Frontend: HTML,CSS,JavaScript
Bckend: Python, FastAPI
Database: MySQL
Communication: HTTP request and JSON data

The frontend sends request to the backend. The backend processes the requests, intercts with the database when necessary, and returns responses to the frontend.

## 3. API Request and Response

## 3.1 Request Information

For each API  endpoint, document:

Endpoint: The URL path of the API.
HTTP Method: The operation used , such as GET or POST.
Purpose: What the API does.
Request Body: The informtation sent by the frontend.

Authentication: Whether Authentication is required.


## 3.2 Example Registration Request

Endpoint: /api/auth/register

HTTP method: POST

Purpose:Register a new user.

Request Body:
{
    "full_name" : "Example User",
    "email" : "user@example.com",
    "passward" : "ExamplePassward123"

}

## 3.3 Response Information

Document the following details for each response:

HTTP status code
Response message
Response data, if applicable

## Example: Successful Response

Status Code: 201 Created

{
    "message" : "Registration successful"
}


Example: Error Response

Status Code: 409 Conflict
{
    "detail" : "An account with this email already exists"

}

These are example responses. The actual responsees should match your Implemented API

## 4. API Endpoints

Document every API endpoint in a table.

Endpoint                        |  HTTP Method            | Purpose                                | Authentication Required


/api/auth/register              |        POST             | Register a new user                    |    No

/api/auth/login                 |          POST           | Log in existing user                   |     No


/api/auth/logout                |           POST          |Log out the current user                |    Yes

/api/auth/me                    |           GET           |Get the current user's  information     |    Yes

/api/auth/forgot-password       |         POST            |Request a password reset link           |    No


/api/auth/reset-passward        |          POST           | Set a new password usign a valid       | No
                                                           reset token    



Additional endpoints for Google login, GitHub login, and passkeys will be documented when implemented.

5. Error Handling

The backend must return appropriate status codes and error messages when a request fails.

Status Code

Meaning

Example

400 Bad Request

The request cannot be processed as submitted

Invalid or unusable request

401 Unauthorized

Authentication is missing or invalid

Incorrect login credentials

403 Forbidden

The user is not permitted to perform an operation

Insufficient permissions

404 Not Found

The requested resource does not exist

Requested resource not found

409 Conflict

The request conflicts with existing data

Email already registered

422 Unprocessable Entity

Request data fails validation

Missing or invalid field

500 Internal Server Error

An unexpected server error occurred

Unexpected backend failure

The frontend should read the response and display a suitable message to the user.

Never expose passwords, secret keys, or sensitive internal error details in API responses.

6. Frontend Setup

Requirements

A web browser.

A code editor, such as VS Code.

Python installed.

The project's frontend and backend dependencies.

Frontend Files

index.html — Contains the registration and login forms.

style.css — Defines the application's appearance.

script.js — Handles form events, sends API requests, and displays responses.

Explain how to open or serve the frontend according to your chosen development setup.

7. Backend Setup

Requirements

Python.

FastAPI.

Uvicorn.

MySQL and the required database driver.

Setup Steps

Open a terminal in the backend directory.

Create and activate a Python virtual environment.

Install the dependencies listed in requirements.txt.

Configure the environment variables.

Start the FastAPI development server.

Open the interactive API documentation at /docs.

Document the exact commands after setting up your project.

8. Frontend–Backend Connection

The frontend communicates with FastAPI through HTTP requests.

JavaScript uses the fetch() API to send requests and receive responses.

Communication Flow

The user submits a form.

JavaScript collects the form data.

JavaScript sends an HTTP request to the appropriate FastAPI endpoint.

FastAPI validates and processes the request.

The backend interacts with MySQL if required.

FastAPI returns a response.

JavaScript handles the response and displays a success or error message.

Document the API base URL, request headers, request format, response format, and error-handling behavior.

9. CORS Configuration

CORS stands for Cross-Origin Resource Sharing.

It controls whether a browser allows frontend code from one origin to access a backend on another origin.

For example, the frontend might run on port 5500, while FastAPI runs on port 8000.

If they have different origins, configure FastAPI to allow requests from the specific frontend origin.

Document:

The frontend origin.

The backend origin.

The allowed HTTP methods.

The allowed request headers.

Whether credentials, such as session cookies, are required.

Allow only the origins and permissions your application needs.

10. Environment Configuration

Environment variables store configuration values separately from application code.

Examples include:

Database host.

Database name.

Database username.

Database password.

Application secret key.

Google OAuth credentials.

GitHub OAuth credentials.

Email service configuration.

Store secret values in the environment, not in frontend JavaScript or committed source code.

Add .env to .gitignore so that your real credentials are not pushed to GitHub.

11. Authentication and Security

Document how authentication works in the application.

Include:

Password hashing.

Login verification.

Session or token management.

Logout behavior.

Password reset token validation and expiration.

OAuth authentication.

Passkey authentication using WebAuthn.

Passwords must never be stored in plaintext. Passkey implementations should store credential information and public keys, not fingerprint or face data.

12. API Testing

Document how to test the APIs using:

FastAPI Swagger UI at /docs.

Automated tests using Pytest.

Successful requests.

Invalid requests.

Authentication failures.

Database errors and other expected failure cases.

Update this section as you add tests and implement additional endpoints.

13. Future Updates

Update this document whenever an endpoint, request format, response format, status code, or authentication behavior changes.                            




