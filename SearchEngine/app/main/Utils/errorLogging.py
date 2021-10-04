import logging
import re
logging.basicConfig(filename = 'nameError.log', level=logging.ERROR,
format = '%(asctime)s:%(message)s')
# Transaction details info
class transaction_module:
    def fetched_from_db(self):
        logging.error('INFO: File is read from search history')
    def signedin(self, user):
        logging.error(f'INFO: user signed in with id: {user}')
    def datainserted(self):
        logging.error('INFO:Data is inserted in table')
    def datafetched(self):
        logging.error('INFO: Data is fetched from table')
    def registered(self,user):
        logging.error(f"INFO:New user registered with id: {user} ")
# validates file name      
def validateFname(fname):
    for char in fname:
        if char in ['#','*','!','<','>','$']:
            logging.error('ERROR: Unsupported file name format')
# validates e mail
def validateEmail(mailId):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
    if(re.search(regex,mailId)):   
        return  
    else:   
        logging.error("ERROR: Invalid Email")
        return "Invalid Mail id"
# validates password
def validatePasswd(passw):
    fl = 0
    while True:   
        if (len(passw)<8): 
            fl= -1
            break
        elif not re.search("[a-z]", passw): 
            fl = -1
            break
        elif not re.search("[A-Z]", passw): 
            fl = -1
            break
        elif not re.search("[0-9]", passw): 
            fl = -1
            break
        elif not re.search("[_@$]", passw): 
            fl = -1
            break
        elif re.search("\s", passw): 
            fl = -1
            break
        else: 
            fl = 0
            #print(" This Is Valid Password") 
            break
    if fl ==-1: 
        logging.error("ERROR: Not a Valid Password")
        return 'Invalid Password'
# vlaidates login choice
def validateLoginChoice(option):
    if option != 1 and  option != 2:
        logging.error('ERROR: Invalid choice between sign in and register')
# validates drives input
def validateDrives(searchdrive,availdrive):
    resultdrive = []
    for drive in searchdrive:
        if drive in availdrive:
            resultdrive.append(drive)
        else:
            logging.error(f'invalid drive {drive}')
    if len(resultdrive) == 0:
        return 0
    else:
        return resultdrive