from database import conn, select, insert, delete, update, search

class Data:
    def __init__(self):
        self.mydb = conn()

    def get_data(self, query):
        return select(query, self.mydb)

    def insert_data(self, query):
        return insert(query, self.mydb)

    def delete_data(self, query, id):
        return delete(query, self.mydb, id)

    def update_data(self, query, id, data):
        return update(query, self.mydb, id, data)

    def search_data(self, query):
        return search(query, self.mydb)