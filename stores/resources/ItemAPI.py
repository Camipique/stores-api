from flask_restful import Resource, reqparse
from flask_injector import inject
from stores.services.ItemService import ItemService


class Item(Resource):

    DECORATORS = []
    ENDPOINT = "/items/<name>"

    @inject
    def __init__(self, item_service: ItemService):
        self.item_service = item_service

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("store", type=int, required=True)

    def post(self, name):
        self.reqparse.add_argument("price", type=float, required=True)

        args = self.reqparse.parse_args()

        return self.item_service.add_item(name, args.price, args.store)

    def delete(self, name):
        args = self.reqparse.parse_args()

        return self.item_service.delete_item(name, args.store)


class Items(Resource):

    DECORATORS = []
    ENDPOINT = "/items"

    @inject
    def __init__(self, item_service: ItemService):
        self.item_service = item_service

    def get(self):
        return self.item_service.get_items()

