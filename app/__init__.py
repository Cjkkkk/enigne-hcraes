import os
from flask import Flask
from app.routes.home import main
from invertedIndex.termGenerator import preprocessing
from invertedIndex.InvertedIndex import get_invertedIndex, invertedindex
from invertedIndex.renameData import get_doc_id_mapping, doc_id_mapping
from vectorSpace.vectorSpace import VectorSpace
from phraseQuery.phraseQuery import PhraseQuery
from boolquery.boolquery import BoolQuery
from spellingCorrection.spellingCorrection import SpellingCorrection


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
        doc_id_map = doc_id_mapping()
        dic = invertedindex(doc_id_map)
        vector_space = VectorSpace(dic, True)
    else:
        # 构建好vectorSpace和InvertedIndex
        doc_id_map = get_doc_id_mapping()
        dic = get_invertedIndex()
        vector_space = VectorSpace(dic, False)

    phrase_query = PhraseQuery(dic)
    bool_query = BoolQuery(dic)
    spelling_correction = SpellingCorrection(dic)
    app.vector_space = vector_space
    app.phrase_query = phrase_query
    app.bool_query = bool_query
    app.spelling_correction = spelling_correction
    app.doc_id_map = doc_id_map
    # register blueprints
    app.register_blueprint(main)

    return app
