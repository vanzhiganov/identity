"""
Copyright (C) 2015, 2018 Stack Web Services LLC. All rights reserved.
"""
import json
from uuid import uuid4
import jwt
from flask import current_app, g, request
from flask_restful import Resource

from SWSIdentity.models.users import Users
from SWSIdentity.statuses import get_status
from SWSIdentity.decorators import required_jwt_token, requires_api_auth
from SWSIdentity import redis


class ResourceUsers(Resource):
    """Users endpoint class"""
    def post(self):
        """Create a new user
        curl -X POST 'http://rest-api.ru/api/identity/0.1/users/' \
        -H 'Content-Type: application/json' \
        -d '{"email": "vanzhiganov@ya.ru", "password": "...", "domain": "stackwebservices.com"}'
        """
        return {
            "status": {
                "code": 0,
                "message": "Success"
            }
        }
