from uuid import uuid4
from hashlib import md5, sha512
from SWSIdentity import db
from SWSIdentity.Models.domains import Domains
from SWSIdentity.Models.users import Users


class ControllerUsers(object):
    def get_by_email(self, email, domain=None):
        user = Users.query.filter_by(email=email).first()

        return {
            'id': user.id, 'email': user.email
        }

    def create(self, email, password, domain=None):
        """

        :param email:
        :param password:
        :param domain:
        :return:
        """
        salt = str(uuid4())
        user = Users()
        user.email = email
        user.password = self.hash(password, salt, 'sha512')
        user.salt = salt
        user.enabled = 1
        db.session.add(user)
        db.session.commit()
        return user.id

    def auth(self, email, password, domain='default'):
        """User auth method

        >>> ControllerUsers().auth("user@stackwebservices.com", "P@$$w0rd")
        True
        >>> ControllerUsers().auth("user@stackwebservices.com", "P@$$w0rd", "stackwebservices.com")
        False

        :return: boolean
        """
        domain = Domains.query.filter(Domains.name == domain.lower()).first()

        # TODO: ...
        # if not domain:
        #     return False

        # user = Users.query.filter(
        #     Users.email == email,
        #     # Users.password == self.hash(password)
        # )#.count() == 1

        print(email)
        user = Users.query.filter_by(email=email).first()
        if not user:
            return False
        # TODO: add domain
        if user.password == self.hash(password, user.salt, 'sha512'):
            return True

    @staticmethod
    def hash(password, salt='', algorithm='sha512'):
        """Hash string to md5 string


        >>> ControllerUsers.hash("example", "", "sha512")
        1a79a4d60de6718e8e5b326e338ae533

        >>> ControllerUsers.hash("example", "", "md5")
        1a79a4d60de6718e8e5b326e338ae533

        :return str
        """
        if algorithm == 'sha512':
            x = sha512('{}{}'.format(md5(password.encode()).hexdigest(), salt.encode()).encode()).hexdigest()
            print(x)
            return x
        elif algorithm == 'md5':
            return md5("{}".format(password.encode())).hexdigest()

    @classmethod
    def is_exists_email(cls, email, domain='default'):
        """Check exists email addres method

        >>> ControllerUsers.is_exists_email("user@stackwebservices.com")
        False
        >>> ControllerUsers.is_exists_email("user@stackwebservices.com", "stackwebservices.com")
        True

        :return boolean
        """
        if Users.query.filter(Users.email == email).count() == 0:
            return False
        return True
