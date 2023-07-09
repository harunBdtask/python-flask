import os

PRODUCTION = 'production'


class Config(object):
    DEBUG = False
    TESTING = False
    REDIS_HOST = os.getenv('redis_host')
    REDIS_PORT = os.getenv('redis_port')
    REDIS_PASSWORD = os.getenv('redis_password')
