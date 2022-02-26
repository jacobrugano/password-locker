import unittest # Importing the unittest module
from credential import Credential # Importing the user class

class TestCredential(unittest.TestCase):
    '''
    We create a subclass class called TestCredential, that inherits from unittest.TestCase and defines
    test cases for the TestCredential class behaviours.
    '''

    def setUp(self):
        '''
        setUp() method allows us to define instructions that will be executed before each test method.
        '''
        self.new_credential = Credential("Jacob","3456788","0711223344") # create user object


#Let's write code to check if the Credential class has been instantiated correctly and the results are as expected.
    def test_init(self):

        self.assertEqual(self.new_credential.user_name,"Jacob")
        self.assertEqual(self.new_credential.pass_word,"3456788")
        self.assertEqual(self.new_credential.phone_number,"0711223344")
