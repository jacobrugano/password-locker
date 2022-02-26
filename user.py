class User:   #Class that generates new instances of contacts


    user_list = [] #user_list is a Class variables(variables that belong to the entire class and can be  accessed by all instances of the class. This user_list var will be used to store our created user objects
    def __init__(self,first_name,last_name,number,password):
                            #  __init__ method to create new instances of a class User and to allow us to pass in properties for the new object.
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.password = password


    #We create a save_user() method and called it on User object to save users into the user_list using append() method.'''  
    def save_user(self):  
        User.user_list.append(self) 