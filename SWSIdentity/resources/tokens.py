"""
Copyright (C) 2015, 2018 Stack Web Services LLC. All rights reserved.
"""
import json
from uuid import uuid4
import jwt
from flask import current_app, g, request
from flask_restful import Resource
from SWSIdentity.statuses import get_status
from SWSIdentity.Controllers.Users import ControllerUsers
from SWSIdentity.decorators import check_token, check_using_cookie
from SWSIdentity import redis


class ResourceTokens(Resource):
    """Token endpoint class"""
    method_decorators = {
        'post': [check_using_cookie],
        'get': [check_token],
        'delete': [check_token]
    }

    def post(self):
        """Create new token

        curl -X POST 'http://localhost:5000/api/identity/0.1/tokens/' \
        -d '{"email": "vanzhiganov@ya.ru", "password": "...", "domain": "stackwebservices.com"}' \
        -H 'Content-Type: application/json'
        """
        schema = {
            'type': 'object',
            'properties': {
                'email': {'type': 'string'},
                'password': {'type': 'string'},
                'domain': {'type': 'string'}
            },
            'required': [
                'email', 'password'
            ]
        }
        credentials = request.json

        print(credentials)

        email = credentials.get('email')
        password = credentials.get('password')

        if not ControllerUsers().auth(email, password, 'default'):
            return {
                'status': get_status(1)
            }
        user_data = ControllerUsers().get_by_email(email)

        expire = 3600
        token = str(uuid4())

        redis.set(token, json.dumps(user_data))
        redis.expire(token, expire)

        jwt_token = jwt.encode(
            {'token': token},
            current_app.config['JWT_SECRET'],
            algorithm=current_app.config['JWT_ALGORITHM']
        )
        if g.use_cookie:
            return {
                "status": get_status(0)
            }, 200, {'Set-Cookie': 'token={}'.format(token)}
        return {
            "response": {
                "token": jwt_token.decode()
            },
            "status": get_status(0)
        }

    def delete(self):
        """Revoke current token. Delete token from redis
        """
        redis.delete(g.token)

        return {
            # "status": status.response(0)
        }

    def get(self):
        """Выдаёт токен содержащийся в jwt указанному токену в GET параметре.
        
        curl 'http://localhost:5000/api/identity/0.1/tokens/?token=90EE868B-86A1-415B-A477-F5C0056D00F1'
        {
            "response": {
                "token": "..."
            }
        }

        Decorators:
            required_jwt_token
        """
        if not request.args.get('token'):
            return {"status": get_status(0)}
        # TODO: get 
        return {
            "response": {
                # "token": g.token
            },
            # "status": status.response(0)
        }