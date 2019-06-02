import nltk
import os 
from nltk.corpus import stopwords

counter = 0
stopword_list = stopwords.words('english')
def preprocessing(dir_addr='./Reuters',output_addr='./Result',stemming='False'):
    file_list = os.listdir(dir_addr)
    for file_addr in file_list:
        with open(output_addr+'/'+file_addr.split('.')[0]+'.txt','w+') as f_out:
            f_out.write(str(get_tokens_from_file(dir_addr + '/' + file_addr)))

def get_tokens_from_string(content):
    Punctuation = list('''!@#$%^&*()_+-=[]\;',./{}|:"<>?''')
    res = nltk.word_tokenize(content)
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
    return res 

def get_tokens_from_file(file_addr):
    with open(file_addr) as f:
        return get_tokens_from_string(handle_file(f))

def handle_file(f):
    # global counter
    # counter+=1
    try:
        content = f.read()
        # if counter < 5:
        #     print(content)
    except UnicodeDecodeError:
        print(content)
    return content

def test():
    print(get_tokens_from_string('jly jly dqwdh dwq dw q dwq'))
    print(get_tokens_from_file('./Reuters/1.html'))

if __name__ == '__main__':
    pass 
  #  test()
#    print(os.listdir('./Reuters'))
    #preprocessing()
    # print('counter =',counter)