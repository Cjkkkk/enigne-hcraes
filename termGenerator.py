import nltk
import os 
from nltk.corpus import stopwords

counter = 0
stopword_list = stopwords.words('english')
def preprocessing(dir_addr='./Reuters',output_addr='./Result',stemming='False'):
    Punctuation = list('''!@#$%^&*()_+-=[]\;',./{}|:"<>?''')
    file_list = os.listdir(dir_addr)
    for file_addr in file_list:
        with open(dir_addr + '/' + file_addr) as f, open(output_addr+'/'+file_addr.split('.')[0]+'.txt','w+') as f_out:
            res = handle_file(f)
            for symbol in Punctuation:
                try:
                    while True:
                        res.remove(symbol)
                except ValueError:
                    pass
            for stop_word in stopword_list:
                try:
                    while True:
                        res.remove(stop_word)
                except ValueError:
                    pass
            f_out.write(str(res))

def handle_file(f):
    global counter
    counter+=1
    try:
        content = f.read()
        if counter < 5:
            print(content)
    except UnicodeDecodeError:
        print(counter)
    return nltk.word_tokenize(content)

if __name__ == '__main__':
#    print(os.listdir('./Reuters'))
    preprocessing()
    print('counter =',counter)