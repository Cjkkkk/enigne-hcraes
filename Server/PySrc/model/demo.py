'''
file: demo.py
description: script for generating the model of words vectors.

'''

import os
from gensim import corpora
from gensim import models

# func: test whether the file is a test file.
def is_literature_file(file):
    if file[:4] == 'test':
        return file
    else:
        return None


if __name__ == '__main__':
    # set the path
    txt_dir = '../../Preparement/'
    files = os.listdir(txt_dir)
    files = filter(is_literature_file,files)

    # load all the files we scrapy from web
    words = ''
    documents = []
    for file in files:
        with open(txt_dir+file,'r') as f:
            document = f.read()
            words = words + document
            documents.append(document)

    # set stoplist set
    stoplist = set('for a of the and to in , .'.split())

    # split words
    texts2 = [[word for word in document.lower().split() if word not in stoplist] for document in documents]
    texts = [word for word in words.lower().split() if word not in stoplist]
    
    # train Word2Vec model
    model = models.Word2Vec(texts2,size=150,min_count=1,window=5,iter=100)
    
    # save model
    model.save('./model')
            