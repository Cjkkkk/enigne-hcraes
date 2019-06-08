# -*- coding: utf-8 -*-
import numpy as np
import pickle

class PhraseQuery:
    inverted_index={}
    queryresult=[]
    unionSet=[]

    def __init__(self,inverted_index):
        self.inverted_index=inverted_index

    def cal_unionSet(self,words):
        lists = []
        listslength = []
        for word in words:
            if word in self.inverted_index.keys():
                lists.append(list(self.inverted_index[word].keys()))
                listslength.append(len(list(self.inverted_index[word].keys())))
            else:#当有单词不存在时直接返回，可能之后需要与单词矫正进行整合
                return

        ascendingIndex = np.argsort(listslength).tolist()
        length = len(lists)
        if length == 0:
            return
        self.unionSet = lists[ascendingIndex[0]]
        print()
        if length > 1:
            for i, index in enumerate(ascendingIndex, 1):
                self.unionSet = list(set(self.unionSet).intersection(set(lists[index])))

    def cal_PhraseQueryResult(self,words):
        self.cal_unionSet(words)
        if len(self.unionSet)>0:
            for docid in self.unionSet:
                self.search(words, 0, docid)
        else:
            print("Invalid Input!")

    def getPhraseQueryResult(self):
        return self.queryresult

    def search(self,words,wordsid,docid,nextposid=None):
        if wordsid==0:
            for posid in self.inverted_index[words[wordsid]][docid]:
                self.search(words, wordsid+1, docid, posid+1)
        elif wordsid<len(words)-1:
            if nextposid in self.inverted_index[words[wordsid]][docid]:
                self.search(words, wordsid + 1, docid, nextposid + 1)
            else:
                return
        elif wordsid==len(words)-1:
            if nextposid in self.inverted_index[words[wordsid]][docid]:
                self.queryresult.append(docid)
            else:
                return
        elif wordsid==len(words): #当查询只有一个词时
            self.queryresult=self.unionSet
            return
        return

#TEST

"""
if __name__ == "__main__":

    words=["Based","on","preliminary","results"]
    dict= pickle.load(open("../InvertedIndex.p", "rb"))
    phrasequery=PhraseQuery(dict)
    phrasequery.cal_PhraseQueryResult(words)
    print(phrasequery.getPhraseQueryResult()) #

"""
