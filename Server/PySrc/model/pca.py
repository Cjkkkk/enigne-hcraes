'''
file: pca.py
description: script for generating the model of principle components analysis.

'''
from sklearn.decomposition import PCA
from gensim import models
import numpy as np
import os
from gensim import corpora
from gensim import models
import pandas as pd
from sklearn.externals import joblib


# func: test whether the file is a test file.
def is_literature_file(file):
    if file[:4] == 'test':
        return file
    else:
        return None


if __name__ == '__main__':
    txt_dir = '../../Preparement/'
    files = os.listdir(txt_dir)
    files = filter(is_literature_file,files)
    # print(list(files))
    words = ''
    documents = []

    # load the machine learning model we have pretrained.
    # model is the Word2Vec model  
    model = models.Word2Vec.load('./model')
   
    # load all the files we scrapy from web
    for file in files:
        with open(txt_dir+file,'r') as f:
            document = f.read()
            words = words + document
            documents.append(document)

    # set stoplist set
    stoplist = set('for a of the and to in , .'.split())

    # split words
    texts = [word for word in words.lower().split() if word not in stoplist]
    texts = list(set(texts))
    vecs = []
    for text in texts:
        vecs.append(model[text])

    vecs = np.array(vecs)
    with open('./vecs.csv','w+') as f:
        vecs =pd.DataFrame(vecs)
        f.write(vecs.to_csv())
        
    # train PCA model, set n_components = 90
    pca = PCA(n_components=90)

    # use pca fit our vectors
    pca.fit(vecs)
    cov = pca.get_covariance() 

    # save the pca model
    joblib.dump(pca, "train_model90.m")
