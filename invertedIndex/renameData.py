import os
import pickle

# Function to rename multiple files
def rename():
    i = 0
    path = os.path.join(os.path.dirname(__file__), "../data")
    if not os.path.isdir(path):
        raise OSError("can not find directory {0}".format(path))
    files = os.listdir(path)
    files.sort(key=lambda x: int(x.split(".")[0]))
    for filename in files:
        src = os.path.join(path, filename)
        dst = os.path.join(path, str(i) + ".html")
        os.rename(src, dst)
        i += 1


def doc_id_mapping():
    path = os.path.join(os.path.dirname(__file__), "../data")
    if not os.path.isdir(path):
        raise OSError("can not find directory {0}".format(path))
    files = os.listdir(path)
    mapping = {'id_to_doc': {}, 'doc_to_id': {}}
    i = 0
    for filename in files:
        mapping['id_to_doc'][i] = filename.split(".")[0]
        mapping['doc_to_id'][filename.split(".")[0]] = i
        i += 1
    with open("doc_id_mapping.p", "wb") as f:
        pickle.dump(mapping, f)
    return mapping


def get_doc_id_mapping():
    return pickle.load(open("doc_id_mapping.p", "rb"))
