from flask import request
from flask_restful import Resource
from db_models import UserModel
from globals import database, FlaskAPI
from app_schemas import app_user_schema
from passlib.apps import custom_app_context as pwd_context




class RestAppUserRegister(Resource):


    def post(self):

        user = UserModel(
            full_name=request.json['full_name'],
            email=request.json['email'],
            passwd=pwd_context.hash(request.json['passwd']),
        )

        database.session.add(user)

        database.session.commit()

        return app_user_schema.dump(user)
    
FlaskAPI.add_resource(RestAppUserRegister, '/app/v0.1/user/register')