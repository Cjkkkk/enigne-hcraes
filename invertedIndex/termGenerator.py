# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import stopwords

counter = 0
content = 0
Punctuation = list('''!@#$%^&*()_+-=[]\;',./{}|:"<>?''')
stopword_list = stopwords.words('english')


def preprocessing(filename, stemming='False'):
    with open(filename) as f:
        res = handle_file(f, content)
        if res:
            for symbol in Punctuation:
                try:
                    while True:
                        res.remove(symbol)
                except ValueError:
                    pass
            return res
        else:
            return None
        
        # 短语检索是否需要去除停用词？
        """
        for stop_word in stopword_list:
            try:
                while True:
                    res.remove(stop_word)
            except ValueError:
                pass
        """
        


def handle_file(f, content):
    global counter
    counter += 1
    try:
        content = f.read()
    except UnicodeDecodeError:
        print(counter)
    if content:
        return nltk.word_tokenize(content)
    else:
        return None
