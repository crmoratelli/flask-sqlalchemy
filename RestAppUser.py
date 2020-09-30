from flask import request
from flask_restful import Resource
from db_models import UserModel
from globals import database, FlaskAPI, auth
from app_schemas import app_users_schema
from passlib.apps import custom_app_context as pwd_context

class RestAppUser(Resource):

    def get_user(self):
        users = UserModel.query.all()
        return app_users_schema.dump(users)

    @auth.login_required()
    def get(self):
        return self.get_user()


    @auth.login_required()
    def put(self):
        user = UserModel.query.filter_by(id=request.json['id']).first()

        if user:    
            #The email is unique and cannot be changed.
            if 'full_name' in request.json:
                user.full_name = request.json['full_name']
            if 'passwd' in request.json:
                user.passwd = pwd_context.encrypt(request.json['passwd'])


            database.session.commit()

            return self.get_user()

        return app_users_schema.dump({})



FlaskAPI.add_resource(RestAppUser, '/app/v0.1/user')