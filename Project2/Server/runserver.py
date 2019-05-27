"""
This script runs the Server application using a development server.
"""

from os import environ
from SearchServer import app

#app.debug = True

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '23333'))
    except ValueError:
        PORT = 23333
    app.run(HOST, PORT)
