from flask_app.config.mysqlconnection import MySqlConnection, connectToMySql
from flask_app import app
 
class User:
    DB = "mydb"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

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
    def delete_user(cls, id):
        data = { 'id' : id}
        query = "delete * FROM users WHERE id = %(id)s;"
        return connectToMySql(cls.DB).query_db(query, data)

    
