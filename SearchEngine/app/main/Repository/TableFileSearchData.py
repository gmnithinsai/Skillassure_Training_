import logging
from DBconnect import *
from app.main.Utils.errorLogging import *
trans_mod = transaction_module()

connection = connect('FileSearchEngine')
# File search table
class DatabaseOperations:
    def __init__(self):
        self.postman = connection.cursor()
    # creates table
    def createTable(self):
        Table_Create_Query = '''
        CREATE TABLE FileSearchData(Filename TEXT NOT NULL,FileLocation TEXT)
        '''
        try:
            self.postman.execute(Table_Create_Query)
            connection.commit()
        except:
            logging.error("Table is duplicated")
        finally:
            connection.close()
    # insert data into table
    def insertData(self,floc,fnam,userid):
        fdetails = (floc,fnam,userid)
        insert_data_query = '''
        insert into filesearchdata(Filename, Filelocation, userid) values(%s, %s, %s)
        '''
        self.postman.execute(insert_data_query, fdetails)
        trans_mod.datainserted()
        connection.commit()
        #connection.close()
    # select data from the table
    def selectData(self, filename):
        data = (filename, )
        select_data_query = '''
        select filelocation from filesearchdata where filename = %s
        '''
        result = self.postman.execute(select_data_query, data)
        rows = self.postman.fetchone()
        trans_mod.datafetched()
        return rows
    # add extra column into database
    def addColumn(self):
        add_column_query = '''ALTER TABLE filesearchdata
        ADD COLUMN userid VARCHAR'''
        self.postman.execute(add_column_query)
        connection.commit()
        print("Added column")
        
# close connection
def close():
    connection.close()





