def testDatabase():
    import sqlite3

    conn = sqlite3.connect('../server/preHandle/PretreatmentInfo.db')
    cursor = conn.cursor()
    cursor.execute('''
                      SELECT * from InvertedFile
                        ''')

    a = cursor.fetchall()

    for i in a[:20]:
        print(i)

    # cursor.execute('''
    # SELECT * from urlTitleIndex''')
    cursor.execute('''
                    SELECT * from tf''')
    b = cursor.fetchall()
    for i in b[:]:
        print(i)

    conn.close()


testDatabase()
