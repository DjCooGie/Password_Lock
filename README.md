# PassTheLock
PassTheLock is an application that manages user crendentials. i.e it saves different account passwords and usernames.

## Author
* Evans Onchagwa

### SetUp / Installation Requirements
* python3.6
* pip
* pyperclip

* #### Cloning
Navigate into the folder you want the application to be
In your terminal;
  > $ git clone https://github.com/jusinam/Password_Lock.git
  > 
  > $ cd PassTheLock

#### Running the application
* In your terminal;
    $ chmod +x pass_lock.py
    $ ./pass_lock.py

## Testing the Application
* To run the tests for the class files:
    $ python3.6 user_test.py
    $ python3.6 credentials_test.py

#### Technologies used
Python3.6

#### BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Displays short-codes for navigation | **In terminal: $./pass_lock.py** | Welcome, enter a short-code: ca-Create Account, li-Log In, ex-Exit |
| Displays prompt for creating an account | **Enter: ca** | Enter username and password |
| Displays prompt for login in | **Enter: li** | Enter your account name and password |
| Displays short-codes for navigation | **Successful login** | Choose short-code: cc - Create Credential, rc - Display Credentials, ex - Exit |
| Displays prompt for creating a credential | **Enter: cc** | Enter the site name, your username and password |
| Displays a list of credentials | **Enter: rc** | Prints a list of saved credentials |
| Exit app | **Enter: ex** | Exit the app |

#### Known Bugs
No known bugs

#### Collaborate
>Incase of any questions, problems ideas concerning the app, feel free to reach out to me:
>>Github: [Evans Onchagwa](https://github.com/jusinam)
>>Email: evansonchagwa01@gmail.com

#### License
MIT
&copy;2019 Evans Onchagwa
