#from app.main.Controller.LoginTemplate import *
from app.main.Utils.errorLogging import *
from app.main.Controller.searchTemplate import *
from app.main.Repository.TableFileSearchData import DatabaseOperations
from app.main.Repository.TableLoginCredentials import close
from app.main.Controller.LoginTemplate import *
#clos = DatabaseOperations()

class inputs:
# input login credentials
    def login_credentials(self):
        self.username = input('ENter Email: ')
        self.password = input("Enter password: ")
        return self.username, self.password
    # input file name
    def file_name(self):
        self.filename = input("Enter file name: ")
        return self.filename
    def get_userid(self):
        return self.username

# login flow
def login():
    try:
        option = int(input('Choose options:\n\n1. sign-in\n\n2. Register\n\n-> '))
    except:
        print("Invalid input please enter valid input")
        retry = input("Retry?(yes/no): ")
        if retry == 'yes':
            login()
        else:
            print("We are sorry please try next time")
    # validates login choice     
    validateLoginChoice(option)
    # flow of isgn in option
    if option == 1: 
        a = inputs()
        udetails = a.login_credentials()
        obj_login = Login(udetails[0],udetails[-1])
        res = obj_login.signin() 
        if res == 'Invalid':
            loginres = obj_login.re_login()
            if loginres == True:
                login()
            else:
                print("")
    # flow of register option
    elif option == 2:
        a = inputs()
        udetails = a.login_credentials()
        obj_login = Login(udetails[0],udetails[-1])
        resR = obj_login.register()
        if resR == 'Invalid':
            loginres = obj_login.re_login()
            if loginres == True:
                login()
            else:
                print("Buye")
    else:
        print("Wrong choice")
        login()
    try:
        return udetails[0]
    except:
        print("Local error")

# search flow
def search(userid):
    obj_search = SearchTemplate()
    availdrives = obj_search.display_drives()
    search_drive = obj_search.search_drives()
    rdrives = obj_search.resultantdrives()
    if rdrives == 0:
        re_attempt = obj_search.re_search()
        if re_attempt == 1:
            search(userid)
        else:
            print("Bye")
    else:
        objinput = inputs()
        filename = objinput.file_name()
        if len(rdrives) == 1:
            search_again = obj_search.search_single_drive(filename,rdrives[0],userid)
            if search_again == 1:
                search(userid)
            else: print('Your seearch is complete')
        else:
            search_again = obj_search.search_Multiple_drives(filename,rdrives,userid)
            if search_again == 1:
                search(userid)
            else: print("Thanyou ")

def main():
    userid = login()
    search(userid)
    clos = close()

if __name__ == '__main__':
    main()