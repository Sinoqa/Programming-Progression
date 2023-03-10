from flask_app.config.mysqlconnection import MySqlConnection, connectToMySql

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
    def create_buyer(cls, data):
        query = 'INSERT INTO buyers (first_name, last_name, phone_number) values(%(first_name)s, %(last_name)s, %(phone_number)s); '
        return MySqlConnection(cls.db).query_db(query,data)
    

#CRUD READING OF DATABASE
    @classmethod
    def get_all_buyers(cls):
        query = "SELECT * FROM buyers;"
        result = MySqlConnection(cls.db).query_db(query)
        users = []
        print(result)
        for row in result:
            users.append(cls(row))
        return users
    
    @classmethod
    def get_buyer_by_id(cls, data):
        data = {'id':id}
        query = 'SELECT * FROM flowers WHERE id = %(id)s'
        return MySqlConnection(cls.db).query_db(query, data)




#CRUD UPDATE OF DATABASE




#CRUD DELETION OF DATABASE