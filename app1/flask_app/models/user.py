from flask_app.config.mysqlconnection import MySqlConnection, connectToMySql
from flask_app import app
from flask_app.models import book




class User:
    DB = "mydb"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []
        

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users(first_name,last_name) values(%(first_name)s, %(last_name)s);"
        return connectToMySql(cls.DB).query_db(query, data)


    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        result = connectToMySql(cls.DB).query_db(query)
        users = []
        for row in result:
            users.append(cls(row))
        return users

    @classmethod
    def get_user_id(cls, id):
        data = {'id': id}
        query = """SELECT *
        FROM users
        JOIN books
        ON
        users.id = books.users_id
        WHERE users.id = %(id)s
        ;"""
        result = connectToMySql(cls.DB).query_db(query, data)
        print('00000000000000000000000000', result)
        this_user = cls(result[0])
        for a_book in result:
            data = {
                'title' : a_book['title'],
                'author' : a_book['author'],
                'thoughts' : a_book['thoughts'],
                'created_at': a_book['books.created_at'],
                'updated_at': a_book['books.updated_at'],
                'id' : a_book['books.id']
            }
            this_user.books.append(book.Book(data))
        return(this_user)
    

    @classmethod
    def get_user_id2(cls, id):
        data = {'id':id}
        query = "SELECT * FROM books WHERE id = %(id)s"
        this_user = connectToMySql(cls.DB).query_db(query, data)
        this_user = this_user[0]
        their_book = book.Book.get_book_by_id(this_user.id)
        this_user.books = their_book
        return their_book
    

    @classmethod
    def delete_user(cls, id):
        data = { 'id' : id}
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySql(cls.DB).query_db(query, data)

    
    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name =%(first_name)s, last_name = %(last_name)s WHERE ID = %(id)s;"
        result = connectToMySql(cls.DB).query_db(query, data)
        return result
