import os
from flask import Flask
from flask_restful import Api
from flask_injector import FlaskInjector, singleton
from stores.resources import API_HANDLERS
from stores.models.entities import Database
from stores.services import SERVICES

app = Flask(__name__)
api = Api(app=app)


for handler in API_HANDLERS:
    handler.decorators = handler.DECORATORS
    api.add_resource(handler, handler.ENDPOINT)


def configure(binder):
    PROVIDER = "sqlite"
    FILE_NAME = os.path.join("..", "..", "data", "database.sqlite")
    create_db = True

    args = {
        "provider": PROVIDER,
        "filename": FILE_NAME,
        "create_db": create_db
    }

    db = Database(**args)
    db.model.generate_mapping(create_tables=True)
    binder.bind(Database, to=db, scope=singleton)

    for service in SERVICES:
        binder.bind(service, scope=singleton)


injector = FlaskInjector(app=app, modules=[configure])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
