import mysql.connector
import psycopg2


class DatabaseConnection:
    def __init__(self, database, config):
        self.connection = ''
        self.cursor = ''
        if database == "mySQL":
            self.connection = self.connectMySQL(config)
        if database == "postgreSQL":
            self.connection = self.connectPostgres(config)
        else:
            print("error")
        pass
    
    @staticmethod
    def connectMySQL(config):
        try:
            conn = mysql.connector.connect(**config)
        except:
            conn = False
            print("Você não possui acesso ao banco")
        return conn

    @staticmethod
    def connectPostgres(config):
        try:
            conn = psycopg2.connect(**config)
        except:
            conn = False
            print("Você não possui acesso ao banco")
        return conn

    @staticmethod
    def readSQL(queryPath):
        with open(queryPath, 'r') as sql_file:
            return sql_file.read()

    def execute(self, query):
        if not isinstance(self.connection, bool):
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        else:
            print("Conexão falhou! self.connection =", self.connection)
            return (None)
