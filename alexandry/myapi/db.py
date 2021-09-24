#!/usr/bin/python

from os import stat
import sqlite3
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def addBook(request):
    id = request.data.get('id')
    author = request.data.get('author')
    title = request.data.get('title')
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
        return Response({"message":"Book succesfully added"}, status=status.HTTP_200_OK)

    except sqlite3.Error as error:
        print("Error while working with SQLite : ", error)        
        return Response("problem while adding book", status=status.HTTP_400_BAD_REQUEST)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")



@api_view(['GET'])
def getBooks(request):
    try:
        print(request)
        sqliteConnection = sqlite3.connect('books.db')
        cursor = sqliteConnection.cursor()
        print("Opened database")

        select_query = """SELECT id, title, author from BOOK"""
        cursor.execute(select_query)

        records = cursor.fetchall()
        print("fetched")
        print(records)
        cursor.close()
        return Response(records)
        # for row in records:
        #     id = row[0]
        #     title=row[1]
        #     author=row[2]
        #     print("id = ", row[0])
        #     print("title = ", title)
        #     print("author = ", author)
        #     print(" ")


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


# addBook(1,"Hunger Games", "Suzanne Collins")
# addBook(2,"Le Rouge et le Noir", "Stendhal")
# addBook(3,"L'Oeuvre au Noir", "Marguerite Yourcenar")
# getBooks()
# updateBook(1,"Jeu de la faim")
# getBooks()



