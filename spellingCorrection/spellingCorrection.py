import numpy as np
import pickle


class SpellingCorrection:
    inverted_index={}
    suggestion = []

    def __init__(self, inverted_index):
        self.inverted_index=inverted_index

    def edit_distance(self, w1, w2):
        l1,l2=len(w1)+1, len(w2)+1
        matrix = [[0 for j in range(l2)] for i in range(l1)]
        for i in range(l1):
            matrix[i][0]=i
        for j in range(l2):
            matrix[0][j]=j
        for i in range(1,l1):
            for j in range(1,l2):
                delta=0 if w1[i-1]==w2[j-1] else 1
                matrix[i][j]=min(matrix[i-1][j-1]+delta,
                                 matrix[i-1][j]+1,
                                 matrix[i][j-1]+1)
        return matrix[-1][-1]

    def correct(self, words):
        w1=words
        for i in range(len(w1)):
            min = 1000
            suggestion0 = ""
            if w1[i] in self.inverted_index:
                suggestion0=w1[i]
            else:
                for w2 in self.inverted_index:
                    dis=self.edit_distance(w1[i], w2)
                    if dis<min:
                        min=dis
                        suggestion0=w2
                    else:
                        continue
            self.suggestion.append(suggestion0)
        return

    def getcorrectionresult(self):
        return self.suggestion


if __name__=="__main__":
    words=["COCOC","BAHII","REVIEEW"]
    dict = pickle.load(open("../InvertedIndex.p", "rb"))
    sc=SpellingCorrection(dict)
    sc.correct(words)
    print(sc.getcorrectionresult())