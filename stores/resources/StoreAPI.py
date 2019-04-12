from flask_restful import Resource, reqparse
from flask_injector import inject
from stores.services.StoreService import StoreService


class Store(Resource):

    DECORATORS = []
    ENDPOINT = "/stores/<store_name>"

    @inject
    def __init__(self, store_service: StoreService):
        self.store_service = store_service

    def get(self, store_name):
        return self.store_service.get_store_by_store_name(store_name)

    def post(self, store_name):
        return self.store_service.add_store(store_name)

    def delete(self, store_name):
        return self.store_service.delete_store_by_store_name(store_name)


class StoreItems(Resource):

    DECORATORS = []
    ENDPOINT = "/stores/<store_name>/items"

    @inject
    def __init__(self, store_service: StoreService):
        self.store_service = store_service

    def get(self, store_name):
        return self.store_service.get_store_items(store_name)


class Stores(Resource):

    DECORATORS = []
    ENDPOINT = "/stores"

    @inject
    def __init__(self, store_service: StoreService):
        self.store_service = store_service

    def get(self):
        return self.store_service.get_stores()
