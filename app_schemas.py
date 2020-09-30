from globals import marshmallow
from marshmallow import fields, post_load

class AppUserSchema(marshmallow.Schema):
    class Meta:
        fields = ("id", "full_name", "email")

app_user_schema = AppUserSchema()

#Show all users
app_users_schema = AppUserSchema(many=True)

