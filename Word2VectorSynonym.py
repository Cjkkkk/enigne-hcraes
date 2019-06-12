from gensim import models
from gensim import corpora
import os


def generate_word2vec_model(html_dir='',save_addr=''):
    files = os.listdir(html_dir)
    documents = []
    for file in files:
        with open(html_dir+os.sep+file,'r') as f:
            document = f.read()
            documents.append(document)

    stoplist = set('for a of the and to in , .'.split())

    texts2 = [[word for word in document.lower().split() if word not in stoplist] for document in documents]
    model = models.Word2Vec(texts2,size=150,min_count=1,window=5,iter=100)
    model.save(save_addr+'/model')

def inference(word='',model_dir='', topn = 3):
    model = models.Word2Vec.load(model_dir)
    res = model.most_similar(positive=[word], topn=topn)
    return map(lambda x:x[0],res)

if __name__ == '__main__':
    pass
