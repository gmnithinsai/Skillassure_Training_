from PC_drives import *
from file_location import *
from app.main.Repository.TableFileSearchData import DatabaseOperations
from app.main.Utils.errorLogging import *
dbOpera = DatabaseOperations()

# get file location 
class getFlocation:
    def __init__(self, filename,drives):
        self.filename = filename
        self.drives = drives

    # get file location from searching in drives
    def get_fileloc_pc(self):
        floc = multiThreading(self.filename, self.drives)
        newfloc = []
        #print(floc)
        if len(floc) == 0:
            print("File not found in pc")
        else:
            for loc in floc:
                if len(loc) != 0:
                    newfloc.append(loc)
                    print('join')
                    print("\n".join(loc))
        return newfloc
    # get file location from database
    def get_fileloc_db(self):
        floc = dbOpera.selectData(self.filename)
        if floc != None:
            for loc in floc:
                print(loc,'from database')
        return floc

# data base update operations   
class DbUpdate:
    def __init__(self, filename, filelocation,userid):
        self.fname = filename
        self.floc = filelocation
        self.userid = userid
    # insert data 
    def insert_fdetails(self):
        dbOpera.insertData(self.fname, self.floc, self.userid)
    

# operations in search flow
class SearchTemplate:
    @classmethod
    # display drives available in pc
    def display_drives(self):
        self.drives = drives_in_pc()
        print("Available Drives in your pc:")
        for drive in self.drives:
            print(drive[0])
        return self.drives
    # user input for drives
    def search_drives(self):
        searchdrive = input("Enter drives in which you want to search(space separated inputs): ").split()
        self.searchdrives = []
        for i in searchdrive:
            self.searchdrives.append(i.upper()+':\\')
        return self.searchdrives
    # search again if drives are not matched with available drives
    def re_search(self):
        reattempt = input("Do you want to choose drives again: ")
        if reattempt == 'yes':
            return 1
        else:
            return 0
    # validation of search drives and avialable drives
    def resultantdrives(self):
        res = validateDrives(self.searchdrives, self.drives)
        if res == 0:
            print("No matches available for your drives")
        else:
            print(f"Available drives:{res}")
        return res
    # search file again
    def search_file_again(self):
        fagain = input("search another file?(yes/no): ")
        if fagain == 'yes':
            return 1
        else:
            return 0
    # search operation in multi thread
    def search_Multiple_drives(self, filename, drives,userid):
        obj_floc = getFlocation(filename,drives)
        dbfloc = obj_floc.get_fileloc_db()
        # search in pc only when file not found in db
        if dbfloc == None:
            pcfloc = obj_floc.get_fileloc_pc()
            if len(pcfloc) == 0:
                print("File not exist")
            else:
                obj_updatedb = DbUpdate(filename, pcfloc,userid)
                obj_updatedb.insert_fdetails()
        res = self.search_file_again()
        return res
    # search operation in single thread
    def search_single_drive(self, filename, drives,userid):
        obj_floc = getFlocation(filename,drives)
        dbfloc = obj_floc.get_fileloc_db()
        # search in pc only when file not found in db
        if dbfloc == None:
            searchresult = locate_file(filename,drives)
            for loc in searchresult:
                print(loc)
                if len(searchresult) == 0:
                    print("File not exist")
                else:
                    obj_updatedb = DbUpdate(filename, searchresult,userid)
                    obj_updatedb.insert_fdetails()
        res = self.search_file_again()
        return res