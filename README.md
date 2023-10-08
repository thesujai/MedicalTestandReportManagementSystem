# Medical Test and Report Management System

A Django-based web application for managing medical tests and reports.

## Description

This web application is designed to help medical facilities and professionals manage medical tests and their associated reports efficiently. It allows users to create, view, update, and delete medical tests and their reports, making the process of managing patient data and medical information more streamlined.

## Stacks

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap 4

### Backend
- Python
- Django
- SQLite (for development, you can switch to other databases for production)

## Running Locally

To run this project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/thesujai/MedicalTestandReportManagementSystem.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd MedicalTestandReportManagementSystem
    ```

3. **Install project dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py makemigrations
    ```
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (Admin account):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

    Access the application in your web browser:

    Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the application. You can log in using the superuser account created in step 5.


## Contributing

Contributions are welcome! If you'd like to contribute to this project.



## Acknowledgments

- Thanks to the Django and open-source community for providing excellent tools and resources.

Feel free to reach out if you have any questions or need further assistance with this project. Happy coding!
