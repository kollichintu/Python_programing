
import pyodbc


conn = pyodbc.connect(r'Driver=SQL Server;Server=AGN-CL-LAXMANK-\SQLEXPRESS;Database=testDB;Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('SELECT * FROM SL_POL_DED')

for row in cursor:
    print(row)