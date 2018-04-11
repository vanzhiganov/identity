"""
Copyright (C) 2015, 2018 Stack Web Services LLC. All rights reserved.
"""
from functools import wraps
import json
import jwt
from flask import current_app, request, g
from SWSIdentity import redis
from SWSIdentity.statuses import get_status


def check_using_cookie(func):
    @wraps(func)
    def sad(*args, **kwargs):
        current_app.logger.debug(request.headers.get('X-Set-Cookie', None))
        if request.headers.get('X-Set-Cookie', None):
            g.use_cookie = True
        else:
            g.use_cookie = False
        return func(*args)
    return sad


def check_token(func):
    @wraps(func)
    def sad(*args, **kwargs):
        if request.cookies.get('token') or request.headers.get('X-Token'):
            g.token = request.cookies.get('token') or request.headers.get('X-Token')
        else:
            return {
                "status": get_status(7)
            }
        token_data = redis.get(g.token)
        if not token_data:
            return {
                "status": get_status(7)
            }
        g.token_data = json.loads(token_data)

        redis.expire(g.token, current_app.config.get('TOKEN_TTL', 3600))

        current_app.logger.debug(g.token_data)

        # current_app.logger.debug(request.headers.get('X-Set-Cookie', None))
        # if request.headers.get('X-Set-Cookie', None):
        #     g.use_cookie = True
        # else:
        #     g.use_cookie = False
        return func(*args)
    return sad
