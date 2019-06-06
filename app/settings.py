from dotenv import load_dotenv
load_dotenv(dotenv_path='.env', verbose=True)
# DB_HOST = os.getenv("DB_HOST")


class Config(object):
    pass


class ProdConfig(Config):
    ENV = 'prod'


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
