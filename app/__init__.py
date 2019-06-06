import os
from flask import Flask
from app.routes.home import main


def create_app():
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/
    Arguments:
        object_name: the python path of the config object,
                     e.g. app.settings.ProdConfig
    """
    env = os.getenv('FLASK_ENV')
    if env == 'development':
        env = 'Dev'
    elif env == 'production':
        env = 'Prod'
    else:
        env = 'Test'

    app = Flask(__name__)

    app.config.from_object("app.settings.%sConfig" % env)

    # register blueprints
    app.register_blueprint(main)

    return app
