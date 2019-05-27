import sqlite3
from PySrc.Document import Document


# the function for searching. Input is a string and output is a list
# and every element in the list is a tuple with three attributes:
# FileID,URL and Title


def Search(inputStr):
    # convert the string into a list for analyzing later
    inputList = inputStr.split()

    # matchFile is a set for the files matching the input string
    matchFile = set()

    # connect to the database
    conn = sqlite3.connect('./preHandle/PretreatmentInfo.db')
    cursor = conn.cursor()
    a = list()

    # we should select the information about the documents
    for i in inputList:
        cursor.execute('''select FileNumber
                          from InvertedFile where WORD = ?''', (i,))

        # fetchall is a function to fetch the contents we select before
        result = cursor.fetchall()
        resultList = []
        # we should judge if it is a empty list first
        if len(result) > 0 and len(result[0]) > 0:
            resultList = result[0][0].split()
        for j in resultList:
            matchFile.add(int(j))
    resultList = []

    # generate the result list
    for i in matchFile:
        cursor.execute('''SELECT *
                          from urlTitleIndex 
                          WHERE FileID = ?
                        ''', (i,))
        tempResult = cursor.fetchall()
        if tempResult:
            document = Document(tempResult[0])
            resultList.append(document)
        else:
            pass

    # close the database
    conn.close()

    return resultList
