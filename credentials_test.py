import unittest
from credentials import Credential
from user import User

class TestCredentials(unittest.TestCase):
    '''    
    Class defines test cases for the Credentials class behaviours

	Args:
	    unittest.TestCase: facilitates creation of test cases
    '''
    
    def test_verify_user(self):
        '''
        Function to test whether the login in function check_user works as expected
        '''
        self.new_user = User('Simion','pass001')
        self.new_user.save_user()
        user2 = User('Brian','pass001')
        user2.save_user()
        
        for user in User.users_list:
            if user.realname == user2.realname and user.password == user2.password:
                current_user = user.realname
            return current_user
            
        self.assertEqual(current_user,Credential.verify_user(user2.password,user2.realname))

    def setUp(self):
        '''
        Function to create an account's credentials before each test
        '''
        self.new_credential = Credential('Evans','Facebook','evanjo','pass001')  

    def test_init(self):
        '''
        Checks if instantiantion of objects is properly done
        '''
        self.assertEqual(self.new_credential.username,'Evans')
        self.assertEqual(self.new_credential.sitename,'Facebook')
        self.assertEqual(self.new_credential.accountname,'evanjo')
        self.assertEqual(self.new_credential.password,'pass001')

    def test_save_credentials(self):
        '''
        Test to check if the new credential info is saved into the credentials list
        '''
        self.new_credential.save_credentials()
        twitter = Credential('Skina','Twitter','sqina','pass001')
        twitter.save_credentials()
        self.assertEqual(len(Credential.credentials_list),2)
        
    def tearDown(self):
        '''
        Clears the credentials list after every test
        '''
        Credential.credentials_list = []
        User.users_list = []
        
    def test_output_credentials(self):
        '''
        Checks if the output_credentials method, displays the correct credentials.
        '''
        self.new_credential.save_credentials()
        twitter = Credential('Skina','Twitter','sqina','pass001')
        twitter.save_credentials()
        self.assertEqual(len(Credential.output_credentials(twitter.username)),2)

    def test_findby_sitename(self):
        '''
        Checks if the findby_sitename method returns the correct credential
        '''
        self.new_credential.save_credentials()
        twitter = Credential('Skina','Twitter','sqina','pass001')
        twitter.save_credentials()
        credential_exists = Credential.findby_sitename('Twitter')
        self.assertEqual(credential_exists,twitter) 



if __name__ == '__main__':
    unittest.main()