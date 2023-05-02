import psycopg2
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv('.env')

DB_ULR = os.environ.get("PGURL_LOCAL")

class Database:
    
    def __init__(self):
        self.url = DB_ULR
        try:
            self.conect = psycopg2.connect(self.url)
            self.cursor = self.conect.cursor()
        except Exception as e:
            print(f'Falha ao conectar no banco de dados: {e}')
    
    @property
    def konect(self):
        return self.conect
    @property
    def kursor(self):
        return self.cursor
    
    def commit(self):
        self.konect.commit()
    def fetchall(self):
        return self.kursor.fetchall()
    def execute(self, sql, params=None):
        self.kursor.execute(sql, params or ())
    def query(self,sql, params=None):
        self.kursor.execute(sql, params or ())
        return self.fetchall()
    
    def setPassword(self,password):
        self.hash_password = generate_password_hash(password)
        return self.hash_password
    def registerUser(self, name, email, password):
        sql = f'''SELECT * FROM "users" WHERE email = '{email}' '''
        if self.query(sql):
            print(f'Email {email} já cadastrado')
            return False
        hash_pass = self.setPassword(password)
        print(hash_pass,len(hash_pass))
        sql = f'''INSERT INTO "users" (name, email,password) VALUES ('{name}','{email}','{hash_pass}')'''
        try:
            self.execute(sql)
            self.commit()
            print("Usuário registrado com suecesso")
            return True
        except Exception as e:
            print(f'Falha ao registrar usuário: {e}')
            return False
    
    def validateUser(self, email, password):
        sql = f'''SELECT id,name,email,password FROM "users" WHERE email = '{email}' '''
        q = self.query(sql)
        if q:
            stored_hash = q[0][3]
            print(stored_hash,password)
            check_pass = check_password_hash(stored_hash,password)            
            return check_pass, q
        else:
            return False, 0