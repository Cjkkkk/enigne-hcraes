import pickle


class BoolQuery:
    inverted_index={}
    queryresult=[]
   
    def __init__(self, inverted_index):
        self.inverted_index = inverted_index

    def merge2_and(self, term1, term2):
        answer=[]
        if (term1 not in self.inverted_index) or (term2 not in self.inverted_index):
            return answer
        else:
            i = len(self.inverted_index[term1])
            j = len(self.inverted_index[term2])
            docIdx = list(self.inverted_index[term1].keys())
            docIdy = list(self.inverted_index[term2].keys())
            x = 0
            y = 0
            while x < i and y < j:
                if docIdx[x] == docIdy[y]:
                    answer.append(docIdx[x])
                    x += 1
                    y += 1
                elif docIdx[x] < docIdy[y]:
                    x += 1
                else:
                    y += 1
            return answer

    def merge2_or(self,term1, term2):
        if (term1 not in self.inverted_index) and (term2 not in self.inverted_index):
            answer = []
        elif term2 not in self.inverted_index:
            answer = list(self.inverted_index[term1].keys())
        elif term1 not in self.inverted_index:
            answer = list(self.inverted_index[term2].keys())
        else:
            answer = list(self.inverted_index[term2].keys())
            for item in list(self.inverted_index[term2].keys()):
                if item not in answer:
                    answer.append(item)
        return answer

    def merge2_not(self,term1, term2):
        answer = []
        if term1 not in self.inverted_index:
            return answer
        elif term2 not in self.inverted_index:
            answer = list(self.inverted_index[term1].keys())
            return answer
        else:
            answer = list(self.inverted_index[term1].keys())
            ans = []
            for item in answer:
                if item not in list(self.inverted_index[term2].keys()):
                    ans.append(item)
            return ans

    def merge3_and(self,term1, term2, term3):
        answer = []
        if term3 not in self.inverted_index:
            return answer
        else:
            answer = self.merge2_and(term1, term2)
            if answer == []:
                return answer
            ans = []
            docIdy = list(self.inverted_index[term3].keys())
            i = len(answer)
            j = len(docIdy)
            x = 0
            y = 0
            while x < i and y < j:
                if answer[x] == docIdy[y]:
                    ans.append(answer[x])
                    x += 1
                    y += 1
                elif answer[x] < docIdy[y]:
                    x += 1
                else:
                    y += 1
            ans.sort()
            return ans

    def merge3_or(self,term1, term2, term3):
        answer = self.merge2_or(term1, term2)
        docIdy = list(self.inverted_index[term3].keys())
        if term3 not in self.inverted_index:
            return answer
        else:
            if answer == []:
                answer = docIdy
            else:
                for item in docIdy:
                    if item not in answer:
                        answer.append(item)
            answer.sort()
            return answer

    def merge3_and_or(self,term1, term2, term3):
        answer = self.merge2_and(term1, term2)
        docIdy = list(self.inverted_index[term3].keys())
        if term3 not in self.inverted_index:
            return answer
        else:
            if answer == []:
                answer = docIdy
                return answer
            else:
                for item in docIdy:
                    if item not in answer:
                        answer.append(item)
                answer.sort()
                return answer

    def merge3_or_and(self,term1, term2, term3):
        answer = self.merge2_or(term1, term2)
        if (term3 not in self.inverted_index) or (answer == []):
            return answer
        else:
            ans = []
            i = len(answer)
            j = len(self.inverted_index[term3])
            x = 0
            y = 0
            docIdy = list(self.inverted_index[term3].keys())
            while x < i and y < j:
                if answer[x] == docIdy[y]:
                    ans.append(answer[x])
                    x += 1
                    y += 1
                elif answer[x] < docIdy[y]:
                    x += 1
                else:
                    y += 1
            ans.sort()
            return ans

    def search(self, word):
        terms = word
        if terms == []:
            return
        if len(terms) == 3:
            # A and B
            if terms[1] == "and":
                answer = self.merge2_and(terms[0], terms[2])
                self.queryresult=answer
            # A or B
            elif terms[1] == "or":
                answer = self.merge2_or(terms[0], terms[2])
                self.queryresult=answer
            # A not B
            elif terms[1] == "not":
                answer = self.merge2_not(terms[0], terms[2])
                self.queryresult=answer
            # 输入的三个词格式不对
            else:
                print("input wrong!")
            return
        elif len(terms) == 5:
            # A and B and C
            if (terms[1] == "and") and (terms[3] == "and"):
                answer = self.merge3_and(terms[0], terms[2], terms[4])
                self.queryresult=answer
            # A or B or C
            elif (terms[1] == "or") and (terms[3] == "or"):
                answer = self.merge3_or(terms[0], terms[2], terms[4])
                self.queryresult=answer
            # (A and B) or C
            elif (terms[1] == "and") and (terms[3] == "or"):
                answer = self.merge3_and_or(terms[0], terms[2], terms[4])
                self.queryresult=answer
            # (A or B) and C
            elif (terms[1] == "or") and (terms[3] == "and"):
                answer = self.merge3_or_and(terms[0], terms[2], terms[4])
                self.queryresult=answer
            else:
                print("More format is not supported now!")
            return
        else:
            print("More format is not supported now!")
            return

    def getqueryresult(self):
        return self.queryresult

'''
if __name__ == "__main__":
    words = ["COCOA","and","BAHIA"]
    dict= pickle.load(open("../InvertedIndex.p", "rb"))
    boolquery=BoolQuery(dict)
    boolquery.search(words)
    print(boolquery.getqueryresult()) #

'''
