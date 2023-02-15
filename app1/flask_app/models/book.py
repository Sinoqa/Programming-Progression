from flask_app.config.mysqlconnection import MySqlConnection, connectToMySql
from flask_app import app


class Book:
    DB = "mydb"
    def __init__(self, data):
        self.title = data['title']
        self.author = data['author']
        self.thoughts = data['thoughts']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.id = data['id']



    @classmethod
    def create_book(cls, data):
        query = "INSERT INTO books (title, author, thoughts, users_id) VALUES (%(title)s, %(author)s, %(thoughts)s, %(users_id)s, );"
        return MySqlConnection(cls.DB).query_db(query, data)
 

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        result = MySqlConnection(cls.DB).query_db(query)
        books = []
        for row in result:
            books.append(cls(row))
        return books



    @classmethod
    def get_all_books_by_user(cls, data):
        query = "SELECT * FROM users JOIN books ON users.id = books.users_id WHERE users.id = %(id)s;"
        results = connectToMySql(cls.DB).query_db(query, data)
        return results
 




    
    @classmethod
    def get_book_by_id(cls,id):
        data = {'id' : id}
        query = "SELECT * FROM books WHERE books.id = %(id)s;"
        result = connectToMySql(cls.DB).query_db(query, data)
        results = cls(result[0])
        books = []
        for book in result:
            data = {
                'title' : book['title'],
                'author' : book['author'],
                'thoughts' : book['thoughts'],
                'created_at': book['created_at'],
                'updated_at': book['updated_at'],
                'id' : book['id']
            }
            books.append(data)
        print(books)
        return results


    @classmethod
    def update_book(cls, data):
        query = "UPDATE books SET title= %(title)s, author= %(author)s, thoughts= %(thoughts)s WHERE id =%(id)s;"
        result = connectToMySql(cls.DB).query_db(query, data)
        return result

    @classmethod
    def delete_book_by_id(cls, id):
        data = {'id':id}
        query = "DELETE FROM books WHERE id = %(id)s;"
        result = connectToMySql(cls.DB).query_db(query, data)
        return result
