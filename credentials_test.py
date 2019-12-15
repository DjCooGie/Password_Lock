import unittest
from credentials import Credential

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