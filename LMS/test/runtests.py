import pyodbc 
server = 'NDD-NOT-PRE813' 
database = 'lms' 
username = 'sa' 
password = 'P@ssword1' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print (row[0]) 
    row = cursor.fetchone()