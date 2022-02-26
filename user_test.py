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


#Let's write code to check if the User class has been instantiated correctly and the results are as expected.
    def test_init(self):

        self.assertEqual(self.new_user.first_name,"Jacob")
        self.assertEqual(self.new_user.last_name,"Rugano")
        self.assertEqual(self.new_user.phone_number,"0711223344")
        self.assertEqual(self.new_user.password,"3456788")
        ''' self.assertEqual() this is a TestCase method that checks for an expected result.
              The first argument is the expected result and the second argument is the result that is actually gotten.
             This code block is to check if the name and description of our new object is what we actually inputted. '''


#code block to test if the user details has been added using the length method.
    def test_save_user(self):
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1) #We test this using the length method.
