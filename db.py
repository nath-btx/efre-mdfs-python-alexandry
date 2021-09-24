#!/usr/bin/python

import sqlite3


def addBook(id,title,author):
    try:
        sqliteConnection = sqlite3.connect('books.db')
        cursor = sqliteConnection.cursor()
        print("Opened database")

        create_table_query = '''CREATE TABLE IF NOT EXISTS BOOK(
                            id INT PRIMARY KEY NOT NULL,
                            title TEXT NOT NULL,
                            author TEXT NOT NULL);'''
        
        cursor = sqliteConnection.cursor()
        cursor.execute(create_table_query)

        insert_with_param = """INSERT INTO 'BOOK'
                            ('id', 'title', 'author')
                            VALUES(?,?,?);"""

        data_tuple = (id, title, author)
        cursor.execute(insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Book added successfully")

    except sqlite3.Error as error:
        print("Error while working with SQLite : ", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")



def getBooks():
    try:
        sqliteConnection = sqlite3.connect('books.db')
        cursor = sqliteConnection.cursor()
        print("Opened database")

        select_query = """SELECT id, title, author from BOOK"""
        cursor.execute(select_query)

        records = cursor.fetchall()
        print("fetched")
        print(records)
        # for row in records:
        #     id = row[0]
        #     title=row[1]
        #     author=row[2]
        #     print("id = ", row[0])
        #     print("title = ", title)
        #     print("author = ", author)
        #     print(" ")
        cursor.close()


    except sqlite3.Error as error:
        print("Error while working with SQLite : ", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")




def updateBook(id, title):
    try:
        sqliteConnection = sqlite3.connect('books.db')
        cursor = sqliteConnection.cursor()
        print("Opened database")
        update_query = """Update BOOK 
                        set title = ? 
                        where id = ?"""
        data = (id, title)
        cursor.execute(update_query, data)
        print("Book updated")



        


    except sqlite3.Error as error:
        print("Error while working with SQLite : ", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")


addBook(1,"Hunger Games", "Suzanne Collins")
addBook(2,"Le Rouge et le Noir", "Stendhal")
addBook(3,"L'Oeuvre au Noir", "Marguerite Yourcenar")
getBooks()
# updateBook(1,"Jeu de la faim")
# getBooks()



