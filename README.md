# PassTheLock
PassTheLock is an application that manages user crendentials. i.e it saves different account passwords and usernames.

## Author
* Evans Nyambane

### SetUp / Installation Requirements
* python3.6
* pip
* pyperclip

* #### Cloning
Navigate into the folder you want the application to be
In your terminal;
  > $ git clone https://github.com/DjCooGie/Password_Lock.git
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
| Display short-codes for navigation | **In terminal: $./pass_lock.py** | Welcome, enter a short-code: ca-Create Account, li-Log In, ex-Exit |
| Displays prompt for creating an account | **Enter: ca** | Enter username and password |
| Displasys prompt for login in | **Enter: li** | Enter your account name and password |
| Displays short-codes for navigation | **Successful login** | Choose short-code: cc - Create Credential, rc - Display Credentials, ex - Exit |
| Displays prompt for creating a credential | **Enter: cc** | Enter the site name, your username and password |
| Displays a list of credentials | **Enter: rc** | Prints a list of saved credentials |
| Exit app | **Enter: ex** | Exit the app |

#### Known Bugs
No known bugs

#### Collaborate
>Incase of any questions, problems ideas concerning the website, feel free to reach out to me:
>>Github: [Evans Nyambane](https://github.com/DjCooGie)
>>Email: evansonchagwa01@gmail.com

#### License
MIT
&copy;2019 Evans Nyambane


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.