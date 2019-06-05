from InvertedIndex import GetInvertedIndex
from collections import defaultdict
import sys

"""
{word1:{docid1:pos1,pos2,...;docid2:pos1,pos2,...},word2:{}}
"""
InvertedIndex = defaultdict(dict)


def merge2_and(term1, term2):
    global InvertedIndex
    answer = []
    if (term1 not in InvertedIndex) or (term2 not in InvertedIndex):
        return answer
    else:
        i = len(InvertedIndex[term1])
        j = len(InvertedIndex[term2])
        docIdx = list(InvertedIndex[term1].keys())
        docIdy = list(InvertedIndex[term2].keys())
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


def merge2_or(term1, term2):
    if (term1 not in InvertedIndex) and (term2 not in InvertedIndex):
        answer = []
    elif term2 not in InvertedIndex:
        answer = list(InvertedIndex[term1].keys())
    elif term1 not in InvertedIndex:
        answer = list(InvertedIndex[term2].keys())
    else:
        answer = list(InvertedIndex[term2].keys())
        for item in list(InvertedIndex[term2].keys()):
            if item not in answer:
                answer.append(item)
    return answer


def merge2_not(term1, term2):
    answer = []
    if term1 not in InvertedIndex:
        return answer
    elif term2 not in InvertedIndex:
        answer = list(InvertedIndex[term1].keys())
        return answer
    else:
        answer = list(InvertedIndex[term1].keys())
        ans = []
        for item in answer:
            if item not in list(InvertedIndex[term2].keys()):
                ans.append(item)
        return ans


def merge3_and(term1, term2, term3):
    answer = []
    if term3 not in InvertedIndex:
        return answer
    else:
        answer = merge2_and(term1, term2)
        if answer == []:
            return answer
        ans = []
        docIdy = list(InvertedIndex[term3].keys())
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


def merge3_or(term1, term2, term3):
    answer = merge2_or(term1, term2)
    docIdy = list(InvertedIndex[term3].keys())
    if term3 not in InvertedIndex:
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


def merge3_and_or(term1, term2, term3):
    answer = merge2_and(term1, term2)
    docIdy = list(InvertedIndex[term3].keys())
    if term3 not in InvertedIndex:
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


def merge3_or_and(term1, term2, term3):
    answer = merge2_or(term1, term2)
    if (term3 not in InvertedIndex) or (answer == []):
        return answer
    else:
        ans = []
        i = len(answer)
        j = len(InvertedIndex[term3])
        x = 0
        y = 0
        docIdy = list(InvertedIndex[term3].keys())
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


def search():
    terms = input("Search query >> ").split()
    if terms == []:
        sys.exit()
    if len(terms) == 3:
        # A and B
        if terms[1] == "and":
            answer = merge2_and(terms[0], terms[2])
            print(answer)
        # A or B
        elif terms[1] == "or":
            answer = merge2_or(terms[0], terms[2])
            print(answer)
        # A not B
        elif terms[1] == "not":
            answer = merge2_not(terms[0], terms[2])
            print(answer)
        # 输入的三个词格式不对
        else:
            print("input wrong!")

    elif len(terms) == 5:
        # A and B and C
        if (terms[1] == "and") and (terms[3] == "and"):
            answer = merge3_and(terms[0], terms[2], terms[4])
            print(answer)
        # A or B or C
        elif (terms[1] == "or") and (terms[3] == "or"):
            answer = merge3_or(terms[0], terms[2], terms[4])
            print(answer)
        # (A and B) or C
        elif (terms[1] == "and") and (terms[3] == "or"):
            answer = merge3_and_or(terms[0], terms[2], terms[4])
            print(answer)
        # (A or B) and C
        elif (terms[1] == "or") and (terms[3] == "and"):
            answer = merge3_or_and(terms[0], terms[2], terms[4])
            print(answer)
        else:
            print("More format is not supported now!")
    else:
        print("More format is not supported now!")


def b_main():
    global InvertedIndex
    InvertedIndex = GetInvertedIndex(dict)
    while True:
        search()


'''
if __name__ == "__main__":
    b_main()
'''