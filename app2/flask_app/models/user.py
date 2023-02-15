from flask_app.config import mysqlconnection, connectToMySql
from flask_app.controllers import users


class User:
    db = "shopping"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.phone_number = data['phone_number']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



#CRUD CREATION OF DATABASE
    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO flower_shop first_name, last_name, phone_number values = %(first_name)s, %(last_name)s, %(phone_number)s; '
        result = mysqlconnection(cls.db).query_db(query,data)
        return result





#CRUD READING OF DATABASE
    @classmethod
    def get_all_buyers(cls):
        query = 'SELECT * FROM shopping'
        result = connect(cls.db).query_db(query)
        buyers = [ ]
        for row in result:
            buyers.append(cls[row])
        return buyers
    
    @classmethod
    def get_user_by_id(cls, data):
        data = {'id':id}
        query = 'SELECT * FROM shopping WHERE id = %(id)s'
        return mysqlconnection(cls.db).query_db(query, data)




#CRUD UPDATE OF DATABASE




#CRUD DELETION OF DATABASE
