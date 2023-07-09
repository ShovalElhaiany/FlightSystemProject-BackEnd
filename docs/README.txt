Sure! Here's the README file for your Flight System Project:

# Flight System Project

Flight System Project is a flight management system that allows airline companies to advertise flights and customers to choose the flight that suits them best at an attractive price. The system consists of a database, Business Logic layer, REST API interface, and a client-side (Front End) built in Flask.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

## Project Description

The Flight System Project is a comprehensive flight management system that enables airline companies to showcase their flights and customers to search and select flights based on their preferences. The system incorporates a database that includes tables for Airline Companies, Flights, Customers, Tickets, Countries, Administrators, Users, and User Roles. The system is built using Flask framework and follows a modular structure with various components such as API facades, blueprints, data folders, documentation, logs, routes, tests, src (source code), and lib (libraries).

## Features

- Registration and authentication for different types of users: Administrator, Airline Company, Customer, and Anonymous.
- CRUD operations for airline companies, flights, customers, tickets, countries, administrators, and users.
- Search functionality to retrieve flights based on various parameters.
- Ability to view arrival and departure flights for a specific country.
- Ticket management for customers.
- Logging system with different log levels.

## Installation

To set up the Flight System Project, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project folder: `cd Flight_System_Project`
3. Run the deployment script: `py src/deploy_env.py` (This will create a virtual environment and install the required dependencies)
4. Activate the virtual environment: `.venv/scripts/activate` (Windows) or `. .venv/bin/activate` (macOS/Linux)
5. Run the application: `python app.py`
   - On the first run, the script will create the database, insert data from the data folder, and set up the application.
   - On subsequent runs, the application will start.

## Usage

Once the Flight System Project is installed, you can access the system through the provided API endpoints. The project follows a specific flow, starting from an HTTP request from the user, which goes through the relevant facade based on the user type and permissions, then routes, views, business logic, and data access layer.

Refer to the project's source code and documentation for detailed information about the available endpoints, data models, and functionalities.

## Contact

If you have any questions, feedback, or issues regarding the Flight System Project, feel free to contact the project owner:

- Name: Shoval Elhaiany
- Phone Number: +972503413413
- Email: shoval.elhaiany@gmail.com

---

This concludes the README file for your Flight System Project. Make sure to update the contact information with your own details. Good luck with your project!