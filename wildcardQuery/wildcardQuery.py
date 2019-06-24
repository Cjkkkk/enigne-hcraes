# -*- coding: utf-8 -*-
import numpy as np
from functools import reduce
import re
import pickle

class WildcardQuery:
    inverted_index = {}
    matches=[]
    wildcardID=[]
    queryresult = []
    finalqueryresult = []

    def __init__(self,inverted_index):
        self.inverted_index=inverted_index

    def cal_WildcardQueryResult(self,words):
        self.queryresult = []
        self.finalqueryresult = []
        matchstr = "[a-zA-Z0-9-]+"
        lists = []
        listslength = []
        for id, word in enumerate(words):
            flag = word.find("*")
            if flag == -1:
                if word in self.inverted_index.keys():
                    lists.append(list(self.inverted_index[word].keys()))
                    listslength.append(len(list(self.inverted_index[word].keys())))
                else:  # 当有单词不存在时直接返回，可能之后需要与单词矫正进行整合
                    return
            elif flag != -1:
                self.wildcardID.append(id)
                word=word.replace("*", matchstr)
                word = word + "$"
                tmp=[]
                for checkword in self.inverted_index.keys():
                    if re.match(word,checkword):
                        tmp.append(checkword)
                if tmp:
                    self.matches.append(tmp)
                    print(tmp)
                else:
                    return

        if len(self.matches)==0:
            ascendingIndex = np.argsort(listslength).tolist()
            length = len(lists)
            if length == 0:
                return
            self.unionSet = lists[ascendingIndex[0]]
            if length > 1:
                for i, index in enumerate(ascendingIndex, 1):
                    self.unionSet = list(set(self.unionSet).intersection(set(lists[index])))
            if len(self.unionSet) > 0:
                for docid in self.unionSet:
                    self.search(words, 0, docid)
            self.finalqueryresult=self.queryresult

        elif len(self.matches)==1:
            for match in self.matches[0]:
                copylists = lists[:]
                copylistslength = listslength[:]
                # replace words to words without wildcard
                words[self.wildcardID[0]] = match
                copylists.append(list(self.inverted_index[match].keys()))
                copylistslength.append(len(list(self.inverted_index[match].keys())))
                length = len(copylists)
                if length == 0:
                    continue
                self.cal_subresult(words, copylists, copylistslength)
        else:
            permutations = reduce(lambda x, y: [i + "," + j for i in x for j in y], self.matches)
            for permutation in permutations:
                copylists = lists[:]
                copylistslength = listslength[:]
                # replace words to words without wildcard
                per = permutation.split(",")
                for i, id in enumerate(self.wildcardID):
                    words[id] = per[i]
                for p in per:
                    copylists.append(list(self.inverted_index[p].keys()))
                    copylistslength.append(len(list(self.inverted_index[p].keys())))
                length = len(copylists)
                if length == 0:
                    continue
                self.cal_subresult(words, copylists, copylistslength)

    def cal_subresult(self, words,copylists,copylistslength):
        ascendingIndex = np.argsort(copylistslength).tolist()
        self.unionSet = copylists[ascendingIndex[0]]
        length = len(copylists)
        if length > 1:
            for i, index in enumerate(ascendingIndex, 1):
                self.unionSet = list(set(self.unionSet).intersection(set(copylists[index])))  # 取交
        if len(self.unionSet) > 0:
            self.queryresult = []
            for docid in self.unionSet:
                self.search(words, 0, docid)
            if len(self.finalqueryresult) == 0:
                self.finalqueryresult = self.queryresult[:]
            else:
                self.finalqueryresult = list(set(self.finalqueryresult).union(set(self.queryresult)))  # 取并

    def getWildcardQueryResult(self):
        print(self.finalqueryresult)
        return self.finalqueryresult

    def search(self, words, wordsid, docid, nextposid=None):
        if wordsid == 0:
            for posid in self.inverted_index[words[wordsid]][docid]:
                self.search(words, wordsid + 1, docid, posid + 1)
        elif wordsid < len(words) - 1:
            if nextposid in self.inverted_index[words[wordsid]][docid]:
                self.search(words, wordsid + 1, docid, nextposid + 1)
            else:
                return
        elif wordsid == len(words) - 1:
            if nextposid in self.inverted_index[words[wordsid]][docid]:
                self.queryresult.append(docid)
            else:
                return
        elif wordsid == len(words):  # 当查询只有一个词时
            self.queryresult = self.unionSet
            return
        return



if __name__ == "__main__":

    #words=["*ased","on","preliminary","results"]
    words=["extra*","loss"]
    dict= pickle.load(open("../InvertedIndex.p", "rb"))
    wildcardquery=WildcardQuery(dict)
    wildcardquery.cal_WildcardQueryResult(words)
    doc_id_map = pickle.load(open("../doc_id_mapping.p", "rb"))
    for id in wildcardquery.getWildcardQueryResult():
        print(doc_id_map['id_to_doc'][id])
