from hashlib import md5
from SWSIdentity import db
from SWSIdentity.models.domains import Domains
from SWSIdentity.models.users import Users


class ControllerUser(object):
    def auth(self, email, password, domain='default'):
        """User auth method

        >>> ControllersUser().auth("user@stackwebservices.com", "P@$$w0rd")
        True
        >>> ControllersUser().auth("user@stackwebservices.com", "P@$$w0rd", "stackwebservices.com")
        False

        :return: boolean
        """
        domain = Domains.query.filter(Domains.name == domain.lower()).first()

        if not domain:
            return False

        user = Users.query.filter(
            Users.email == email,
            Users.password == self.hash(password)
        ).count() == 1
    
        return True

    @staticmethod
    def hash(password):
        """Hash string to md5 string

        >>> ControllerUsers.hash("example")
        1a79a4d60de6718e8e5b326e338ae533

        :return str
        """
        return md5(password.encode()).hexdigest()

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
