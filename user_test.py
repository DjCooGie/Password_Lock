import unittest
from user import User, Credential

class TestUser(unittest.TestCase):
    '''
    Class defines test cases for the User class behaviours

    Args:
        unittest.TesCast: facilitates creation of test cases
    '''

    def setUp(self):
        '''
        Method to run before test cases
        '''
        self.new_user = User('Evans','evan01') 

    def test_init(self):
        '''
        Checks if instantiantion of objects is properly done
        '''
        self.assertEqual(self.new_user.realname,'Evans')
        self.assertEqual(self.new_user.password,'evan01')

    def test_save_user(self):
        '''
        Checks if new user info is saved into ther users list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)

class TestCredentials(unittest.TestCase):
    '''    
    Class defines test cases for the Credentials class behaviours

	Args:
	    unittest.TestCase: facilitates creation of test cases
    '''

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


        




if __name__ == '__main__':
    unittest.main()