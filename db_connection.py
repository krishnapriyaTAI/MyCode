import mysql.connector
from rich import print


def createConnection():
    try:
        dbConnection = mysql.connector.connect(host='127.0.0.1',
                                               user='root',
                                               password='123456',
                                               database='atm' )
        dbConnection.autocommit=True
        return dbConnection
    except Exception as err:
        print(str(err))
        
        
def main():
    conn = createConnection()
    cursor=conn.cursor()
    cursor.Execute("select * from customer_table")
    respose = cursor.fetchall()
