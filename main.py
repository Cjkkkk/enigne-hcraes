# -*- coding: utf-8 -*-
import sys
from invertedIndex.termGenerator import preprocessing
from invertedIndex.InvertedIndex import get_invertedIndex, invertedindex
from invertedIndex.renameData import rename
# from boolquery.boolquery import *
from vectorSpace.vectorSpace import build_vector_space, get_vector_space

if __name__ == '__main__':
    # 初次运行需要
    rename()
    preprocessing()
    dic = invertedindex()
    wf = build_vector_space(dic)

    # 构建好vectorSpace和InvertedIndex
    dic = get_invertedIndex()
    wf = get_vector_space()
