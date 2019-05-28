from searchServer import app
from searchServer.essentials import response


@app.route('/test')
def test():
    return response.error(response.OK)
