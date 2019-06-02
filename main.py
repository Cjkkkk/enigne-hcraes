# -*- coding: utf-8 -*-

from invertedIndex.termGenerator import preprocessing
from invertedIndex.InvertedIndex import invertedindex, GetInvertedIndex
from vectorSpace.vectorSpace import *

if __name__ == '__main__':
    preprocessing()
    invertedindex()
    dict = {}
    dict = GetInvertedIndex(dict)
