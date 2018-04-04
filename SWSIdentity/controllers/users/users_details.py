# # coding: utf-8
# """"""
# from peewee import CharField, IntegerField, ForeignKeyField
# from SWSCDNCore.database import DBModel
# from .users import Users


# class UsersDetails(DBModel):
#     user = ForeignKeyField(Users)
#     fname = CharField(null=True)
#     lname = CharField(null=True)
#     address = CharField(null=True)
#     city = CharField(null=True)
#     country = CharField(null=True)
#     state = CharField(null=True)
#     zipcode = IntegerField(null=True)

#     def __repr__(self):
#         return "<UsersDetails user={}>".format(self.user)

#     @classmethod
#     def is_exists_user(cls, user):
#         if cls.select().where(cls.user == user).count() == 1:
#             return True
#         return False

#     @classmethod
#     def get_item(cls, user):
#         return cls.select().where(cls.user == user).first()
