#!/usr/bin/python

from os import stat
import sqlite3
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def addBook(request):
    author = request.data.get('author')
    title = request.data.get('title')
    description = request.data.get('description')
    if (description is None):
        description = "No description"

    try:
        sqliteConnection = sqlite3.connect('books.db')
        cursor = sqliteConnection.cursor()
        print("Opened database")

        create_table_query = """CREATE TABLE IF NOT EXISTS BOOK(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            author TEXT NOT NULL,
                            description TEXT);"""
        
        cursor = sqliteConnection.cursor()
        cursor.execute(create_table_query)

        insert_with_param = """INSERT INTO 'BOOK'
                            ('title', 'author', 'description')
                            VALUES(?,?,?);"""

        data = (title, author, description)
        cursor.execute(insert_with_param, data)
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

        select_query = """SELECT id, title, author, description from BOOK"""
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


@api_view(['DELETE'])
def deleteBook(request):
    try:
        sqliteConnection = sqlite3.connect('books.db')
        cursor = sqliteConnection.cursor()
        print('Opened Database')
        delete_query = """  Delete from BOOK
                            where id = ?"""
        
        cursor.execute("""  Delete from BOOK
                            where id = ?""",(request.data.get('id'),))
        sqliteConnection.commit()
        print('Book deleted')
        return Response('Deleted', status.HTTP_200_OK)
    except sqlite3.Error as error:
        print("Error while working with SQLite : ", error)
        return Response('couldn\'t Update', status.HTTP_400_BAD_REQUEST)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('sqlite connection closed')


@api_view(['PUT'])
def updateBook(request):
    try:
        sqliteConnection = sqlite3.connect('books.db')
        cursor = sqliteConnection.cursor()
        print("Opened database")
        update_query = """UPDATE BOOK 
                        SET title = ?, author = ?, description = ?
                        WHERE id = ?"""

        data = (request.data.get('title'), request.data.get('author'),request.data.get('description'), request.data.get('id'))
        print(data)
        cursor.execute(update_query, data)
        sqliteConnection.commit()
        print("Book updated")
        return Response('Updated', status.HTTP_200_OK)


    except sqlite3.Error as error:
        print("Error while working with SQLite : ", error)
        return Response('couldn\'t Update', status.HTTP_400_BAD_REQUEST)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

