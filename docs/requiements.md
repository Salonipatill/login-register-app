# Project Requirements

## 1. Project Overview

The Login and Registration application is a web application that allows users to create accounts, log in securely, and manage their account access.

The application will have a frontend for user interaction, a FastAPI backend for processing requests, and a MySQL database for storing user information.

The project will be developed step by step, and each feature will be tested after implementation.

## 2. Project Objectives

The main objectives are:

- Allow new users to register for an account.
- Allow registered users to log in securely.
- Provide a password-reset feature.
- Support Google and GitHub sign-in.
- Support passkey authentication using WebAuthn.
- Store user information securely in a database.
- Connect the frontend to the backend through APIs.
- Test application features and handle errors appropriately.

## 3. Technology Stack

| Component | Technology | Purpose |
|---|---|---|
| Frontend | HTML | Structure of web pages |
| Frontend styling | CSS | Design and layout |
| Frontend functionality | JavaScript | Form handling and API requests |
| Backend | Python | Application logic |
| Backend framework | FastAPI | API development |
| Database | MySQL | Persistent data storage |
| Database toolkit | SQLAlchemy | Database interaction |
| API testing | FastAPI Swagger UI | Testing API endpoints manually |
| Automated testing | Pytest | Testing application behavior |
| Version control | Git and GitHub | Tracking and managing code changes |

## 4. Functional Requirements

Functional requirements describe what the application must do.

### 4.1 User Registration

The application must allow a new user to create an account.

**Required fields:**

- Full name
- Email address
- Password
- Confirm password

**Requirements:**

- All required fields must be validated.
- The email address must have a valid format.
- The password and confirm-password fields must match.
- The application must prevent duplicate email registrations.
- Passwords must be securely hashed before being stored.
- The application must display an appropriate success or error message.

### 4.2 User Login

The application must allow registered users to sign in.

**Required fields:**

- Email address
- Password

**Requirements:**

- The backend must verify the submitted credentials.
- Invalid credentials must not grant access.
- Successful login must establish an authenticated session or another chosen authentication mechanism.
- The application must display appropriate success or error messages.
- Authenticated endpoints must verify the user's authentication status.

### 4.3 Logout

The application must allow an authenticated user to log out.

**Requirements:**

- The current authentication session must be invalidated or cleared appropriately.
- The user must no longer have access to protected features through the terminated session.
- The application must display the appropriate result.

### 4.4 Forgot Password

The application must allow a user to request a password-reset link.

**Requirements:**

- The user must be able to enter their email address.
- The backend must process the reset request.
- The application must provide a generic response that does not reveal whether an account exists.
- An eligible account must receive a password-reset link by email.
- The reset token must expire after a limited period.

### 4.5 Reset Password

The application must allow a user to set a new password using a valid reset link.

**Requirements:**

- The user must enter a new password and confirm it.
- Both password fields must match.
- The backend must validate the reset token.
- Expired or previously used tokens must be rejected.
- The new password must be securely hashed before storage.
- A successful reset must invalidate the token.

### 4.6 Google Sign-In

The application should allow users to authenticate using their Google account.

**Requirements:**

- The application must use the appropriate OAuth authentication flow.
- The backend must handle OAuth callbacks and validate the authentication result.
- OAuth client secrets must not be exposed in frontend code.
- The user must be authenticated only after successful verification.

### 4.7 GitHub Sign-In

The application should allow users to authenticate using their GitHub account.

**Requirements:**

- The application must use the appropriate OAuth flow.
- The backend must process the authentication callback.
- The external account identity must be verified.
- OAuth secrets must remain on the backend.

### 4.8 Passkey Authentication

The application should support passkey registration and login using WebAuthn.

**Requirements:**

- Users should be able to register a passkey after creating their account.
- Users should be able to sign in using a previously registered passkey.
- The backend must verify WebAuthn authentication responses.
- Credential information and public keys must be stored securely.
- The application must not collect or store fingerprint or face scans.

Passkey authentication must use WebAuthn rather than relying only on a fingerprint icon or button.

### 4.9 User Interface

The application must provide a clear and consistent interface.

**Requirements:**

- The registration page must contain the required registration fields.
- The login page must contain email and password fields.
- The login page must provide a Forgot Password option.
- The password-reset interface must allow the user to set a new password.
- Google and GitHub sign-in options must be displayed.
- Passkey options must be displayed when the feature is available.
- The visual theme must use navy blue, black, and white.
- Forms must display validation errors and API response messages clearly.

## 5. Non-Functional Requirements

Non-functional requirements describe how the application should behave.

### 5.1 Security

- Passwords must never be stored in plain text.
- Password hashes must be generated using a suitable password-hashing library.
- Database credentials and application secrets must be stored in environment variables.
- HTTPS must be used in production.
- Backend request data must be validated.
- Sensitive information must not be exposed in error messages or logs.
- Authentication and password-reset flows must follow appropriate security practices.

### 5.2 Performance

- The application should respond to normal user requests efficiently.
- Database queries should be designed to avoid unnecessary operations.
- The application should return clear responses when requests fail.

### 5.3 Reliability

- The application should handle invalid input and expected errors without crashing.
- Database connection failures should be handled appropriately.
- The frontend should show useful messages when an API request fails.

### 5.4 Maintainability

- Frontend, backend, database, and tests must be organized into separate folders.
- API routes and business logic should be separated where practical.
- Code should use meaningful names and a consistent structure.
- Documentation must be updated as implementation decisions change.

### 5.5 Testability

- API endpoints must be testable through FastAPI's interactive documentation.
- Automated tests must verify important success and failure cases.
- Tests should use a separate test database or an isolated test setup.

## 6. Database Requirements

The application will use MySQL as its database.

The initial `users` table should store:

- User ID
- Full name
- Email address
- Password hash
- Account status
- Account creation timestamp

Additional tables may be introduced for:

- Password-reset tokens
- OAuth provider accounts
- Passkey credentials

**Database rules:**

- Each user must have a unique email address.
- Primary keys must uniquely identify records.
- Foreign keys must maintain relationships between related tables.
- Passwords must be stored as secure hashes.
- Password confirmation must not be stored.
- Only the data required by the application should be collected.

## 7. API Requirements

The backend must provide APIs for the application's authentication features.

Planned endpoints include:

| Endpoint | Method | Purpose |
|---|---|---|
| `/api/auth/register` | POST | Register a user |
| `/api/auth/login` | POST | Log in a user |
| `/api/auth/logout` | POST | Log out the current user |
| `/api/auth/me` | GET | Retrieve the current user's information |
| `/api/auth/forgot-password` | POST | Request a password-reset link |
| `/api/auth/reset-password` | POST | Reset the password |
| `/api/auth/google/login` | GET | Begin Google authentication |
| `/api/auth/github/login` | GET | Begin GitHub authentication |

Additional callback endpoints and passkey endpoints will be defined when those features are implemented.

The API documentation must describe each implemented endpoint, including its HTTP method, purpose, request data, response, status codes, and authentication requirements.

## 8. Frontend–Backend Integration Requirements

- The frontend must communicate with the FastAPI backend through HTTP requests.
- JavaScript should use the Fetch API to send requests and process responses.
- JSON should be used for request and response data where appropriate.
- The frontend must display success and error messages returned by the backend.
- CORS must be configured when the frontend and backend use different origins.
- The frontend must not connect directly to MySQL.
- Database credentials and backend secrets must never be included in frontend code.

## 9. Testing Requirements

The application must be tested for the following cases:

- Successful registration with valid information.
- Rejection of invalid registration data.
- Rejection of duplicate email addresses.
- Successful login with valid credentials.
- Rejection of incorrect login credentials.
- Successful logout.
- Rejection of unauthenticated access to protected endpoints.
- Password-reset requests and token validation.
- Expired and previously used password-reset tokens.
- Expected API status codes and error responses.
- Database connection and validation errors.

OAuth and passkey tests should be added as those features are implemented.

## 10. Project Folder Structure

The project will use the following structure:

```text
login-register-app/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── routes/
│   └── services/
│
├── database/
│   ├── connection.py
│   └── models.py
│
├── tests/
│   ├── test_register.py
│   ├── test_login.py
│   └── test_password_reset.py
│
├── docs/
│   ├── requirement.md
│   ├── architecture.md
│   ├── api-documentation.md
│   └── database-design.md
│
├── .env
├── .gitignore
└── README.md
```

Additional files and folders may be added as the project grows.

## 11. Implementation Plan

The application will be developed in the following order:

1. Set up the project folders and files.
2. Create the frontend registration and login forms.
3. Build the basic FastAPI application.
4. Connect the frontend to the backend.
5. Connect FastAPI to MySQL using SQLAlchemy.
6. Implement registration and test it.
7. Implement login and logout.
8. Implement password reset.
9. Add Google and GitHub sign-in.
10. Add passkey registration and authentication.
11. Expand automated test coverage.
12. Update documentation and prepare the application for deployment.

## 12. Acceptance Criteria

The project will be considered functionally complete when:

- Users can register with valid information.
- Duplicate email addresses are rejected.
- Passwords are securely hashed and stored.
- Users can log in and log out correctly.
- Password-reset requests and valid reset links work as expected.
- Implemented OAuth and passkey features work correctly.
- Invalid requests return appropriate errors.
- The frontend communicates correctly with FastAPI.
- Database operations work as expected.
- Automated tests cover the main authentication workflows.
- Documentation matches the implemented application.

## 13. Future Improvements

Possible future improvements include:

- Email verification during registration.
- Security notifications for account activity.
- Rate limiting for sensitive authentication endpoints.
- Password change functionality for authenticated users.
- Account recovery options.
- Additional integration and security tests.
- Production deployment and monitoring.
