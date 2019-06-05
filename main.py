# -*- coding: utf-8 -*-
import sys
import argparse
from invertedIndex.termGenerator import preprocessing
from invertedIndex.InvertedIndex import get_invertedIndex, invertedindex
from invertedIndex.renameData import rename
# from boolquery.boolquery import *
from vectorSpace.vectorSpace import build_vector_space, get_vector_space

if __name__ == '__main__':
    # 初次运行需要
    parser = argparse.ArgumentParser(description='A simple search engine')
    parser.add_argument('--build', action="store_true", help='build or not', default=False)
    args = parser.parse_args()
    if args.build:
        rename()
        preprocessing()
        dic = invertedindex()
        wf = build_vector_space(dic)
    else:
        # 构建好vectorSpace和InvertedIndex
        dic = get_invertedIndex()
        wf = get_vector_space()
    while 1:
        target = input("> ")
