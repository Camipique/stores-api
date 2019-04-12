from flask_injector import inject
from stores.models.entities import Database
from pony.orm import db_session, ObjectNotFound


class UserService:
    @inject
    def __init__(self, db: Database):
        self.db = db

    @db_session
    def add_user(self, username, password):

        if self.db.model.User.select(lambda u: u.username == username):
            return {'message': "User '{}' is already in use.".format(username)}, 409

        self.db.model.User(
            username=username,
            password=password
        )

        return {'message': "User '{}' was successfully created.".format(username)}, 201

    @db_session
    def get_user_by_id(self, _id):

        try:
            user = self.db.model.User[_id]
        except:
            return {'message': "User with id: {} does not exist.".format(_id)}, 404

        return {'user': user.to_dict()}, 200

    @db_session
    def delete_user_by_id(self, _id):

        try:
            self.db.model.User[_id].delete()
        except ObjectNotFound:
            return {'message': "User with id: {} does not exist.".format(_id)}, 404

        return {'message': "User with id '{}' deleted".format(_id)}, 200

    @db_session
    def get_users(self):
        users = self.db.model.User.select()[:]  # select *
        result = [user.to_dict() for user in users]

        return result
