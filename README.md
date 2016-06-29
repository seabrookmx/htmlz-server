# htmlz-server 
A simple web server for displaying EBooks exported as HTMLZ from Calibre. Inspired by the flask "flaskr" example.

## To run though the console, set up your virtualenv by running:
`python3 -m virtualenv venv` If your default installation of python is python3, then you can simply run `python -m virtualenv venv`

## Activate your virtualenv by running:
`source venv/bin/activate` This needs to be done in every new terminal where you plan to interact with Python

## Ensure you're running the right interpreter (this should return 3.x)
`python --version`

## Install dependencies:
`pip install -r requirements.txt`

## To configure the location of your HTMLZ archives:
export HTMLZ_REPO='/path/to/your/htmlz/files'

## To debug, run "ebook_server.py":
`python ebook_server.py`

## When running the application, you should be able to see your list of books:
`http://localhost:5000`

## Clicking on a the book in the above view, or going to:
`http://localhost:5000/Book%20Name` should take you to your book
