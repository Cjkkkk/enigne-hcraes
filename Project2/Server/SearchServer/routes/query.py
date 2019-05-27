from flask import request
from SearchServer import app
from SearchServer.ACEssentials import response
import main

@app.route('/query')
def query():
    input = request.args.get('key', '')
    print(input)
    res = main.search_engine(input)
    return response.JSON(res)