# Application Architecture

## 1. Introduction

This project is a login and registration web application that allows users to create accounts, sign in, and manage account access securely.

### Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, FastAPI
- **Database:** MySQL
- **Database Toolkit:** SQLAlchemy
- **Testing:** Pytest, FastAPI TestClient

Planned authentication features include email and password registration, login, password reset, Google and GitHub sign-in, and passkey authentication using WebAuthn. Features will be marked as implemented only after they have been developed and tested.

## 2. Architecture Overview

The application is divided into four main components: frontend, backend, database, and tests.

### System Architecture Diagram

```text
                    USER
                      |
                      v
              +------------------+
              |     FRONTEND     |
              |   HTML / CSS / JS|
              +------------------+
                      |
                HTTP Requests
                 JSON Data
                      |
                      v
              +------------------+
              |      BACKEND     |
              |      FastAPI     |
              | Routes + Services|
              +------------------+
                      |
               Database Operations
                      |
                      v
              +------------------+
              |     DATABASE     |
              |      MySQL       |
              +------------------+

              +------------------+
              |       TESTS      |
              | Pytest/TestClient|
              +------------------+
                      |
                 Test APIs
```

### How It Works

1. The frontend collects user input and displays responses.
2. JavaScript sends HTTP requests to the FastAPI backend.
3. FastAPI validates requests and processes application logic.
4. The backend communicates with MySQL when data needs to be retrieved or stored.
5. FastAPI returns a response to the frontend.
6. The frontend displays the appropriate success or error message.
7. Tests verify that the backend behaves as expected.

**Important:** The frontend must not connect directly to MySQL. Database credentials and database operations must remain on the backend side.

## 3. System Components

### 3.1 Frontend

**Location:** `frontend/`

```text
frontend/
├── index.html
├── style.css
└── script.js
```

Responsibilities:

- **`index.html`** defines the registration, login, and password-reset interfaces.
- **`style.css`** controls the layout, spacing, typography, and navy-blue, black, and white visual theme.
- **`script.js`** handles form interactions, basic client-side validation, API requests, and displaying success or error messages.

Client-side validation improves usability, but the backend must validate all submitted data as well.

### 3.2 Backend

**Location:** `backend/`

```text
backend/
├── main.py
├── config.py
├── routes/
└── services/
```

Responsibilities:

- **`main.py`** creates the FastAPI application and registers its routers.
- **`config.py`** loads application settings from environment variables.
- **`routes/`** defines API endpoints for registration, login, logout, and password reset.
- **`services/`** contains business logic, such as checking account rules, verifying passwords, and processing password-reset emails.

Routes coordinate requests and responses. Reusable business logic should live in services where practical.

### 3.3 Database

**Location:** `database/`

```text
database/
├── connection.py
└── models.py
```

Responsibilities:

- **`connection.py`** configures the connection to MySQL.
- **`models.py`** defines database tables using SQLAlchemy.

The database may store user IDs, full names, unique email addresses, password hashes, account status, and account creation timestamps.

Separate tables may be introduced for OAuth accounts, password-reset tokens, and passkey credentials as these features are implemented.

**Security requirement:** Passwords must never be stored as plain text. Only securely hashed passwords should be stored. Passkey implementations store credential information and public keys, not fingerprint or face data.

### 3.4 Tests

**Location:** `tests/`

Example structure:

```text
tests/
├── test_register.py
├── test_login.py
└── test_password_reset.py
```

Tests verify that the backend behaves correctly for valid and invalid requests.

Examples include:

- Successful user registration.
- Rejection of duplicate email addresses.
- Incorrect login credentials.
- Invalid password-reset tokens.
- Expired password-reset tokens.

Use Pytest and FastAPI TestClient for automated API tests.

Tests should use a separate test configuration or database so that they do not modify real user data.

## 4. Application Workflows

### 4.1 Registration Workflow

1. The user enters their full name, email, password, and password confirmation.
2. JavaScript performs basic validation.
3. The frontend sends the registration request to FastAPI.
4. FastAPI validates the request data.
5. The backend checks whether the email address is already registered.
6. The password is securely hashed.
7. The user record is saved in MySQL.
8. FastAPI returns an appropriate status code and response.
9. The frontend displays a success or error message.

Password confirmation is primarily a form-level check and does not need to be stored in the database.

### 4.2 Login Workflow

1. The user enters their email and password.
2. The frontend sends the credentials to the backend.
3. The backend looks up the account and verifies the submitted password against the stored password hash.
4. If authentication succeeds, the backend establishes the chosen authentication mechanism, such as a secure session cookie.
5. The backend returns a response.
6. The frontend displays the appropriate result.

Credentials must be transmitted over HTTPS in production. Login errors should be designed carefully to avoid unnecessarily revealing whether an email address has an account.

### 4.3 Password Reset Workflow

1. The user enters their email address to request a password reset.
2. The backend returns a generic response that does not disclose whether the account exists.
3. If the account is eligible, the backend generates a random, time-limited, single-use reset token.
4. The backend sends a password-reset link by email.
5. The user opens the link and submits a new password.
6. The backend validates the token and securely hashes the new password.
7. The database is updated, and the token is marked as used.

A hash of the reset token should be stored instead of the raw token whenever practical.

### 4.4 Google and GitHub Authentication

Google and GitHub sign-in will use their appropriate OAuth flows.

The backend will handle the necessary authentication callbacks and protect OAuth client secrets. The frontend will initiate the sign-in process and display the result.

These features are planned until their endpoints and tests are implemented.

### 4.5 Passkey Authentication

Passkey registration and login will use WebAuthn with a suitable library.

The device handles biometric verification locally. The application must not collect or store fingerprint or face scans.

The backend stores the required passkey credential information and public keys.

This feature is planned until it has been implemented and tested.

## 5. Database Architecture

MySQL is the persistent data store. The backend accesses it through the database connection and model layer.

### Initial Users Table

The `users` table is expected to contain the following fields:

| Field | Purpose |
|---|---|
| `id` | Unique user identifier |
| `full_name` | User's full name |
| `email` | Unique email address |
| `password_hash` | Securely hashed password |
| `is_active` | Indicates whether the account is active |
| `created_at` | Account creation timestamp |

The `password_hash` field may be nullable only if passwordless or OAuth-only accounts are intentionally supported.

Additional tables may be introduced for:

- Password-reset tokens.
- OAuth provider accounts.
- Passkey credentials.

Database constraints, including a unique constraint on email, should enforce important rules at the database level as well as in application code.

## 6. Security Architecture

The application should follow these security principles:

- Hash passwords using a modern password-hashing library.
- Validate request data on the backend, even when the frontend also validates it.
- Use HTTPS in production.
- Keep database credentials and secret keys in environment variables.
- Never commit real secrets to source control.
- Configure authentication cookies securely if cookie-based sessions are used.
- Apply suitable CSRF protections when required by the chosen authentication design.
- Make password-reset tokens random, short-lived, and single-use.
- Keep OAuth client secrets on the backend.
- Use a maintained WebAuthn library for passkeys.
- Avoid exposing passwords, tokens, secrets, or sensitive internal errors in API responses and logs.
- Configure CORS to allow only the frontend origins that need access.

The final authentication strategy, password-hashing library, and other security settings should be documented after they have been selected and implemented.

## 7. Frontend–Backend Communication

The frontend communicates with FastAPI through HTTP requests, typically sending and receiving JSON data.

For each endpoint, `api-documentation.md` should define:

- Endpoint path.
- HTTP method.
- Purpose.
- Required request data.
- Response format.
- Status codes.
- Authentication requirements.

During local development, the frontend and backend may run on different ports. If they have different origins, CORS must be configured in FastAPI.

In production, use HTTPS and configure the frontend's API base URL for the deployed environment.

The frontend must never contain database credentials, application secret keys, or OAuth client secrets.

## 8. Testing Architecture

Automated tests should cover:

- Valid and invalid registration requests.
- Duplicate email addresses.
- Successful and unsuccessful login attempts.
- Endpoints that require authentication.
- Password-reset requests and token validation.
- Input validation and expected error status codes.
- Database failures and other relevant edge cases.

Use a separate test database or isolated test setup.

Do not use real passwords, production secrets, or real user records in tests. Add tests for OAuth and passkeys when those flows are implemented.

## 9. Configuration and Deployment

Application configuration should be supplied through environment variables.

A local `.env` file may be used during development, but it must be excluded from version control through `.gitignore`.

A safe example configuration file, such as `.env.example`, may contain placeholder values without real credentials.

The frontend and FastAPI backend may be served separately, or FastAPI may be configured to serve the frontend. The chosen approach should be documented in the setup instructions.

Production deployment should use:

- HTTPS.
- Secure secrets management.
- Appropriate database access controls.
- Environment-specific configuration.
- Suitable error handling and logging.

## 10. Future Improvements

Possible future improvements include:

- Google and GitHub authentication.
- WebAuthn passkey registration and login.
- Email-based password reset.
- Account verification and security notifications.
- Rate limiting for sensitive authentication endpoints.
- Database migrations.
- Additional automated and integration tests.

Update this document whenever the actual architecture or an important implementation decision changes.