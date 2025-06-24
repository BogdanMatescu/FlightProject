import sqlite3 
import os


class database_api: 
    
    def __init__(self):  
        db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../db/flight_collection.db"))
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
        self.table = self.cursor.execute("CREATE TABLE IF NOT EXISTS flights(id Integer Primary KEY, departure varchar(250) NOT NULL, arrival varchar(250) NOT NULL, price float, cabin varchar(250) NOT NULL )")


    def add_new_entry(self, departure, arrival, price, cabin): 
        self.cursor.execute("SELECT * FROM flights ORDER BY id DESC LIMIT 1") 
        last_id = self.cursor.fetchone() 
        if last_id: 
            id = last_id[0] + 1
            self.cursor.execute(f"INSERT INTO flights (id, departure, arrival, price, cabin) VALUES (?, ?, ?, ?, ?)",(id, departure, arrival, price, cabin)) 
            self.db.commit()
        else: 
            id = 1
            self.cursor.execute(f"INSERT INTO flights (id, departure, arrival, price, cabin) VALUES (?, ?, ?, ?, ?)",(id, departure, arrival, price, cabin))
            self.db.commit()
            
    def show_database_inputs(self):
        rezultate = self.cursor.execute("SELECT * FROM flights ORDER BY id ASC;")
        lista_rezultate = list(rezultate)  
        return lista_rezultate