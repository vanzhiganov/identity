"""
Copyright (C) 2015, 2018 Stack Web Services LLC. All rights reserved.
"""
from hashlib import md5
from base64 import b64decode
import json
from functools import wraps
import jwt
from flask import redirect, url_for, session, current_app, request, g, make_response
from SWSIdentity.models.users import Users#, UsersSecrets
from SWSIdentity import redis
from SWSIdentity.statuses import get_status


def parse_authorization_string():
    """

    Example string
    X-Auth: basic cXdlOnF3ZQ==
    """
    __ = request.headers.get('X-Auth', "").split(' ')
    auth_type = 'token' if __[0].lower() == 'token' else 'basic'
    auth_creds = __[1] if len(__) == 2 else __[0]
    if auth_type == 'token':
        return auth_type, auth_creds
    else:
        creds = b64decode(auth_creds).decode().split(':')
        email = creds[0]
        password = md5(creds[1].encode()).hexdigest() if len(creds) > 1 else ''
        return auth_type, [email, password]


def requires_api_auth(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        auth_type, auth_creds = parse_authorization_string()
        if auth_type == 'token':
            # redis key
            redis_key = 'auth_key_{}'.format(auth_creds)
            account_id = redis.get(redis_key)
            if not account_id:
                return {
                    # "status": status.response(6)
                }
            user_data = Users.get_item_by_id(account_id)
        else:
            email = auth_creds[0]
            password = auth_creds[1]
            if not Users.auth(email, password, 1):
                return {
                    'status': {'code': 1, 'message': 'auth fails'}
                }
            user_data = Users.get_item_by_email(email)
        g.account = user_data
        if not g.account:
            return {
                'status': {'code': 1, 'message': 'auth fails'}
            }
        return func(*args, **kwargs)
    return decorated_function


def requires_login(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        # Check session
        required = ['email', 'password', 'user_id']
        success = True

        for item in required:
            if item in session and success:
                continue
            else:
                return redirect(url_for("account.logout"))

        if not Users.auth(session.get('email'), session.get('password'), 1):
            return redirect(url_for("account.logout"))
        return func(*args, **kwargs)
    return decorated_function


def requires_api_login(func):
    """
    TODO: add docstring
    """
    @wraps(func)
    def decorated_function(*args, **kwargs): # pylint: disable=missing-docstring
        # Check session
        required = ['email', 'password']
        success = True
        #print(request.json)

        for item in required:
            if item in session and success:
                continue
            else:
                return {
                    'status': {'code': 1, 'message': 'false'}
                }

        if not Users.auth(session.get('email'), session.get('password'), 1):
            return redirect(url_for("account.logout"))
        return func(*args, **kwargs)
    return decorated_function


def required_jwt_token(func):
    """decorator for JWT checking
    """
    @wraps(func)
    def decorated_function(*args, **kwargs): # pylint: disable=missing-docstring
        jwt_token = request.headers.get('X-Token')
        is_cookie = False
        if request.cookies.get('procdn.net'):
            is_cookie = True
            jwt_token = request.cookies.get('procdn.net')
        try:
            # extract jwt content
            content = jwt.decode(
                jwt_token,
                current_app.config['JWT_SECRET'],
                algorithm=current_app.config['JWT_ALGORITHM']
            )
        except Exception as error:
            current_app.logger.error(error)
            if is_cookie:
                resp = make_response(redirect(url_for('account.login')))
                resp.set_cookie('procdn.net', expires=0)
                return resp
            return {
                "status": get_status(7)
            }
        if not redis.get(content['token']):
            if is_cookie:
                resp = make_response(redirect(url_for('account.login')))
                resp.set_cookie('procdn.net', expires=0)
                return resp
            return get_status(7)
        g.token = content['token']
        g.account = json.loads(redis.get(g.token))
        expire = 3600
        redis.expire(g.token, expire)
        return func(*args, **kwargs)
    return decorated_function
