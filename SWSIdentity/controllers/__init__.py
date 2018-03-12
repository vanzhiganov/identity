
    # @classmethod
    # def auth(cls, email, password, status=1):
    #     """

    #     >>> Users.auth("email@yandex.ru", "example", 1)
    #     True

    #     :return boolean
    #     """
    #     password_hash = cls.hash_password(password)
    #     is_valid = cls.select().where(
    #         cls.email == email, cls.password == password_hash, cls.status == status).count()
    #     return False if is_valid == 0 else True

    # @classmethod
    # def is_exists_id(cls, user_id):
    #     """Check exists user ID method

    #     >>> Users.is_exists_id("6D7868D7-84EB-49E6-BA82-44D7891ECEB0")
    #     True

    #     :return boolean
    #     """
    #     if cls.select().where(cls.id == user_id).count() == 1:
    #         return True
    #     return False

    # @classmethod
    # def get_item_by_id(cls, user_id):
    #     """Get User details by user ID"""
    #     return cls.select().where(cls.id == user_id).first()

    # @classmethod
    # def get_item_by_email(cls, email):
    #     """Get User details by user ID"""
    #     return cls.select().where(cls.email == email).first()
