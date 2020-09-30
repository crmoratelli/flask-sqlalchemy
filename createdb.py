from globals import database
from passlib.apps import custom_app_context as pwd_context
from db_models import *
import os

database.create_all()

"""
Populate the database with default user
"""
u = UserModel(
            full_name="Administrator",
            email="adm@business.com",
            passwd=pwd_context.hash("adm")
    )
    
database.session.add(u)
database.session.commit()

