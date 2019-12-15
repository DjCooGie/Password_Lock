#! /usr/bin/env python3.6

from user import User
from credentials import Credential

def create_user(username,password):
    '''
    Creates a new user account
    '''
    new_user = User(username,password)                                     
    return new_user

def save_user(user):
    '''
    Saves a new user account
    '''
    User.save_user(user)


def confirm_user(username,password):
    '''
    function that verifies the existance of the user before create
    '''
    verifying_user = Credential.verify_user(username,password)
    return verifying_user

def generate_password():
    '''
    Generates a passsword automatically
    '''
    gen_pass = Credential.generate_password()
    return gen_pass

def create_credetial(username,sitename,accountname,password):
    '''
    Creates a new creditional
    '''
    new_credential = Credential(username,sitename,accountname,password)
    return new_credential
    
def save_credential(credential):
	'''
	Saves a newly created credential
	'''
	Credential.save_credentials(credential)
    
def output_credentials(username):
	'''
	Displays saved credentials
	'''
	return Credential.output_credentials(username)

def main():
    print(' ')
    print('Bonjour! Welcome to PassTheLock.')
    while True:
        print(' ')
        print("-"*50)
        print('Use these short-codes to navigate: \n ca-Create new Account \n li-Log In \n ex-Exit')
        short_code = input('Enter short-code: ').lower().strip()
        if short_code == 'ex':
            break

        elif short_code == 'ca':
            print("-"*50)
            print(' ')
            print('To create new user account:')
            username = input('Enter your username - ').strip()
            password = input('Create new password - ').strip()
            save_user(create_user(username,password))
            print(" ")
            print(f'New Account Created Successfully \n Account: {username} using: {password}')
        elif short_code == 'li':
            print("-"*50)
            print(' ')
            print('To login, enter your details:')
            username = input('Enter username - ').strip()
            password = str(input('Enter password - '))
            user_exists = confirm_user(username,password)
            if user_exists == username:
                print(" ")
                print(f'Welcome {username}. Kindly enter short-code  to continue.')
                print(' ')
                while True:
                    print("-"*50)
                    print('Short-codes: \n cc-Create new credential \n rc-Retrieve credentials \n ex-Exit')
                    short_code = input('Enter short-code: ').lower().strip()
                    print("-"*50)
                    if short_code == 'ex':
                        print(" ")
                        print(f'Bon Voyage {username}')
                        break
                    elif short_code == 'cc':
                        print(' ')
                        print('Enter your credential details:')
                        sitename = input('Enter site\'s name - ').strip()
                        accountname = input('Enter site\'s accountname - ').strip()
                        while True:
                            print(' ')
                            print("-"*50)
                            print('Kindly choose short-code for entering a password: \n ep-Enter existing password \n gp-Generate a password \n ex-Exit')
                            passcode = input('Enter short-code: ').lower().strip()
                            print("-"*50)
                            if passcode == 'ep':
                                print(" ")
                                password = input('Enter password: ').strip()
                                break
                            elif passcode == 'gp':
                                password = generate_password()
                                break
                            elif passcode == 'ex':
                                break
                            else:
                                print('Hell no! Wrong code. Re-enter short-code.')
                        save_credential(create_credential(username,sitename,accountname,password))
                        print(' ')
                        print(f'Credential created successfully \n Site Name: {sitename} \n Account Name: {accountname} \n Password: {password}')
                        print(' ')
                    elif short_code == 'rc':
                        print(' ')
                        if output_credentials(username):
                            print('Have a look on the list of your credentials')
                            print(' ')
                            for credential in output_credentials(username):
                                print(f'Site Name: {credential.sitename} \n Account Name: {credential.accountname} \n Password: {credential.password}')
                            print(' ')
                        else:
                            print(' ')
                            print("No saved credentials. Add some.")
                            print(' ')
                    else:
                        print('Hell no! Wrong code. Try again.')

            else:
                print(' ')
                print('Hell no! Worng user details. Try again or Create new account.')

        else:
            print("-"*50)
            print(' ')
            print('Hold up! Wrong code. Re-enter the short-code.')        













if __name__ == '__main__':
    main()