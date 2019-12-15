import random
import string

class Credential:
    '''
    Class to create  account credentials, generate passwords and save user information
    '''

    credentials_list = []
    user_credentials_list = []

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

    def generate_password(self,size=6, char = string.ascii_uppercase + string.ascii_lowercase + string.digits):
        '''
        Generates a 6 character password for a credential
        '''
        gen_pass=''.join(random.choice(char) for _ in range(size))
        return gen_pass

