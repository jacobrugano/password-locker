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
