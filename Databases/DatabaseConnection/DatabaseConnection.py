import mysql.connector
import psycopg2
import datetime

class DatabaseConnection:
    def __init__(self, database, config):
        self.connection = ''
        self.cursor = ''
        if database == "mySQL":
            self.connection = self.connectMySQL(config)
        elif database == "postgreSQL":
            self.connection = self.connectPostgres(config)
        else:
            print("error")
        pass


    def execute(self, query):
        if not isinstance(self.connection, bool):
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        else:
            print("Conexão falhou! self.connection =", self.connection)
            return (None)
    

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
    

    @staticmethod
    def dateToString(value):
        if isinstance(value, (datetime.date, datetime.datetime)):
            value_to_string = value.__str__()
            year = value_to_string[:4]
            month = value_to_string[5:7]
            day = value_to_string[8:10]
            new_value = '%s/%s/%s' % (day,month,year)
            return new_value
        return value
    
    
    @staticmethod
    def fixQueryResult(result):

        final_array = []
        for result_row in result:
            new_row = []

            for index, element in enumerate(result_row): 
                el = DatabaseConnection.dateToString(element)
                new_row.append(el)

            final_array.append(new_row)
        
        return final_array
