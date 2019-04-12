from flask_restful import Resource, reqparse
from flask_injector import inject
from stores.services.UserService import UserService


class Signup(Resource):

    DECORATORS = []
    ENDPOINT = "/signup"

    @inject
    def __init__(self, user_service: UserService):
        self.user_service = user_service

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True)
        self.reqparse.add_argument('password', type=str, required=True)

    def post(self):
        args = self.reqparse.parse_args()
        return self.user_service.add_user(args.username, args.password)


class Users(Resource):

    DECORATORS = []
    ENDPOINT = "/users"

    @inject
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get(self):
        return self.user_service.get_users()


class User(Resource):

    DECORATORS = []
    ENDPOINT = "/users/<int:_id>"

    @inject
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get(self, _id):
        return self.user_service.get_user_by_id(_id)

    def delete(self, _id):
        return self.user_service.delete_user_by_id(_id)
