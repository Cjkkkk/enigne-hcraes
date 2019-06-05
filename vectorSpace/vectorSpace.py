import os
import math
import pickle


def build_vector_space(inverted_index):
    N = cal_N()
    df = cal_df(inverted_index)
    idf = cal_idf(df, N)
    tf = cal_tf(inverted_index, N)
    wf = cal_wf(idf, tf, N)
    pickle.dump(wf, open("VectorSpace.p", "wb"))
    return wf


def get_vector_space():
    return pickle.load(open("VectorSpace.p", "rb"))


def cal_N():
    path = os.path.join(os.path.dirname(__file__), "..\data")
    if not os.path.isdir(path):
        raise OSError("can not find directory {0}".format(path))
    files = os.listdir(path)
    return len(files)


def cal_df(inverted_index):
    df = {}
    for term in inverted_index:
        df[term] = len(inverted_index[term])
    return df


def cal_idf(df, N):
    for term in df:
        df[term] = math.log(N / df[term], 10)
    return df


def cal_tf(inverted_index, N):
    tf = {}
    for term in inverted_index:
        tf[term] = {}
        for doc_id in inverted_index[term]:
            tf[term][doc_id] = 1 + math.log(len(inverted_index[term][doc_id]), 10)
    return tf


def cal_wf(idf, tf, N):
    wf = {}
    for i in range(N):
        wf[i] = {}
    for term in tf:
        for doc_id in tf[term]:
            wf[doc_id][term] = idf[term] * tf[term][doc_id]
    return wf
