from flask import request, session
from SearchServer import app
from SearchServer.ACEssentials import response

@app.route('/test')
def test():

    return response.error(response.OK)