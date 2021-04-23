# Bank security console


This is an internal repository for 'The Siyaniye' bank employees. You won't be able to run this 
repository if you accidentally get into it because you don't have an access to the database, 
however, you can use coding templates freely or look up how database requests are implemented.

Bank security console is a website which can be connected to the visits and staff passcards 
remote database.

_Script runs local web server interacting with remote database._



### How to install


You will need:

* [Python3](https://www.python.org/downloads/) 
* Then use [pip](https://pypi.org/project/pip/) (or pip3, if there is a conflict with Python2) 
to install dependencies
* a browser
* usege of the vertual environment is recommended


Well, you have to use terminal:


1. Clone the project repository to your local folder:

```
git clone https://Momotaro10000/Bank-security-console-Django-ORM-
```


2. Navigate to the project files folder:

```
cd project_name/
```


3. Create a vertual environment with required packages:

```
pip install pipenv
pipenv install -r requirements.txt
```


4. Activate vertual environment:

```
pipenv shell
```


### How to run the script


For the web site working locally you should assign environmental variables. [environs](https://pypi.org/project/environs/) library and .env file will help.

Create .env text file in project folder and fill like this:

```
HOST='hostname' # name of the database node
PORT='5434' # port number
DB_NAME='databasename' # name of the database
ORM_USER='username' # user name
PASSWORD='userpassword' # user password
SECRED_KEY='REPLACE_ME' # secret key
DEBUG=True # debug-status (True or False depends on your purposes, case doesn't relevant)
```

Run the script though the terminal.

In active vertual environment run:

```
python manage.py runserver 
```

Test version of the web site will be available [here](http://127.0.0.1:8000).



_The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/)._
_Settings needed for script correct running is provided by [Devman](https://dvmn.org/)._ 
