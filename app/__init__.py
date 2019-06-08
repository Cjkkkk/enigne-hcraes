import os
from flask import Flask
from app.routes.home import main
from invertedIndex.termGenerator import preprocessing
from invertedIndex.InvertedIndex import get_invertedIndex, invertedindex
from invertedIndex.renameData import rename
from vectorSpace.vectorSpace import VectorSpace
from PhraseQuery.PhraseQuery import PhraseQuery

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

    build = app.config['BUILD']
    if build:
        rename()
        preprocessing()
        dic = invertedindex()
        vector_space = VectorSpace(dic, True)
    else:
        # 构建好vectorSpace和InvertedIndex
        dic = get_invertedIndex()
        vector_space = VectorSpace(dic, False)
        phrase_query=PhraseQuery(dic)
    # register blueprints
    app.vector_space = vector_space
    app.phrase_query=phrase_query
    app.register_blueprint(main)

    return app
