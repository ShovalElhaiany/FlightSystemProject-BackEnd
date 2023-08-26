# Flight System Project - BackEnd

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Architecture](#architecture)
- [Installation and Activation](#installation-and-activation)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Project Description

The Flight System Project's backend is an exhaustive flight management system tailored to enable both airline companies and customers to interact in a seamless manner. This backend project is built using the Flask framework and integrates a well-defined database schema which encompasses tables for Airline Companies, Flights, Customers, Tickets, Countries, Administrators, Users, and User Roles.

---

## Features

- **User Authentication**: Supports various user types such as Administrator, Airline Company, Customer, and Anonymous.
- **CRUD Operations**: Full suite of Create, Read, Update, and Delete operations for managing airline companies, flights, customers, tickets, countries, administrators, and users.
- **Search Functionality**: Advanced search options to find flights based on a variety of parameters.
- **Country-Specific Info**: Enables viewing of arrival and departure flights for specific countries.
- **Ticket Management**: Integrated tools for ticket management by customers.
- **Logging System**: Comprehensive logging mechanisms with different log levels.

---

## Architecture

### Project Structure

The backend architecture consists of multiple layers and components designed for scalability and maintainability:

#### Routes

This directory is the entry point for all HTTP requests. The routing to appropriate views is performed based on the incoming requests.

#### Lib

Comprises three subfolders, each representing a different layer in the project:
  - **Views**: The topmost layer that receives requests from the routes, manipulates the requests, invokes functions from the data access layer, and returns the response.
  - **Business Logic Layer**: Also known as the middle layer, this is where the core data processing logic resides.
  - **Data Access Layer**: The bottom layer that interacts with the database by executing queries based on processed data.

#### BluePrints

Houses files that group URLs together.

#### Utils

A utility folder containing helper functions for data processing and user management.

#### Src

Contains configuration files, the main application creation file, and class definitions for imported libraries.

### Project Flow

The frontend interacts with the backend through API endpoints. The `api` folder contains facades files which act as gateways into the system:
- **base.py**: Houses basic functionalities accessible without restrictions.
- **anonymous.py**: Inherits from `base.py` and extends functionalities for unauthenticated users.
- **airline.py, administrator.py, customer.py**: These files inherit from `anonymous.py` and encapsulate the unique functionalities available to each user type.

Incoming requests are initially processed in the relevant facade and subsequently redirected to routes for further action.

---

## Installation and Activation

To set up and activate the project, follow the steps below:

1. Run the activation command `.\\run.ps1`. This PowerShell script automates the following sequence of commands:

    ```powershell
    .venv/scripts/activate              # Activate the virtual environment
    python.exe -m pip install --upgrade pip  # Update pip
    pip install -r requirements.txt     # Install dependencies
    ```

    **Environment Variables**:
    ```powershell
    $Env:FLASK_DB_HOST='localhost'
    $Env:MYSQL_NAME='flights_system_db'
    $Env:MYSQL_ROOT_PASSWORD='password'
    ```

    Finally, run `python app.py` to start the main application.

---

## Usage

After installing and activating the Flight System Project backend, you can interact with the system through various API endpoints. For more details, refer to the source code and the extensive documentation that accompanies the project.

---

## Acknowledgments

Special thanks to Danny Aram for imparting the essential skills and knowledge that contributed to the development of this backend project.

---

## Contact

For any queries, feedback, or issues related to the Flight System Project, please contact:

- **Name**: Shoval Elhaiany
- **Phone Number**: +972503413413
- **Email**: shoval.elhaiany@gmail.com