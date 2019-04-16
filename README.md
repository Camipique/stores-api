# Stores API
This is an API built with Flask and Flask-RESTful for a simple online store.

The application uses FlaskInjector from Flask which means there is no need to use global objects, they will be searched or created when needed.

It also uses Pony ORM to manage and interact with the application database efficiently.

## Requirements
- Python3, install [here](https://www.python.org/downloads/)
- Virtual environments

## Setup
Install requirements
```
virtualenv --python=python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Install using windows cmd
```
virtualenv --python=python3 .venv
cd .venv/Scripts
activate
cd ..
cd ..
pip install -r requirements.txt
```

## Run
Make sure you are in the virtual environment and, in the stores folder, run
```
python app.py
```

### Database
Database is sqlite and will be stored in the data folder.

It has entities:
- User (id, username, password)
- Store (id, store_name, items)
- Item (id, name, price, store)
