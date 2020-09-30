from passlib.apps import custom_app_context as pwd_context
from globals import auth
from db_models import UserModel

@auth.verify_password
def verify_password(username, password):
    user = UserModel.query.filter_by(email = username).first()

    if user:
            return pwd_context.verify(password, user.passwd)

    return False


