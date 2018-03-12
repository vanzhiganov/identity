import validators
from flask_script import Command, Option
# from SWSIdentity.models.admins import ControllerAdmins


class CommandAdminCreate(Command):
    """prints hello world"""
    option_list = (
        Option('--email', '-e', dest='email'),
        Option('--password', '-p', dest='password'),
    )

    def run(self, email, password):
        if not validators.email(email):
            return 'invalid email address'
        # if ControllerAdmins().is_exists_email(email):
        #     return 'email address already exists'
        # # admin_id = ControllerAdmins().create_admin(email, password, 1, 1)
        # if admin_id:
        #     return "ID: {}".format(admin_id)
        return False
