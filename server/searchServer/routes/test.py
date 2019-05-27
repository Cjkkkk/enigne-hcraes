from flask import request, session
from searchServer import app
from searchServer.ACEssentials import response


@app.route('/test')
def test():
    return response.error(response.OK)
