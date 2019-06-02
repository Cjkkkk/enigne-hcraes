# -*- coding: utf-8 -*-
import pickle

forward_index = {}
inverted_index = {}


def forwardindex(filename, res):
    index = int(filename)
    forward_index[index] = {}
    for i, word in enumerate(res):
        if str(word) not in forward_index[index].keys():
            forward_index[index][str(word)] = [i]
        else:
            forward_index[index][str(word)].append(i)


"""
{word1:{docid1:pos1,pos2,...;docid2:pos1,pos2,...},word2:{}}
"""


def invertedindex():
    for docid, words in forward_index.items():
        for word in words.keys():
            if word not in inverted_index.keys():
                inverted_index[word] = {}
                inverted_index[word][docid] = words[word]
            elif docid not in inverted_index[word].keys():
                inverted_index[word][docid] = words[word]
    sorted(inverted_index.keys())
    dict2txt()


def dict2txt():
    pickle.dumps(inverted_index, open("InvertedIndex.p", "wb"))


def GetInvertedIndex():
    return pickle.load(open("InvertedIndex.p", "rb"))
