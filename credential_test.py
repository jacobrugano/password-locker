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

        ''' self.assertEqual() this is a TestCase method that checks for an expected result.
              The first argument is the expected result and the second argument is the result that is actually gotten.
             This code block is to check if the name and description of our new object is what we actually inputted. '''

#code block to test if the credential details has been added using the length method.
    def test_save_credential(self):
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1) #We test this using the length method.

# tearDown method that does clean up after each test case has run. Just like the setUp() method the tearDown() method executes a set of instructions after every test.
    def tearDown(self):
            Credential.credential_list = [] 
            '''in the tearDown() method, we assign the credential_list list in the Credential class as an 
             empty list. This helps us get accurate test results every time a new test case'''

             
#   test_save_multiple_credential' details to test if we can save multiple credentials in our credentials list.
    def test_save_multiple_credentials(self):
            self.new_credential.save_credential()  
            test_credential = Credential("Jacob","3456788","0711223344") # code block for the extra new credentials details
            test_credential.save_credential() # saving the extra new credential details
            self.assertEqual(len(Credential.credential_list),2) # to check if the length of our credential_list is equal to the number of users saved.

#To test if a credential can delete his credential details from the credential_list
    def test_delete_credential(self):
            self.new_credential.save_credential()  # saving the new credential details
            test_credential = Credential("Jacob","3456788","0711223344")  # code block for the extra new credential details
            test_credential.save_credential()
            self.new_credential.delete_credential()# Deleting a credential object
            self.assertEqual(len(Credential.credential_list),1)# to check if the length of our credential_list is equal to the number of credentials saved.


# To check if we can find a credentials entered using the user name and display this.
def test_find_credential_by_username(self):   #//////////////////////
        self.new_credential.save_credential()
        test_credential = Credential("Jacob","3456788","0711223344") # new user details
        test_credential.save_credential()
        found_credential = Credential.find_by_username("Jacob")

        self.assertEqual(found_credential.user_name,test_credential.user_name)

#Test to check if the credentials actually exists.
def test_credential_exists(self):     #//////////////////////1
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Jacob","3456788","0711223344") # new credential
        test_credential.save_credential()
        credential_exists = Credential.credential_exist("3456788")
        self.assertTrue(credential_exists)


# Test to check if we receive the list of the saved credentials.
def test_display_all_credentials(self):    #//////////////////////2
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)





if __name__ == '__main__':
    unittest.main()