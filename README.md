##########################
Contact Management System
##########################
Contact Management System is a software solution designed to efficiently organize and manage contact information, streamlining the storage and retrieval of names, phone numbers, emails, and addresses. Widely used in both professional and personal settings, it enhances communication efficiency by providing quick access to vital contact details.


Download and Setup
  1.Clone the Repository:
    git clone https://github.com/RumelNHORS/Contact-Management.git
  2.reate a Virtual Environment:
    python -m venv env
  3.Activate the Virtual Environment:
    For Windows:
      .\env\Scripts\activate
    For macOS/Linux:
      source env/bin/activate
  4.Install Dependencies:
    pip install -r requirements.txt

  This command installs the necessary dependencies listed in the requirements.txt file in your Python virtual environment.
  Make sure you have Python and pip installed on your system.

  5.Database Migrations:
    python manage.py makemigrations
    python manage.py migrate
  6.Run the Project:
    python manage.py runserver

    This command starts the development server. Open your web browser and go to http://127.0.0.1:8000/ to access the Contact Management System.
