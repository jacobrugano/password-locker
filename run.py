#!/usr/bin/env python3.6

from traceback import print_list
from credential import Credential
from user import User

#Creating a new user
def create_user(first_name,last_name,number,password):
    '''
    Function to create a new user
    '''
    new_user = User(first_name,last_name,number,password)
    return new_user


#Saving the new user
def save_user(user):
    '''
    Function to save user details
    '''
    user.save_user()