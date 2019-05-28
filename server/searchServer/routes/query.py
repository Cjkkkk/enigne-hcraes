from flask import request
from searchServer import app
from searchServer.essentials import response
import main


@app.route('/query')
def query():
    input = request.args.get('key', '')
    print(input)
    res = main.search_engine(input)
    return response.JSON(res)
