'''
file: pca.py
description: script for determining the number of components we keep in PCA.

'''


from gensim import models
from sklearn.cluster import KMeans
import numpy as np
import os
from sklearn.externals import joblib
import pandas as pd

def is_literature_file(file):
    if file[:4] == 'test':
        return file
    else:
        return None

if __name__ == '__main__':
    # func: test whether the file is a test file.
    txt_dir = '../../preparement/'
    files = os.listdir(txt_dir)
    files = filter(is_literature_file,files)
    # print(list(files))
    words = ''
    documents = []
    model = models.Word2Vec.load('./model')
    print(len(model['you']))
    stoplist = set('for a of the and to in , .'.split())

    # load the machine learning model we have pretrained.
    # PCA is the PCA model  
    pca = joblib.load('train_model.m')

    # Calculate the coveriance matrix for the next step.
    cov = pd.DataFrame(pca.get_covariance())

     # Calculate the coveriance ratio.
    ratio = pca.explained_variance_ratio_
    sumk = []
    # Calculate k_sum(sum of first k elments)
    for i in range(len(ratio)):
        sumk.append(sum(ratio[0:i+1]))

        # make sure when the k_sum is more than 0.8 which means that it is enough
        if sum(ratio[0:i+1])>0.8:
            print(i)
            break
