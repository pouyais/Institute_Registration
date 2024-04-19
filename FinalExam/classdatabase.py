import sqlite3


class Database:
    def __init__(self,path):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS people (id integer PRIMARY KEY, name text, lname text, namecourse text, password integer)")
        self.con.commit()

    def insert(self,name,lname,namecourse,password):
        self.cur.execute("INSERT INTO people VALUES (NULL,?,?,?,?)",(name,lname,namecourse,password))
        self.con.commit()

    def remove(self,id):
        self.cur.execute("DELETE FROM people WHERE id = ?",(id,))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM people")
        rows = self.cur.fetchall()
        return rows
    
    def password(self,password):
        self.cur.execute("SELECT * FROM people WHERE password = ?",(password,))
        pw = self.cur.fetchall()
        return pw