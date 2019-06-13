# -*- coding: utf-8 -*-
import pickle
import os
from invertedIndex.termGenerator import preprocessing
forward_index = {}
inverted_index = {}
dir_addr = 'data'


def forwardindex(filename, res, doc_id_map):
    index = doc_id_map['doc_to_id'][filename]
    forward_index[index] = {}
    for i, word in enumerate(res):
        if str(word) not in forward_index[index].keys():
            forward_index[index][str(word)] = [i]
        else:
            forward_index[index][str(word)].append(i)


"""
{word1:{docid1:pos1,pos2,...;docid2:pos1,pos2,...},word2:{}}
"""


def invertedindex(doc_id_map):
    file_list = os.listdir(dir_addr)
    file_list.sort(key=lambda x: int(x.split('.')[0]))
    for file_addr in file_list:
        res = preprocessing(dir_addr + '/' + file_addr)
        forwardindex(file_addr.split('.')[0], res, doc_id_map)
    for docid, words in forward_index.items():
        for word in words.keys():
            if word not in inverted_index.keys():
                inverted_index[word] = {}
                inverted_index[word][docid] = words[word]
            elif docid not in inverted_index[word].keys():
                inverted_index[word][docid] = words[word]
    sorted(inverted_index.keys())
    dict2txt()
    return inverted_index


def dict2txt():
    pickle.dump(inverted_index, open("InvertedIndex.p", "wb"))


def get_invertedIndex():
    return pickle.load(open("InvertedIndex.p", "rb"))
