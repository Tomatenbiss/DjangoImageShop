<h1>Configure Django on Mac OS</h1>

<h2>Set up the virtual environment</h2>
First you need to have virtualenv installed: 

`pip install virtualenv`

Go to your project folder and setup a new virtual environment.

`virtualenv env`

Next, activate the environment by typing: `source env/bin/activate`

You can deactivate it any time by typing: `deactivate`

Install Requirements: `pip install -r requirements.txt`

Make sure your .gitignore file contains: `env/`

Run the server.

`python imageshop/manage.py runserver`
