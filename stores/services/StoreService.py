from flask_injector import inject
from stores.models.entities import Database
from pony.orm import db_session, ObjectNotFound


class StoreService:
    @inject
    def __init__(self, db: Database):
        self.db = db

    @db_session
    def add_store(self, store_name):

        if self.db.model.Store.select(lambda s: s.store_name == store_name):
            return {'message': "Store with name '{}' is already in use.".format(store_name)}, 409

        store_db = self.db.model.Store(
            store_name=store_name
        )

        return store_db.to_dict(), 201

    @db_session
    def delete_store_by_store_name(self, store_name):

        store = self.db.model.Store.select(lambda s: s.store_name == store_name)

        if store:
            if store.first().items:
                return {'message': "Store with name: '{}' has items in it.".format(store_name)}, 403

            store.delete()
            return {'message': "Store '{}' deleted".format(store_name)}, 200

        return {'message': "Store with name: '{}' does not exist.".format(store_name)}, 404

    @db_session
    def get_store_by_store_name(self, store_name):

        store = self.db.model.Store.select(lambda s: s.store_name == store_name).first()

        if store:
            return store.to_dict(), 200

        return {'message': "Store with name: '{}' does not exist.".format(store_name)}, 404

    @db_session
    def get_stores(self):
        stores = self.db.model.Store.select()[:]

        result = [store.to_dict() for store in stores]

        return result, 200

    @db_session
    def get_store_items(self, store_name):
        store = self.db.model.Store.select(lambda s: s.store_name == store_name).first()

        items = [item.to_dict() for item in store.items]

        return items, 200
