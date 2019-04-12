import os
import unittest
from stores.services import SERVICES
from stores.models.entities import Database
from stores.services.UserService import UserService, DuplicatedUserException
from injector import Injector, singleton


class UsersTest(unittest.TestCase):

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

    def testAddUserToDB(self):
        username = "camipique"
        password = "caLXMH57"

        user_service = self.injector.get(UserService)
        user = user_service.add_user(username, password)

        self.assertIsNotNone(user['id'])
        self.assertEqual(user['username'], username)
        self.assertEqual(user['password'], password)
        self.assertRaises(DuplicatedUserException, user_service.add_user, username, password)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(UsersTest)
    unittest.TextTestRunner().run(suite)
