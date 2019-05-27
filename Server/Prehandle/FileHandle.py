
#  Function for the pretreatment,input include the address prefix. address postfix,
#  the number of the files and the address of the list

def pretreatment(addpre, addpost, numOfFile, addlist):
    # The libraries that we need to import, nltk is a natural
    # language processing library. We use it to handle the texts.
    # math is the library for Calculation
    # sqlite3 is a library which provides the interfaces to the Database
    import nltk
    import math
    import sqlite3

    # Punctuation is a list created for handling punctuation, since it is useless
    Punctuation = list('''!@#$%^&*()_+-=[]\;',./{}|:"<>?''')

    # fileList is used to store the files
    fileList = []

    #the number of the files
    numberOfFiles = numOfFile
	
    # Range is a list used to execute loop
    Range = range(numberOfFiles)
	
    # Address prefix and postfix for files read
    addressPrefix = addpre
    addressPostfix = addpost
	
    for i in Range:
        # append files in the system to the list
        fileList.append(open(addressPrefix + str(i) + addressPostfix))

    # titleDic is used for recording titles for every document
    titleDic = {}
	
	# handle files based on their attributes
    for i in Range:
        temp = str(fileList[i].readline())

        while temp.replace(' ','') == '\n':
            temp = fileList[i].readline()
        if i < 38:
            length = len(temp) - 14
            titleDic[i] = temp[2:length]
        else :
            titleDic[i] = temp
    #    print(temp[:length])

    rawFileList = [fileList[i].read() for i in Range]
    # print(type(rawFileList[1]))
    tokensList = [nltk.word_tokenize(rawFileList[i]) for i in Range]
    # text which a list
    textList = [nltk.Text(tokensList[i]) for i in Range]
    # fdistList is a dictionary
    fdistList = [nltk.FreqDist(textList[i]) for i in Range]
    for i in Range:
        for punc in Punctuation:
            if punc in fdistList[i].keys():
                fdistList[i].pop(punc)

	# invertedFile is a dictionary, keys are words, values are list for corresponding documents
	invertedFile = {}
	
	# tf and idf are the values to describe importance for every word in a document
    tfFile = []
    idfFile = []
    testset = set()
	
	# generate the invertedFile
    for i in Range:
        for j in fdistList[i].keys():
            testset.add(j)
            if invertedFile.get(j) is None:
                invertedFile[j] = [str(i)]
            else:
                invertedFile[j].append(str(i))
				
	# generate the tfFile and the idfFile
    for i in Range:
        fileLength = len(textList[i])
        tfDic = {}
        idfDic = {}
	# tf = the times of a word occuring / the total length of the file
	# idf = log(the total number of the files / (1 + the number of the special files))
	
        for j in fdistList[i].keys():
            tfDic[j] = fdistList[i][j] / fileLength
            idfDic[j] = math.log(numberOfFiles / (1+len(invertedFile[j])))
        tfFile.append(tfDic)
        idfFile.append(idfDic)

    indexDic = {}
	
    # the address for the index list
    ListAddress = addlist
    file = open(ListAddress)
    for i in file.readlines():
        pair = i.split(':')
        sel = len(pair[1]) - 1
        url =  'shakespeare.mit.edu/' + ('Poetry/' if int(pair[0]) >= 42 else '') + pair[1][1:]
       # print(url)
        indexDic[int(pair[0])] = url

    # create the database
    # connect to the database and create the corresponding table
	
    conn = sqlite3.connect('PretreatmentInfo.db')

    print("Database created successfully")
    cursor = conn.cursor()
	
	# create the table for invertedFile
    cursor.execute('''create table InvertedFile
                      (WORD TEXT PRIMARY KEY  NOT NULL,
                        FileNumber   TEXT     NOT NULL
                      );''')

    print("Table created successfully")


    # create the table for file index
    for i in invertedFile.keys():
        stringi = " ".join(invertedFile[i])
        cursor.execute('''INSERT INTO InvertedFile (WORD, FileNumber)
                          VALUES (?,?)
                          ''',(i,stringi))

    cursor.execute('''create table tf_idf
                      (FileID         INT     NOT NULL,
                        WORD         TEXT     NOT NULL,
                        VALUE         REAL     NOT NULL
                      );''')

	# create the tf-idf table, FileID is represented for the ID of the file, WORD is
	# represented for the corresponding word. VALUE is represented for the tf-idf value 
    for i in Range:
        for j in fdistList[i].keys():
            value = tfFile[i][j] * idfFile[i][j]
            cursor.execute('''INSERT INTO tf_idf (FileID, WORD, VALUE)
                              VALUES (?,?,?)
                              ''', (i,j,value))


	# create the tf table, FileID is represented for the ID of the file, WORD is
	# represented for the corresponding word. VALUE is represented for the tf value 							  
    cursor.execute('''create table tf
                      (FileID         INT     NOT NULL,
                        WORD         TEXT     NOT NULL,
                        VALUE         REAL     NOT NULL
                      );''')

    for i in Range:
        for j in fdistList[i].keys():
            value = tfFile[i][j]
            cursor.execute('''INSERT INTO tf (FileID, WORD, VALUE)
                              VALUES (?,?,?)
                              ''', (i,j,value))

	# create the idf table, FileID is represented for the ID of the file, WORD is
	# represented for the corresponding word. VALUE is represented for the idf value 
    cursor.execute('''create table idf
                      (FileID         INT     NOT NULL,
                        WORD         TEXT     NOT NULL,
                        VALUE         REAL     NOT NULL
                      );''')

    for i in Range:
        for j in fdistList[i].keys():
            value = idfFile[i][j]
            cursor.execute('''INSERT INTO idf (FileID, WORD, VALUE)
                              VALUES (?,?,?)
                              ''', (i,j,value))

	# create index table for the file index
	# FileID: ID of the file
	# Title: Title of the file
	# URL: URL of the file
    cursor.execute('''create table urlTitleIndex
                    ( FileID INT    NOT NULL,
                      Title  TEXT   NOT NULL,
                      URL    TEXT   NOT NULL
                    );  ''')


    for i in Range:
        if i in titleDic.keys() and i in indexDic.keys():
            cursor.execute('''INSERT INTO urlTitleIndex (FileID,Title,URL)
                              VALUES (?,?,?)
                              ''', (int(i), titleDic[i],indexDic[i]))

	# commit the changes
	# close the database
    conn.commit()
    conn.close()

num = 195
import os
print(os.getcwd())
addr1 = '../Preparement/list.txt'
addr2 = '../Preparement/test'
addr3 = '.txt'

pretreatment(addr2, addr3, num, addr1)