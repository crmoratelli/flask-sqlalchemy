from globals import database

"""
User Database
"""
class UserModel(database.Model):
    __tablename__ = 'user'
    id = database.Column(database.Integer, primary_key=True)
    full_name = database.Column(database.String(64))
    passwd = database.Column(database.String(128))
    email = database.Column(database.String(64), unique=True)

