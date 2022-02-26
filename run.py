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

    
# Creating credentials
def create_credential(user_name,pass_word,phone,email):
    '''
    Function to create a new user credentials
    '''
    new_credential = Credential(user_name,pass_word,phone,email)
    return new_credential


#We create a save_credential function that takes in a credential/contact object and then calls the save_contact method to save the credentials.
def save_credential(credential):
    '''
    Function to save credentials
    '''
    credential.save_credential()


# We create a del_credential function that takes in a credential object and then calls the delete_credential() method on the contact object deleting it from the credential list.
def del_credential(credential):
    '''
    Function to delete a credentials
    '''
    credential.delete_credential()


# We create a function find_credential that takes in a number and calls the Credentialclass method find_by_number that returns the credentials.
def find_credential(number):
    '''
    Function that finds a credentials by number and returns the credentials
    '''
    return Credential.find_by_number(number)


# The function check_existing_credentials takes in a number as an argument and calls the class method credential_exist which returns a boolean.
def check_existing_credential(number):
    '''
    Function that check if credentials exists with that number and return a Boolean
    '''
    return Credential.credential_exist(number)


# We then create a function that displays all the credentials a user enters.
def display_credential():
    '''
    Function that returns all the saved contacts
    '''
    return Credential.display_credential()


def main():
                # Code for user class kwanza.
        print("Hello!! Welcome to Password Locker! Kindly enter your FIRST name:")
        first_name = input()
        print("To proceed, enter your SECOND name:..")
        last_name = input()
        print("*" * 50)
        print("Enter your phone number:..")
        number = input()
        print("Enter a password of your  choice:")
        password = input()
        print(f"Welcome {first_name} {last_name} of number {number}. Ensure you use {password} as your password to sign up to continue")
        print('\n')
        print("*" * 50)
        print ("Reply with: cc -to Create logins for this Passlocker Account(Recommended), ca - To create new logins for your sub-accounts in the PassLocker account such as Instragram, EX -to Exit the application, ca - create a new credentials account, se - to store existing credentials in the application,  to view your various account credentials and their passwords in the application, de  - To delete a a credentials account")
        print("*" * 50)

        while True:
            short_code = input().lower()

            if short_code == "cc":
                print("You are now creating an account on Password Locker...")
                print("Key in the following details:")
                print("Enter Username:.....")
                username = input()
                print("Enter your password:")
                password = input()

                save_user(create_user(first_name,last_name,number,password))
                print('\n')
                print(f"Your Account information is:")
                print(f"Username: {username}, Password:{password}")
                print("*" * 50)
                print("type     ca      to proceed to the login details of your sub-accounts such as Instagram")

            elif short_code == 'ca':
                print ("If you had not logged in to account eg Instagram, Enter the details you wish to be using in the new application:")
                print("Username:")
                # user_name = input()
                print("Password:")
                # pass_word = input()
                print("phone number:")
                # phone = input()
                print("email:")
                # email = input()

                print("Type  yes  if you would like a generated password?")
                if input() == "yes":
                        print('\n')
                        print("Your generated password is: dsxcvhjkouytredcvbjo09876543")
                        print("*" * 50)
                        print("Select   se  to proceed to saving your existing credentials")
                else: 
                        print("You have chosen    no   so we will use previously generated password.")
                        print("*" * 50)
                        print("Select   se  to proceed to saving your existing credentials")
                        print("*" * 50)
                        
            elif short_code == 'se':
                        print("*" * 50)
                        print("Thank you for choosing this option. You will proceed to storing your logins in the application")
                        print("*" * 50)
                        print("NOTE THAT: This are the same details you will be using in the new application")
                        print("*" * 50)
                        print("Username:")
                        user_name = input()
                        print("Password:")
                        pass_word = input()
                        print("phone number:")
                        phone = input()
                        print("email:")
                        email = input()
                        
                        save_credential(create_credential(user_name,pass_word,phone,email))   
                        print(f"SAVED SUCCESSFULLY! This are the details that will be stored in the application: {user_name} {pass_word} {phone} {email}")
                        print("*" * 50)
                        print("Enter    dc    to view your various account credentials and their passwords in the application")
         
            elif short_code == 'dc':

                            if display_credential():
                                    print("Here is a list of all your your various account credentials and their passwords in the application")

                                    for credential in display_credential():
                                            print(f"{credential.user_name} {credential.pass_word} .....{credential.number}  {credential.email}")
                                    print("*" * 50)
                            else:
                                    print("*" * 50)
                                    print("You dont seem to have all account credentials and their passwords to enable saving. Check if you inputted all the fields appropriately")
                                    print("*" * 50)
           
#Funtion to delete a credential's account that the user no longer needs in the applicatio
            elif short_code == "de":
                            print("Kindly note that an account deleted can NEVER be recovered!!")
                            print("Enter the account login name you wish to delete:...")
                            deleted_name = input()
                            # print(f"{deleted_name} has been deleted")
                            # if find_credential (deleted_name):
                            #     del_credential = find_credential (deleted_name)
                            print(f"The credentials {deleted_name} have been deleted")
                            print("*" * 50)

            elif short_code == "ex":
                            print("Bye, Hoping to see you next time")
            else:
                print("Invalid, please  use these short codes : ca - create a new account, da - display accounts, fa -find an account, de- delete account , gp - generate a random password , ex -logout")

main()  

