import os
import math
import pickle
import numpy as np


class VectorSpace:
    wf = {}
    wf_norm = {}
    inverted_index = {}
    mapping = {}
    N = 0
    ''' 构造vector space
        :param inverted_index {} 倒排索引
        :param build bool 是否重新构建向量空间
    '''

    def __init__(self, inverted_index, build, N=None):
        self.inverted_index = inverted_index
        if N:
            self.N = N
        else:
            self.cal_N()
        if build:
            self.build_vector_space()
            self.cal_wf_norm()
            # self.build_term_to_id()
        else:
            self.load_vector_space()
            self.load_wf_norm()
            # self.load_term_to_id()

    ''' 从文件中加载vector space '''

    def load_vector_space(self):
        self.wf = pickle.load(open("VectorSpace.p", "rb"))

    ''' 计算文档数目 '''

    def cal_N(self):
        path = os.path.join(os.path.dirname(__file__), "../data")
        if not os.path.isdir(path):
            raise OSError("can not find directory {0}".format(path))
        self.N = len(os.listdir(path))

    def cal_df(self, inverted_index):
        df = {}
        for term in inverted_index:
            df[term] = len(inverted_index[term])
        return df

    def cal_idf(self, df, N):
        for term in df:
            df[term] = math.log(N / df[term], 10)
        return df

    def cal_tf(self, inverted_index, N):
        tf = {}
        for term in inverted_index:
            tf[term] = {}
            for doc_id in inverted_index[term]:
                tf[term][doc_id] = 1 + math.log(len(inverted_index[term][doc_id]), 10)
        return tf

    def cal_wf(self, idf, tf, N):
        self.wf = {}
        for i in range(N):
            self.wf[i] = {}
        for term in tf:
            for doc_id in tf[term]:
                self.wf[doc_id][term] = idf[term] * tf[term][doc_id]

    ''' 构建vector space并将结果存储在文件中 '''

    def build_vector_space(self):
        df = self.cal_df(self.inverted_index)
        idf = self.cal_idf(df, self.N)
        tf = self.cal_tf(self.inverted_index, self.N)
        self.cal_wf(idf, tf, self.N)
        with open("VectorSpace.p", "wb") as f:
            pickle.dump(self.wf, f)

    def cal_wf_norm(self):
        for doc_id in self.wf:
            sum = 0
            for term in self.wf[doc_id]:
                sum += self.wf[doc_id][term] ** 2
            self.wf_norm[doc_id] = math.sqrt(sum)
        with open("Wf_norm.p", "wb") as f:
            pickle.dump(self.wf_norm, f)

    def load_wf_norm(self):
        self.wf_norm = pickle.load(open("Wf_norm.p", "rb"))

    # def build_term_to_id(self):
    #     self.mapping = {}
    #     idx = 0
    #     for term in self.inverted_index:
    #         self.mapping[term] = idx
    #         idx += 1
    #     pickle.dump(self.mapping, open("TermMapping.p", "wb"))
    #
    # def load_term_to_id(self):
    #     self.mapping = pickle.load(open("TermMapping.p", "rb"))
    '''计算余弦'''

    def cal_cos(self, doc_id, vec):
        vec_norm = math.sqrt(len(vec))
        dot_product = 0
        for term in vec:
            if term in self.wf[doc_id]:
                dot_product += self.wf[doc_id][term]
        if self.wf_norm[doc_id] * vec_norm == 0:
            cos = 0
        else:
            cos = dot_product / (self.wf_norm[doc_id] * vec_norm)
        return cos

    ''' 返回top k最相关的文档索引 '''

    def cal_k_relevant(self, k, vec):
        cos = np.array([self.cal_cos(i, vec) for i in range(self.N)])
        idx = np.argpartition(cos, -k)[-k:]
        return idx[np.argsort(cos[idx])]
