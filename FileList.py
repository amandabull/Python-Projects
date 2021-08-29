#Creating the Database with sqlite3
import sqlite3

conn = sqlite3.connect('fileList.db')

#Creating a table with 2 fields: ID field (auto-increment primary integer) and a field for the fileList names.
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    conn.commit()

#Inserting the variable fileList

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#Determining which files have a ".txt" extension
conn = sqlite3.connect('fileList.db')

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_fileList(col_fileName) VALUES (?)", (x,))
            print(x)
conn.close()
