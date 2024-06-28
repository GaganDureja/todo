## About Project
This project made to simply perform crud operation on ToDo tasks.

## How to Run/Setup

Follow the below steps to run the project on your local computer:

1. Open Command Prompt/Terminal.
2. Check if Python is installed on your system by typing `python --version` or `python3 --version`.
3. If Python is not installed, download it from [here](https://www.python.org/downloads/).
4. Clone the project repository by typing the following command in the terminal:
`git clone git@github.com:GaganDureja/todo.git`
5. Navigate to the project directory. `cd todo`
6. Create a virtual environment to manage project dependencies Install and Run:
```bash
sudo apt install python3-venv
python3 -m venv env
```
7. Activate the virtual environment: `source env/bin/activate`
8. Install the project requirements by running: `pip install -r requirements.txt`
8. Apply migrations by running:
`python3 manage.py migrate`
10. After all installations are done, start the server by running:
 `python3 manage.py runserver`
11. You can test all the api links with your browser or some apps like postman.
  * Create and Retrieve Task [Open Link](http://127.0.0.1:8000/api/tasks)
  * Retrieve/Update/Delete Single Task: GET [Open Link](http://127.0.0.1:8000/api/tasks/1)
  * Due Today Tasks [Open Link](http://127.0.0.1:8000/api/tasks/due-today).

## Admin Panel
1. To log in as an admin, you need a superuser account. Stop the server by `Ctrl+C`.
2. Create a superuser by running:` python3 manage.py createsuperuser`
3. Provide the required information (username, email, password) as prompted.
```bash
Username: admin
Email: admin@mail.com
Password: admin@123
Password (again): admin@123
```
4. You can use the above credentials for testing/development purpose but for production I recommend to use strong credentials.
5. Once the superuser is created, start the server again by running:
`python3 manage.py runserver`
6. Access the Django admin panel [here](http://127.0.0.1:8000/admin) and log in using the superuser credentials.