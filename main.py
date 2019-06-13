# -*- coding: utf-8 -*-
import argparse
from invertedIndex.InvertedIndex import get_invertedIndex, invertedindex
from invertedIndex.renameData import doc_id_mapping, get_doc_id_mapping
from vectorSpace.vectorSpace import VectorSpace

if __name__ == '__main__':
    # 初次运行需要
    parser = argparse.ArgumentParser(description='A simple search engine')
    parser.add_argument('--build', action="store_true", help='build or not', default=False)
    args = parser.parse_args()
    if args.build:
        doc_id_map = doc_id_mapping()
        dic = invertedindex(doc_id_map)
        vector_space = VectorSpace(dic, True)
    else:
        # 构建好vectorSpace和InvertedIndex
        doc_id_map = get_doc_id_mapping()
        dic = get_invertedIndex()
        vector_space = VectorSpace(dic, False)
    while True:
        target = input("> ")
        target = target.split(" ")
        vector_space.cal_k_relevant(5, target)
