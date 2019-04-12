import os
import unittest
from stores.services import SERVICES
from stores.services.ItemService import ItemService
from stores.models.entities import Database
from injector import Injector, singleton


class ItemsTest(unittest.TestCase):

    def setUp(self):

        def configure(binder):
            PROVIDER = "sqlite"
            FILE_NAME = os.path.join("..", "..", "data", "test-database.sqlite")
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

        self.injector = Injector(modules=[configure])

    def tearDown(self):
        db = self.injector.get(Database)
        db.model.drop_all_tables(with_all_data=True)

    def testDBIsAlright(self):
        db = self.injector.get(Database)
        self.assertIsNotNone(db)

    def testAddItemToDB(self):
        name = "car"
        price = 3500.00

        item_service = self.injector.get(ItemService)
        item = item_service.add_item(name, price)

        self.assertIsNotNone(item['id'])
        self.assertEqual(item['name'], name)
        self.assertEqual(item['price'], price)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ItemsTest)
    unittest.TextTestRunner().run(suite)
