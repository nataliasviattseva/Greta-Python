import sqlite3
import psycopg2


class SQLite():
    def __init__(self, data_base):
        self.data_base = data_base
        print(self.data_base)

    def set_connexion(self):
        try:
            self.connexion = sqlite3.connect(self.data_base)
            self.cursor = self.connexion.cursor()
        except sqlite3.Error as err:
            print("! SQLite set_connexion() error : ", err)

    def create_table(self, sql_create_table):
        try:
            self.cursor.execute(sql_create_table)
        except sqlite3.Error as err:
            print("! SQLite create_table() error : ", err)

    def drop_table(self, table):
        try:
            sql = "drop table " + table + ";"
            self.cursor.execute(sql)
        except sqlite3.Error as err:
            print("! SQLite drop_table() error : ", err)

    def delete_all(self, table):
        try:
            sql = "delete from " + table + ";"
            self.cursor.execute(sql)
            # réinialise la séquence d'indexes à 0
            sql = '''update SQLITE_SEQUENCE set SEQ = 0;'''
            self.cursor.execute(sql)
        except sqlite3.Error as err:
            print("! SQLite delete_all() error : ", err)

    def insert_into(self, sql_insert_into):
        try:
            self.cursor.execute(sql_insert_into)
            self.connexion.commit()
        except sqlite3.Error as err:
            print("! SQLite insert_into() error : ", err)

    def select_all(self, table):
        try:
            sql = "select * from " + table + ";"
            print(sql)
            self.cursor.execute(sql)
            # restitue la liste résultante de la selection de donnés
            data_set = self.cursor.fetchall()
            print("select_all.data_set: ", data_set)
            return data_set
        except sqlite3.Error as err:
            print("! SQLite select_all() error : ", err)

    def close_connexion(self):
        try:
            self.cursor.close()
            self.connexion.close()
        except sqlite3.Error as err:
            print("! SQLite close_connexion() error : ", err)


class PostgreSQL():
    def __init__(self, data_base):
        self.data_base = data_base
        print(self.data_base)

    def set_connexion(self):
        try:
            self.connexion = psycopg2.connect(user='nsviattseva',
                                              password='qa12345678',
                                              host='localhost',
                                              port='5432',
                                              database=self.data_base)
            self.cursor = self.connexion.cursor()
        except psycopg2.Error as err:
            print("! postgreSQL set_connexion() error : ", err)

    def select_all(self, table):
        try:
            sql = "select * from " + table + ";"
            print(sql)
            self.cursor.execute(sql)
            # restitue la liste résultante de la selection de donnés
            data_set = self.cursor.fetchall()
            print("data_set: ", data_set)
            return data_set
        except psycopg2.Error as err:
            print("! SQLite select_all() error : ", err)

    def close_connexion(self):
        try:
            self.cursor.close()
            self.connexion.close()
        except psycopg2.Error as err:
            print("! SQLite close_connexion() error : ", err)


'''
""" SQLite EXECUTION """
sqlite = SQLite('../dbGreta78.db')
sqlite.set_connexion()

sql_create_table = """
create table if not exists tbCartoons
(id integer primary key autoincrement not null,
 Nom text,
 Prenom text,
 email text);
 """
sqlite.create_table(sql_create_table)

sqlite.delete_all('tbCartoons')

sql_insert_into = """
insert into tbCartoons (Nom, Prenom, email)
values
 ('DUCK', 'Donald', 'donald.duck@greta78.com'),
 ('MOUSE', 'Mickey', 'mickey.mouse@greta78.com');
"""
sqlite.insert_into(sql_insert_into)

sqlite.select_all('tbCartoons')
sqlite.close_connexion()
'''

""" PostgreSQL EXECUTION """
pgSQL = PostgreSQL('db_greta78')

pgSQL.set_connexion()

data_set = pgSQL.select_all('tb_formateur')

pgSQL.close_connexion()
