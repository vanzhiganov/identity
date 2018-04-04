"""
Copyright (C) 2015, 2018 Stack Web Services LLC. All rights reserved.
"""
import os
import time

from flask import Flask, g, request
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_restful import Resource, Api
from raven.contrib.flask import Sentry

redis = FlaskRedis() # pylint: disable=invalid-name
db = SQLAlchemy() # pylint: disable=invalid-name


def init_app():
    """Init Application
    """
    from SWSIdentity import resources
    from SWSIdentity.config import config

    app = Flask(__name__)
    app.config['DEBUG'] = config.getboolean('main', 'debug')
    app.config['SECRET_KEY'] = config.get("main", "secret_key")

    app.config['JWT_SECRET'] = config.get('jwt', 'secret_key')
    app.config['JWT_ALGORITHM'] = config.get('jwt', 'algorithm')

    app.config['SQLALCHEMY_DATABASE_URI'] = config.get('database', 'uri')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['REDIS_URL'] = config.get('redis', 'url')

    db.init_app(app)
    redis.init_app(app)
    migrate = Migrate(app, db)

    if config.getboolean('sentry', 'enabled'):
        sentry = Sentry(app, dsn=config.get('sentry', 'dsn'))

    # RESTAPI
    api = Api(app)
    ## Tokens
    api.add_resource(resources.ResourceTokens, '/api/identity/0.1/tokens/')
    ## Domains
    # api.add_resource(resources.ResourceTokens, '/api/identity/0.1/domains/')
    # api.add_resource(resources.ResourceTokens, '/api/identity/0.1/domains/<int:domain_id>')
    ## Projects
    # api.add_resource(resources.ResourceTokens, '/api/identity/0.1/projects/')
    # api.add_resource(resources.ResourceTokens, '/api/identity/0.1/projects/<int:project_id>')
    ## Groups
    # api.add_resource(resources.ResourceTokens, '/api/identity/0.1/groups/')
    # api.add_resource(resources.ResourceTokens, '/api/identity/0.1/groups/<int:group_id>')
    # api.add_resource(resources.ResourceTokens, '/api/identity/0.1/groups/<int:group_id>/users/')
    # api.add_resource(
    #     resources.ResourceTokens, '/api/identity/0.1/groups/<int:group_id>/users/<int:user_id>')
    # Users
    api.add_resource(resources.ResourceUsers, '/api/identity/0.1/users/')
    # api.add_resource(resources.ResourceTokens, '/api/identity/0.1/users/<int:user_id>')
    # api.add_resource(resources.ResourceTokens, '/api/identity/0.1/users/<int:user_id>/groups')
    # api.add_resource(resources.ResourceTokens, '/api/identity/0.1/users/<int:user_id>/projects')
    # api.add_resource(resources.ResourceTokens, '/api/identity/0.1/users/<int:user_id>/password')

    return app


def init_celery():
    """Init Celery"""
    return


def init_manager():
    """Init manager"""
    from SWSIdentity.commands import CommandAdminCreate
    from SWSIdentity.config import config
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.get('database', 'uri')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['REDIS_URL'] = config.get('redis', 'url')

    db.init_app(app)
    migrate = Migrate(app, db)
    manager = Manager(app)

    manager.add_command('db', MigrateCommand)
    manager.add_command('admin_create', CommandAdminCreate)

    return manager
