import random
import string

class Credential:
    '''
    Class to create  account credentials, generate passwords and save user information
    '''

    credentials_list = []
    user_credentials_list = []
    @classmethod
    def verify_user(cls,username,password):
        '''
        Method that checks if the name and password entered match entries in the users_list
        '''
        current_user = ''
        for user in User.users_list:
            if (user.username == username and user.password == password):
                current_user = user.username
            return current_user

    def __init__(self,username,sitename,accountname,password):
        '''
        Method defines properties each user object will hold.
        '''
        self.username = username
        self.sitename = sitename
        self.accountname = accountname
        self.password = password

    def save_credentials(self):
        '''
        Saves a newly created user instance
        '''
        Credential.credentials_list.append(self)

    def generate_password(size=6, char = string.ascii_uppercase + string.ascii_lowercase + string.digits):
        '''
        Generates a 6 character password for a credential
        '''
        gen_pass=''.join(random.choice(char) for _ in range(size))
        return gen_pass
    
    @classmethod
    def findby_sitename(cls,sitename):
        '''
        Takes in a sitename and returns a credential matching the sitename
        '''
        for credential in cls.credentials_list:
            if credential.sitename == sitename:
                return credential


    @classmethod
    def output_credentials(cls,username):
        '''
        Displays the saved credentials list
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.username == username:
                user_credentials_list.append(credential)
        return user_credentials_list