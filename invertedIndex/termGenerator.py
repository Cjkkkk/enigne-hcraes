# -*- coding: utf-8 -*-
import nltk
import os
from nltk.corpus import stopwords
from invertedIndex.InvertedIndex import forwardindex

counter = 0
content = 0
stopword_list = stopwords.words('english')


def preprocessing(dir_addr='data', output_addr='result', stemming='False'):
    Punctuation = list('''!@#$%^&*()_+-=[]\;',./{}|:"<>?''')
    file_list = os.listdir(dir_addr)
    # order the file in acescend order
    file_list.sort(key=lambda x: int(x.split('.')[0]))
    for file_addr in file_list:
        with open(dir_addr + '/' + file_addr) as f, open(output_addr + '/' + file_addr.split('.')[0] + '.txt',
                                                         'w+') as f_out:
            res = handle_file(f, content)
            if res == None:
                continue
            for symbol in Punctuation:
                try:
                    while True:
                        res.remove(symbol)
                except ValueError:
                    pass
            # 短语检索是否需要去除停用词？
            """
            for stop_word in stopword_list:
                try:
                    while True:
                        res.remove(stop_word)
                except ValueError:
                    pass
            """
            f_out.write(str(res))
            # after thinking, I can only come up with the idea of putting this function here..
            forwardindex(file_addr.split('.')[0], res)


def handle_file(f, content):
    global counter
    counter += 1
    try:
        content = f.read()
        if counter < 5:
            print(content)
    except UnicodeDecodeError:
        print(counter)
    if content:
        return nltk.word_tokenize(content)
    else:
        return None
