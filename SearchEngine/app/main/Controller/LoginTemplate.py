import base64
import logging
from app.main.Utils.errorLogging import validateEmail, validatePasswd
from app.main.Repository.TableLoginCredentials import *
from app.main.Utils.notifications import login_notification
from app.main.Utils.errorLogging import transaction_module
TransMod = transaction_module()
# Login class
class Login:
    def __init__(self, id, pwd):
        self.id = id
        self.pswd = pwd
        self.count = 0
        self.fl_reattempt = None
    # validates login credentials
    def validateUdetails(self):
        valid_id = validateEmail(self.id)
        if valid_id:
            self.count+=1
            print(valid_id)
        valid_p = validatePasswd(self.pswd)
        if valid_p:
            self.count+=1
            print(valid_p)
    # validates whether user should signedin or not
    def validate_presignin(self):
        if self.count > 0: 
            return "Invalid"
    # validates whether user signed in or not
    def validate_SI_Reg(self):
            if self.loginexist[0]:
                login_notification(self.id)
                print("You have succesfully logged in")
                TransMod.signedin(self.id)
            else:
                print("Your login is failed please register or relogin with other credentials ")
                return 0
    # validates registration
    def validateReg(self):
        if self.count > 0: 
            #self.fl_reattempt = 'Invalid'
            return "Invalid"
    # sign in module
    def signin(self):
        self.validateUdetails()
        validate_signin = self.validate_presignin()
        if validate_signin == 'Invalid':
            return "Invalid"
        else:
            pswrd = self.encoder(self.pswd)
            obLoginCred = TbLoginCred(self.id, pswrd)
            self.loginexist =  obLoginCred.existData()
            valid = self.validate_SI_Reg()
            if valid == 0:
                return 'Invalid'
            else:
                print(' ')
    # register module    
    def register(self):
        self.validateUdetails()
        validate_reg = self.validateReg()
        if validate_reg == 'Invalid':
            return 'Invalid'
        else:
            self.insertUdetails()
            TransMod.registered(self.id)
            print("You have been registered as new user")
    # attempt to relogin
    def re_login(self):
            re_attempt = input("Do you want to try again:(yes/no):")
            if re_attempt == 'yes':
                return True
            else:
                return False
    # encryption of password
    def encoder(self,pswd): 
        self.password = pswd.encode("utf-8")
        self.encoded = base64.b64encode(self.password)
        return str(self.encoded)
    # Decryption of password
    def decoder(self, encoded):
        self.decoded = base64.b64decode(encoded)
        self.decodedpswd = str(self.decoded)
        self.decodedpswd.replace('b','')
        return self.decodedpswd
    # insert login credentials into database(encrypted)
    def insertUdetails(self):
        self.encodedpswd = self.encoder(self.pswd)
        objLogincred = TbLoginCred(self.id, self.encodedpswd)
        objLogincred.insertData()


