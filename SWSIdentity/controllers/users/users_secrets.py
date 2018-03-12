# coding: utf-8
# """"""
# from peewee import CharField, IntegerField, TextField, ForeignKeyField
# from SWSCDNCore.database import DBModel
# from .users import Users


# class UsersSecrets(DBModel):
#     """Users Secrets Model"""
#     user = ForeignKeyField(Users)
#     secret = CharField(unique=False, null=False)
#     acl = TextField()
#     status = IntegerField()

#     @classmethod
#     def get_user_secret(cls, email):
#         return cls.select().where(
#             cls.user << Users.select(Users.id).where(Users.email == email)
#         ).first()
