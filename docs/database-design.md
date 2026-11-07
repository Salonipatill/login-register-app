# Database Design

## 1. Introduction

This document describes how the database for the Login and Registration application is planned.

The application will use **MySQL** to store user account information. The FastAPI backend will communicate with MySQL using **SQLAlchemy**.

The database will support these features as they are implemented:

- User registration and login
- Password reset
- Google and GitHub sign-in
- Passkey authentication using WebAuthn

## 2. Database Overview

- **Database:** MySQL
- **Backend:** Python with FastAPI
- **Database toolkit:** SQLAlchemy
- **Purpose:** Store user accounts and authentication-related information

The database will be developed step by step. The first table will be `users`. Other tables can be added when their features are implemented.

## 3. Tables

### 3.1 `users`

**Purpose:** Stores information about registered users.

| Column | Suggested data type | Constraints | Purpose |
|---|---|---|---|
| `id` | INT | Primary key, auto-increment | Identifies each user |
| `full_name` | VARCHAR(100) | NOT NULL | Stores the user's full name |
| `email` | VARCHAR(255) | NOT NULL, UNIQUE | Stores the user's email address |
| `password_hash` | VARCHAR(255) | Nullable only if passwordless accounts are supported | Stores the securely hashed password |
| `is_active` | BOOLEAN | NOT NULL, default TRUE | Indicates whether the account is active |
| `created_at` | TIMESTAMP | Default current timestamp | Records when the account was created |

**Rules:**

- Each email address must be unique.
- Passwords must never be stored in plain text.
- Password confirmation is checked during registration but is not stored in the database.
- The `password_hash` column can be nullable if the application supports accounts created through OAuth or passkeys without a password.

### 3.2 `password_reset_tokens` — planned

**Purpose:** Stores information needed to validate password-reset requests.

| Column | Suggested data type | Purpose |
|---|---|---|
| `id` | INT, primary key | Identifies the token record |
| `user_id` | INT, foreign key to `users.id` | Identifies the associated user |
| `token_hash` | VARCHAR(255), unique | Stores a hash of the reset token |
| `expires_at` | DATETIME | Records when the token expires |
| `used_at` | DATETIME, nullable | Records when the token was used |
| `created_at` | TIMESTAMP | Records when the token was created |

Reset tokens should expire after a limited time and be usable only once. Store a hash of the token rather than the raw token whenever practical.

### 3.3 `oauth_accounts` — planned

**Purpose:** Links an application user to an external identity provider, such as Google or GitHub.

| Column | Suggested data type | Purpose |
|---|---|---|
| `id` | INT, primary key | Identifies the OAuth account record |
| `user_id` | INT, foreign key to `users.id` | Identifies the application user |
| `provider` | VARCHAR(50) | Stores the provider name, such as Google or GitHub |
| `provider_user_id` | VARCHAR(255) | Stores the user's identifier at that provider |
| `created_at` | TIMESTAMP | Records when the account was linked |

The combination of `provider` and `provider_user_id` should be unique. OAuth client secrets must be kept on the backend, not in frontend JavaScript.

### 3.4 `passkeys` — planned

**Purpose:** Stores credential information required for WebAuthn passkey authentication.

| Column | Suggested data type | Purpose |
|---|---|---|
| `id` | INT, primary key | Identifies the passkey record |
| `user_id` | INT, foreign key to `users.id` | Identifies the associated user |
| `credential_id` | Binary or text type, unique | Identifies the passkey credential |
| `public_key` | Binary type | Stores the public key used to verify authentication |
| `sign_count` | Suitable integer type | Stores the signature counter, where supported |
| `created_at` | TIMESTAMP | Records when the passkey was registered |
| `last_used_at` | DATETIME, nullable | Records the last successful use, if tracked |

A user may have multiple passkeys. Use a maintained WebAuthn library to confirm the required fields and appropriate data types. The application must not collect or store fingerprint or face scans.

## 4. Relationships

The planned relationships are:

- One user can have multiple password-reset token records over time.
- One user can link multiple OAuth accounts.
- One user can register multiple passkeys.

```text
users
  |--< password_reset_tokens
  |--< oauth_accounts
  `--< passkeys
```

`1-to-many` means one record in `users` may be associated with multiple records in the related table. A foreign key such as `user_id` connects the records.

## 5. Primary Keys, Foreign Keys, and Constraints

- **Primary key (PK):** Uniquely identifies a row, for example `users.id`.
- **Foreign key (FK):** Connects a row to another table, for example `password_reset_tokens.user_id` references `users.id`.
- **Unique constraint:** Prevents duplicate values, such as duplicate user email addresses.
- **NOT NULL:** Requires a value to be present.

The database should enforce important rules, including unique email addresses and valid foreign-key references. Index columns that are frequently searched or used to connect tables, where appropriate.

## 6. Security Considerations

- Store secure password hashes, never plain-text passwords.
- Store only a hash of password-reset tokens whenever practical.
- Keep database credentials in environment variables and exclude `.env` from version control.
- Do not put database credentials or OAuth client secrets in frontend code.
- Use SQLAlchemy's safe query mechanisms or parameterized queries.
- Restrict database access to authorized components and administrators.
- Use a separate test database or isolated setup for tests.
- Do not store biometric data for passkey authentication.

## 7. Database Connection

The database-related files are planned to have these responsibilities:

- `database/connection.py` — Configures the MySQL connection and database sessions.
- `database/models.py` — Defines tables using SQLAlchemy models.

The FastAPI backend will use this database layer to read and update records. The frontend must communicate with FastAPI; it must not connect directly to MySQL.

## 8. Implementation Plan

1. Create the MySQL database.
2. Create the initial `users` table.
3. Connect FastAPI to MySQL using SQLAlchemy.
4. Implement and test registration.
5. Implement and test login.
6. Add the password-reset table when password reset is implemented.
7. Add OAuth and passkey tables when those features are implemented.
8. Test constraints, relationships, and error cases.

## 9. Maintenance

This document describes the planned database design. Update it when tables, columns, data types, constraints, or relationships change. Keep it consistent with the actual SQLAlchemy models and database migrations.