from pony.orm import *
from pony.orm import Database as PonyDatabase


class Database:

    def __init__(self, **db_params):
        self.model = PonyDatabase(**db_params)

        class Item(self.model.Entity):
            id = PrimaryKey(int, auto=True)
            name = Required(str)
            price = Required(float)
            store = Required("Store")
            composite_key(id, store)

        class User(self.model.Entity):
            id = PrimaryKey(int, auto=True)
            username = Required(str, unique=True)
            password = Required(str)

        class Store(self.model.Entity):
            id = PrimaryKey(int, auto=True)
            store_name = Required(str, unique=True)
            items = Set("Item")
