from flask_injector import inject
from stores.models.entities import Database
from pony.orm import db_session


class ItemService:
    @inject
    def __init__(self, db: Database):
        self.db = db

    @db_session
    def add_item(self, name, price, store):

        store = self.db.model.Store[store]

        for item in store.items:
            if item.name == name:
                return {'message': "Item with name '{}' already exists in the store".format(name)}, 409

        item = self.db.model.Item(
            name=name,
            price=price,
            store=store
        )
        return item.to_dict(), 201

    @db_session
    def delete_item(self, name, store):

        item = self.db.model.Item.select(lambda i: i.name == name and i.store.id == store)

        if item:
            item.delete()
            return {'message': "Item '{}' deleted".format(name)}, 200

        return {'message': "Item with name: '{}' does not exist in the store.".format(name)}, 404

    @db_session
    def get_items(self):
        items = self.db.model.Item.select()[:]

        result = {'items': [item.to_dict() for item in items]}

        return result
