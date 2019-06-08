from flask import Blueprint, render_template, send_from_directory, current_app, request, jsonify
import os

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def home():
    # current_app.logger.info()
    return render_template("index.html")


@main.route('/data/<path:filename>', methods=['GET'])
def download_file(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, 'data'), filename)


@main.route('/search', methods=['GET'])
def search():
    return render_template("search.html")


@main.route('/search_', methods=['GET'])
def search_():

    data = request.args.get('key')
    words = data.split(" ")

    searchtype=int(request.args.get('searchtypeid'))
    if searchtype==0:#向量空间模型TopK查询
        idx = current_app.vector_space.cal_k_relevant(10, words).tolist()
    elif searchtype==1:#布尔查询 未完
        idx = current_app.vector_space.cal_k_relevant(10, words)
    elif searchtype==2:#短语查询
        current_app.phrase_query.cal_PhraseQueryResult(words)
        idx=current_app.phrase_query.getPhraseQueryResult()

    # 读取文件
    root_dir = os.getcwd()
    content = []
    for i in idx:
        with open(os.path.join(root_dir, 'data/{0}.html'.format(i)), "r") as f:
            content.append(f.read(200))
    return jsonify({"idx": idx, 'content': content}), 200
