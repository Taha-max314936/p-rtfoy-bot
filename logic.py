import sqlite3
from config import DATABASE


class DB_Manager:
    def __init__(self, database):
        self.database = database # veri tabanının adı
        
    def create_tables(self):
        con = sqlite3.connect(DATABASE)
        with con:
            con.execute('''CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    project_name TEXT NOT NULL,
    description TEXT,
    url TEXT,
    status_id INTEGER,
    FOREIGN KEY(status_id) REFERENCES status(status_id))
                        
    )

                       ''')

        con.execute('''CREATE TABLE skills (
                skill_id INTEGER PRIMARY KEY,
                skill_name TEXT)
                    )''')
        
        con.execute('''CREATE TABLE status (
                    status_id INTEGER PRIMARY KEY
                    skill_name TEXT)
                    ''')
        
        con.execute('''CREATE TABLE project_skills (
                    project_id INTEGER,
                    skill_id TEXT,
                    FOREIGN KEY(project_id) REFERENCES projects(project_id))
                    FOREIGN KEY(skill_id) REFERENCES skills(skill_id))
                    )            
                    ''')
        con.commit

        print("Veri tabanı oluşturuldu")

        