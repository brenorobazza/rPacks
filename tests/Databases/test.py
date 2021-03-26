from DatabaseConnection.DatabaseConnection import DatabaseConnection
from credentials import test_postgres_database_credentials

# put this in credentials.py
# database = {
#         "user": "youruser",
#         "password": "yourpassword",
#         "host": "yourhost",
#         "port": port_number,
#         "database": "postgres"
#     }

database = DatabaseConnection('postgreSQL', test_postgres_database_credentials)
results = database.execute("SELECT * FROM test_table LIMIT 10")
print(results)