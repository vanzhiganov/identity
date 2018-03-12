#!/usr/bin/env python
import os
# from SWSIdentity import init_app
import click

# os.set.environ('FLASK_APP', 'identity-manage')

# app = init_app()


@click.command()
def initdb():
    """Initialize the database."""
    click.echo('Init the db')

# initdb()