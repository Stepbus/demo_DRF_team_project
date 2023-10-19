To run

    create and fill in the file ".env" according to the sample ".env.example"

    use the command "docker-compose up --build -d"

    Migrations will be applied, samples will be created from the "fixtures.json" file, and the project will be launched

* Database project: Postgres 

* To create an admin outside the terminal, the main page will offer to create an admin user
    
* Established permissions : IsAdminUser

Admin panel

    The administrative panel is powered by jazzmin
    Fields for search, sorting, and filtering added to the admin panel

API

    The models have a m2m relationships
    added url for instances for quick transition 
    additional information on the calculation of related parties has been added
    changed the name of some fields for better understanding of the logic
    added a custom validation for the fields in the models
    added default paginations

Admin users
    
    When entering the main page, a user registration window appears. After the user is successfully added, he or she is automatically logged in with the created account and redirected to the API page.
    It is possible to enter the data of an existing user.
    
    If the user is logged in, the "Log in" button on the main page changes to "To API" 
    You can unlog in on the API page in the admin panel

Swagger

    url "swagger/" will allow you to check the documentation based on swagger
