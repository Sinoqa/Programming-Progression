from flask_app.config.mysqlconnection import MySqlConnection, connectToMySql

class Flower:

    db = "shopping"


    def __init__(self, data):
        self.id = data['id']
        self.flower_type = data['flower_type']
        self.amount = data['amount']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



#CRUD CREATION OF DATABASE
    @classmethod
    def create_flower(cls, data):
        query = 'INSERT INTO flowers flower_type, amount values = %(flower_type)s, %(amount)s; '
        return MySqlConnection(cls.db).query_db(query,data)



#CRUD READING OF DATABASE
    @classmethod
    def get_all_flowers(cls):
        query = "SELECT * FROM flowers;"
        result = MySqlConnection(cls.db).query_db(query)
        flowers = []
        print(result)
        for row in result:
            flowers.append(cls(row))
        return flowers
    
    @classmethod
    def get_flower_by_id(cls, data):
        data = {'id':id}
        query = 'SELECT * FROM flowers WHERE id = %(id)s'
        return MySqlConnection(cls.db).query_db(query, data)




#CRUD UPDATE OF DATABASE




#CRUD DELETION OF DATABASE