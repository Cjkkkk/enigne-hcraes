import gensim
import os
import collections
import smart_open
import random

id_dir = {}
counter = 0
def read_corpus(fname, tokens_only=False, tag_num=0):
    with smart_open.smart_open(fname) as f:
        document = f.read()
        if tokens_only:
            return (gensim.utils.simple_preprocess(document))
        else:
            return gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(document),[tag_num])

def generate_train_corpus(dir_addr):
    file_list = os.listdir(dir_addr)
    global counter
    res_corpus = []
    for file_addr in file_list:
        counter+=1
        id_dir[counter] = file_addr
        # print(file_addr)
        res_corpus.append(read_corpus(dir_addr+os.sep+file_addr,tag_num=counter))
    print(type(res_corpus), len(res_corpus))
    return res_corpus

def train_Doc2Vec_model(train_corpus, save_model=False, save_addr="model/"):
    model = gensim.models.doc2vec.Doc2Vec(vector_size=100, min_count=2,epochs=400)
    model.build_vocab(train_corpus)
    model.train(train_corpus, total_examples = model.corpus_count, epochs=model.epochs)
    if save_model==True:
        model.save(save_addr+"mymodel")
    return model

def handle_query(model, query_str):
    query_vector = model.infer_vector(query_str.split())
    sims = model.docvecs.most_similar([query_vector], topn=len(model.docvecs))
    rank = [sim for sim in sims]
    return rank[:10]

def test():
    tmp_model = gensim.models.Doc2Vec.load("model/mymodel")
    print(handle_query(tmp_model,"hello world"))

def main():
    addr = "./Reuters"
    train_Doc2Vec_model(generate_train_corpus(addr),save_model=True)

if __name__=='__main__':
    # read_corpus("./Reuters/1.html")
    # generate_train_corpus("./Reuters")
    # main()
    test()