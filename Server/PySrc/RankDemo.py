from PySrc.RankMethodBase import RankMethodBase
from gensim import models
from sklearn.externals import joblib
import numpy as np 
import pandas as pd
import sqlite3
import scipy.stats as stats


'''
class Rank1
    inherit: RankMethodBase
    description: our first rank method, maybe the last one before peer review
    method: rank: rank the documents inputed by the input string.
'''


class Rank1(RankMethodBase):
    def rank(self,documents,sentence):

        # load the machine learning model we have pretrained.
        # pca is the principle components analysis model
        # model is the Word2Vec model  
        pca = joblib.load('./PySrc/model/train_model90.m')
        model = models.Word2Vec.load('./PySrc/model/model')


        # parse our sentence, it will return sentence vectors and words list.
        sentence_vecs,words = parse_sentence(sentence,pca,model)
        rank_list = []

        # traversal all documents
        for document in documents:

            # get tf-idf list 
            idf_vec = get_tf_idf(document,words)
            rank = calculate_document_similarity(document.clusters,sentence_vecs,model,idf_vec)
            rank_list.append((document,rank))
        
        # sort the list
        rank_list = sorted(rank_list,key=lambda x:x[1])
        return rank_list


 # parse our sentence, it will return sentence vectors and words list.
def parse_sentence(sentence,pca,model):
    stoplist = set('for a of the and to in , .'.split())
    texts = [model[word] for word in sentence.lower().split() if word not in stoplist]
    words = [word for word in sentence.lower().split() if word not in stoplist]
    vec_list = []
    # texts = pd.DataFrame(texts)
    # vec_list = pca.transform(texts)
    for text in texts:
        text = np.reshape(text,(1,-1))
        vec = pca.transform(text)
        vec_list.append(vec)
    return np.array(vec_list),words



# calculate vector similarity by pearson.
def calculate_vector_similarity_by_cos(a,b):
    corr = stats.pearsonr(a,b)
    return corr


# calculate the similarity between a document and a sentence by calculating all clusters.
def calculate_document_similarity(clusters,sentence_vecs,model,idf_vec):
    rank_list = []
    for cluster in clusters.iterrows():
        cluster = cluster[1].values
        vec_similarity = []
        for vec in sentence_vecs:
            vec = vec[0]
            similarity = calculate_vector_similarity_by_cos(vec,cluster)
            vec_similarity.append(similarity)
        vec_similarity = np.array(vec_similarity)

        # vector multiply.
        vec_rank = np.dot(idf_vec,vec_similarity)
        rank_list.append(vec_rank)
    return np.max(rank_list)
            
# get tf-idf list from database.
def get_tf_idf(document,words):
    conn = sqlite3.connect('./Prehandle/PretreatmentInfo.db')
    cursor = conn.cursor()
    tf_idf_list = []
    for word in words:
        cursor.execute('''SELECT *
                          from tf
                          WHERE FileID = :document and WORD=:word 
                        ''',{'document':int(document.name),'word':word})
        tempResult = cursor.fetchall()
        if not tempResult :
            tf_idf_list.append(0)
        else:
            tf_idf_list.append(tempResult[0][2])
    return np.array(tf_idf_list)
        


