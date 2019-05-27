from preHandle.searchDemo import Search
from pySrc.rankDemo import Rank1
import pandas as pd
import pickle


# the search method, it consist search and rank two parts.
def search_engine(input):
    documents = Search(input)
    rankq = Rank1()

    # get clusters of documents selected
    documents = read_clusters(documents)
    # do rank
    documents = rankq.rank(documents, input)
    documents = list(documents)
    documents.reverse()
    return documents


# get clusters of documents selected from pretrained model.
def read_clusters(documents):
    # clusters = pd.read_csv('./pySrc/model/clusters.csv')
    clusters = pickle.load(open('./pySrc/model/clusters2.pickle', 'rb'))
    for document in documents:
        document.clusters = clusters['test' + str(document.name) + '.txt']
    return documents


if __name__ == '__main__':
    # test it.
    print(search_engine('lies got'))
