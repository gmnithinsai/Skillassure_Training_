import logging
from DBconnect import *
# connection to Database
connection = connect('FileSearchEngine')
# Table login credentials operations class
class TbLoginCred:
    def __init__(self, uname, passwd):
        self.uname = uname
        self.passwd = passwd
        self.postman = connection.cursor()
    def createTable(self):
        Table_Create_Query = '''
        CREATE TABLE Login_Credentials(username TEXT NOT NULL,password TEXT NOT NULL)
        '''
        try:
            self.postman.execute(Table_Create_Query)
            connection.commit()
            print("Table created")
        except:
            logging.error("Table is duplicated")
        finally:
            connection.close()
    # insert data into table
    def insertData(self):
        fdetails = (self.uname,self.passwd)
        insert_data_query = '''
        insert into login_credentials(username, password) values(%s, %s)
        '''
        self.postman.execute(insert_data_query, fdetails)
        #print("Data inserted into table")
        connection.commit()
        connection.close()
    # checks for login credentials exists
    def existData(self):
        exist_data_query = '''
        SELECT EXISTS(SELECT * FROM login_credentials where username = %(u)s and password = %(p)s)
        '''
        self.postman.execute(exist_data_query,{'u' : self.uname, 'p' : self.passwd})
        result = self.postman.fetchone()
        return result
    # select data from the table    
    def selectData(self):
        data = (self.uname,self.passwd )
        select_data_query = '''
        select filelocation from filesearchdata where filename = %s
        '''
        self.postman.execute(select_data_query, data)
        rows = self.postman.fetchone()
        print("Fetched from DB")
        return rows
    # add column in the table
    def addColumn(self,column_name):
        self.cname = column_name
        add_column_query = '''ALTER TABLE login_credentials
        ADD COLUMN %s VARCHAR'''
        self.postman.execute(add_column_query,(self.cname,))
        
# close database connection
def close():
        print('connncection closed')
        connection.close()
