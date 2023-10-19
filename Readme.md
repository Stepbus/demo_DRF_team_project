Getting Started

To get the project up and running, follow these steps:

    create and fill in the file ".env" according to the sample ".env.example"

    use the command "docker-compose up --build -d"

    Migrations will be applied, samples will be created from the "fixtures.json" file, and the project will be launched

Requirements

    * Database: Postgres

Features

Admin Panel: 

    * The administrative panel is powered by jazzmin
    * Fields for search, sorting, and filtering added to the admin panel

API:

    * Models have m2m relationships.
    * URL for instances for quick transition.
    * Additional information on the calculation of related parties.
    * Custom validation for model fields.
    * Default pagination implemented.

Permissions:
    
    * Uses IsAdminUser for access control.

User Authentication:

    * The main page offers an admin user creation outside the terminal.
    * A login window appears upon entering the main page. Successful registration automatically logs the user in and redirects to the API page.
    * Option to login with an existing user.
    * "Log in" button on the main page changes to "To API" if the user is logged in.
    * Logout option available in the admin panel on the API page.

Documentation:

    * Swagger documentation is available at swagger/ URL.
