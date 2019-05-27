'''
file: cluster.py
description: script for generating the clusters of different documents.

'''


from sklearn.decomposition import PCA
from gensim import models
import numpy as np
import os
from gensim import corpora
from gensim import models
import pandas as pd
from sklearn.externals import joblib
from sklearn.cluster import KMeans
import pickle


# func: test whether the file is a test file.
def is_literature_file(file):
    if file[:4] == 'test':
        return file
    else:
        return None


if __name__ == '__main__':
    # set the path
    txt_dir = '../../preparement/'
    files = os.listdir(txt_dir)
    files = filter(is_literature_file,files)

    # load all the files we scrapy from web
    words = ''
    documents = []
    
    # load the machine learning model we have pretrained.
    # pca is the principle components analysis model
    # model is the Word2Vec model  
    model = models.Word2Vec.load('./model')
    pca = joblib.load('train_model90.m')

    # set stoplist set
    stoplist = set('for a of the and to in , .'.split())   
    all_clusters = {}
    for file in files:
        with open(txt_dir+file,'r') as f:
            document = f.read()
            texts = [model[word] for word in document.lower().split() if word not in stoplist] 
            texts = np.array(texts)        
            # use pca to transform the raw vectors
            texts = pca.transform(texts)

            # train KMeans model and get the clustering centers.
            clustering = KMeans()
            clustering.fit(texts)
            clusters = clustering.cluster_centers_
            clusters = pd.DataFrame(clusters)
            all_clusters[file] = clusters

    # save the clusters model by pickle.
    pickle.dump(all_clusters,open("clusters2.pickle", "wb"))


