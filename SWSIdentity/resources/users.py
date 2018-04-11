"""
Copyright (C) 2015, 2018 Stack Web Services LLC. All rights reserved.
"""
from flask import request
from flask_restful import Resource
from SWSIdentity.statuses import get_status
from SWSIdentity.Controllers.Users import ControllerUsers


class ResourceUsers(Resource):
    """Users endpoint class"""
    def post(self):
        """Create a new user

        curl -X POST 'http://rest-api.ru/api/identity/0.1/users/' \
        -H 'Content-Type: application/json' \
        -d '{
            "email": "vanzhiganov@ya.ru",
            "password": "...",
            "domain": "stackwebservices.com"
        }'
        """
        email = request.json.get('email')
        password = request.json.get('password')
        domain = request.json.get('domain', 'default')

        if ControllerUsers().is_exists_email(email, domain):
            return {
                "status": get_status(2)
            }

        ControllerUsers().create(email, password, domain)

        return {
            "status": get_status(0)
        }
