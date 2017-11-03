<h1>Configure Django on Mac OS</h1>

<h2>Set up the virtual environment</h2>
First you need to have virtualenv installed: 

`pip install virtualenv

Go to your project folder and setup a new virtual environment.

`virtualenv env`

Next, activate the environment by typing: `source env/bin/activate`

You can deactivate it any time by typing: `deactivate`

Now you are ready to install python 3.6.

`brew install python3`

Install Django: `pip install django`
The current version is 1.11.7

Make sure your .gitignore file contains: `env/`

Run the server.

`python imageshop/manage.py runserver`