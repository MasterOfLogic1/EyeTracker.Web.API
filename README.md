# EyeTracker.Web.API
EyeTracker.WebAPI is RESTful backend service tailored for eye tracking web applications. Built on the OpenAPI 3.0 specification, the API provides secure endpoints for user management—such as login, registration, and JWT-based authentication—ensuring that only authorized users can access its features. In addition to managing user accounts, the API specializes in handling flight instrumentation data, offering dedicated endpoints to create and retrieve real-time data for critical cockpit modules like ECAM, EFIS, and PFD.

This versatile API is designed to facilitate seamless communication between an  tracking application web and its data sources, making it an ideal solution for integrating high-fidelity eye tracking with advanced cockpit metrics. Whether you’re developing a flight simulation, monitoring pilot performance, or creating innovative aviation applications, EyeTracker.WebAPI provides a secure, scalable, and easy-to-use platform to power your data-driven insights

![image](https://github.com/user-attachments/assets/f42da3dc-caa3-4ed0-b56d-e8dc9b91cd92)


```markdown
# EyeTracker.WebAPI

**Version:** 1.0.0  
**Specification:** OpenAPI Specification (OAS) 3.0

EyeTracker.WebAPI is a RESTful API designed to serve data to an eye tracking application. It provides endpoints for user authentication, account management, and data operations for various modules including ECAM, EFIS, and PFD. The API is fully documented and includes a schema endpoint for easy integration.

---

## Table of Contents

- [Features](#features)
- [Installation & Setup](#installation--setup)
- [Endpoints](#endpoints)
  - [Authorization & Accounts](#authorization--accounts)
  - [Authentication (JWT Token Management)](#authentication-jwt-token-management)
  - [ECAM Data](#ecam-data)
  - [EFIS Data](#efis-data)
  - [PFD Data](#pfd-data)
  - [API Schema](#api-schema)
- [Schemas](#schemas)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **User Authorization:** Login and registration endpoints.
- **JWT Authentication:** Endpoints to obtain and refresh JWT tokens.
- **Data Operations:** Create and retrieve data for ECAM, EFIS, and PFD modules.
- **API Schema:** A dedicated endpoint to access the API schema and documentation.

---

## Installation & Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/EyeTracker.WebAPI.git
   cd EyeTracker.WebAPI
   ```

2. **Install Dependencies:**

   If using Python, ensure you have the necessary dependencies installed:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**

   Create and configure your environment file (e.g., `.env`) as required by the project.

4. **Run the API:**

   Depending on your setup, you can start the server with:

   ```bash
   python manage.py runserver
   ```

   or the relevant command for your framework.

---

## Endpoints

### Authorization & Accounts

- **Login**
  - **Method:** `POST`
  - **Endpoint:** `/api/accounts/login/`
  - **Description:** Authenticates a user with provided credentials.

- **Registration**
  - **Method:** `POST`
  - **Endpoint:** `/api/accounts/register/`
  - **Description:** Registers a new user account.

### Authentication (JWT Token Management)

- **Obtain JWT Token**
  - **Method:** `POST`
  - **Endpoint:** `/api/accounts/token/`
  - **Description:** Issues a JWT token upon successful authentication.

- **Refresh JWT Token**
  - **Method:** `POST`
  - **Endpoint:** `/api/accounts/token/refresh/`
  - **Description:** Refreshes an existing JWT token to extend the session.

### ECAM Data

- **Retrieve ECAM Data**
  - **Method:** `GET`
  - **Endpoint:** `/api/data/ecam/`
  - **Description:** Retrieves a list of ECAM data entries.

- **Create ECAM Data**
  - **Method:** `POST`
  - **Endpoint:** `/api/data/ecam/`
  - **Description:** Creates a new ECAM data entry.

### EFIS Data

- **Retrieve EFIS Data**
  - **Method:** `GET`
  - **Endpoint:** `/api/data/efis/`
  - **Description:** Retrieves a list of EFIS data entries.

- **Create EFIS Data**
  - **Method:** `POST`
  - **Endpoint:** `/api/data/efis/`
  - **Description:** Creates a new EFIS data entry.

### PFD Data

- **Retrieve PFD Data**
  - **Method:** `GET`
  - **Endpoint:** `/api/data/pfd/`
  - **Description:** Retrieves a list of PFD data entries.

- **Create PFD Data**
  - **Method:** `POST`
  - **Endpoint:** `/api/data/pfd/`
  - **Description:** Creates a new PFD data entry.

### API Schema

- **Retrieve API Schema**
  - **Method:** `GET`
  - **Endpoint:** `/api/schema/`
  - **Description:** Provides the full API schema and documentation.

---

## Schemas

The API uses the following schemas for its operations:

- **Ecam**
- **Efis**
- **Login**
- **MyTokenObtainPair**
- **Pfd**
- **Registeration**
- **TokenRefresh**

These schemas define the structure of requests and responses across the API endpoints.

---

## Usage Examples

### 1. User Login

```bash
curl -X POST http://localhost:8000/api/accounts/login/ \
     -H 'Content-Type: application/json' \
     -d '{"username": "your_username", "password": "your_password"}'
```

### 2. Obtain JWT Token

```bash
curl -X POST http://localhost:8000/api/accounts/token/ \
     -H 'Content-Type: application/json' \
     -d '{"username": "your_username", "password": "your_password"}'
```

### 3. Retrieve ECAM Data

```bash
curl -X GET http://localhost:8000/api/data/ecam/ \
     -H 'Authorization: Bearer <your_jwt_token>'
```

*Replace `<your_jwt_token>` with your actual JWT token.*

---

```
