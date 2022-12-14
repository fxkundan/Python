import pandas as pd
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-PBJFQ5N\MSSQLSERVER01;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
data =cursor.execute('SELECT TOP (10) [AddressID],[AddressLine1],[AddressLine2] FROM [AdventureWorks2019].[Person].[Address]')

//table_rows=cursor.fetchall()
f=[i[0] for i in data.description]
print(f)
for i in data:
    print(i)
