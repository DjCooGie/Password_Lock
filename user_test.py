import unittest
from user import User

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





if __name__ == '__main__':
    unittest.main()