"""
Copyright (C) 2015, 2018 Stack Web Services LLC. All rights reserved.
"""
import os
import sys
try:
    import configparser
except:
    import ConfigParser as configparser

config_file = os.getenv('IDENTITY_CONFIG', '/etc/sws/identity/config.ini')

# setting file read
config = configparser.ConfigParser()
if os.path.exists(config_file):
    config.read(config_file)
else:
    sys.exit('config file not found IDENTITY_CONFIG: %s' % config_file)
