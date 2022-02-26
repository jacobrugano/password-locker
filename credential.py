class Credential:   #Class that generates new instances of credentials
    
    credential_list = [] #credential_list is a Class variables(variables that belong to the entire class and can be  accessed by all instances of the class. This user_list var will be used to store our created user objects
    def __init__(self,user_name,pass_word,number,email):
                            #  __init__ method to create new instances of a class Credential and to allow us to pass in properties for the new object.
        self.user_name = user_name
        self.pass_word = pass_word
        self.phone_number = number
        self.email = email

#We create a delete_credential method that uses the remove() method to delete the credential object from the credential_list.
    def delete_credential(self):
        Credential.credential_list.remove(self)

#We create a credential_user() method and called it on Credential object to save credentialss into the credential_list using append() method.'''  
    def save_credential(self):  
        Credential.credential_list.append(self) 


    @classmethod 
    def find_by_user_name(cls,user_name):
        '''
        Method that takes in the username and returns a username that matches that name.
        Args:
            number: username to search for
        Returns :
            Credentials of person that matches the username.
        '''
        for credential in cls.credential_list:
            if credential.user_name == user_name:
                return credential


    @classmethod             
    def display_credential(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credential_list