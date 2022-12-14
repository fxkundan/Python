import pyodbc
import pandas as pd 
import numpy as np
import pyarrow.parquet as pq
import pyarrow as pa
from fastparquet import write 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=emishasql.database.windows.net;'
                      'Database=sql2022;'UID=USER;PWD=PASSWORD')

cursor = conn.cursor()
cursor.execute('SELECT TOP (10) cast([AddressID] as varchar(50)) as AID,[AddressLine1] FROM [AdventureWorks2019].[Person].[Address]')

table_rows=cursor.fetchall()
conn.close()
print(table_rows)
#df = pd.DataFrame(table_rows)
#df.columns = df.columns.astype(str)
#print(df)
#write('C:\\Users\\KundanKumar\\Desktop\\Study\\Test\\test2.parquet', df)


#df.to_parquet('C:\\Users\\KundanKumar\\Desktop\\Study\\Test\\test2.parquet',parquet_engine = 'pyarrow', compression='snappy')