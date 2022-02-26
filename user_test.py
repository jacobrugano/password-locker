import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):
    '''
    We create a subclass class called TestUser, that inherits from unittest.TestCase and defines
    test cases for the contact class behaviours.
    '''

    def setUp(self):
        '''
        setUp() method allows us to define instructions that will be executed before each test method.
        '''
        self.new_user = User("Jacob","Rugano","0711223344", "3456788") # create user object
