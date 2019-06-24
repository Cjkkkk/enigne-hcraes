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
    print(data)
    words_o = data.split(" ")
    current_app.spelling_correction.correct(words_o)  # 拼写矫正
    searchtype = int(request.args.get('searchtypeid'))
    if searchtype>=0 and searchtype<=2:
        words = current_app.spelling_correction.getcorrectionresult()#通配符不进行拼写矫正
    else:
        words=words_o[:]

    if searchtype == 0:  # 向量空间模型TopK查询
        idx = current_app.vector_space.cal_k_relevant(10, words).tolist()
    elif searchtype == 1:  # 布尔查询
        current_app.bool_query.search(words)
        idx = current_app.bool_query.getqueryresult()
    elif searchtype == 2:  # 短语查询
        current_app.phrase_query.cal_PhraseQueryResult(words)
        idx = current_app.phrase_query.getPhraseQueryResult()
    elif searchtype == 3:  # 通配符查询
        current_app.wildcard_query.cal_WildcardQueryResult(words_o)
        idx = current_app.wildcard_query.getWildcardQueryResult()

    # 读取文件
    root_dir = os.getcwd()
    content = []
    files = [current_app.doc_id_map['id_to_doc'][i] for i in idx]
    for file in files:
        with open(os.path.join(root_dir, 'data/{0}.html'.format(file)), "r") as f:
            content.append(f.read(200))

    return jsonify({"idx": files, 'content': content, 'words': words, 'words_o': words_o}), 200
