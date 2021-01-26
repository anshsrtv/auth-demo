# Auth Demo
## Setup and run
1. Clone this repository `git clone https://github.com/anshsrtv/auth-demo.git`
1. Enter the main directory `cd auth-demo/`
1. Create a virtual environment with Python3: `python3 -m venv env `. If you dont have `python3` yet then you can install it with:
    1. linux(ubuntu/debian) - `sudo apt install python3`
    1. windows - Download installer from https://www.python.org/downloads/release/python-370/.
1. Activate the virutal environment: `source env/bin/activate`
1. Install all the dependencies in `requirements.txt` file: `pip install -r requirements.txt`
1. Make Migrations if needed `python manage.py makemigrations`
1. Migrate the migrations: `python manage.py migrate`
1. Run the app: `python manage.py runserver`
1. Navigate to http://localhost:8000 in your browser
1. When you are done using the app, deactivate the virtual environment: `deactivate`

  
