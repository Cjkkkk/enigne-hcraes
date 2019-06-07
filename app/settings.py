from dotenv import load_dotenv
load_dotenv(dotenv_path='.env', verbose=True)


class Config(object):
    BUILD = False


class ProdConfig(Config):
    ENV = 'prod'


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
