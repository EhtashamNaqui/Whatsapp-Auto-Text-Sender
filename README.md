# Whatsapp-Auto-Text-Sender
This Repository will help you to automate a text message to a specific phone number at a specific time duration on WhatsApp messenger.

## Prerequisites:
- Copy all the files in this repository except _pycache_ to a folder and open VS Code or any other IDE in that folder.
- twilio (https://www.twilio.com)
- Advance Python Scheduler (https://apscheduler.readthedocs.io/en/stable/)
    - Install Guide (https://apscheduler.readthedocs.io/en/stable/userguide.html)
- Heroku (https://www.heroku.com)

You can also use `pip` to install heroku and aps -

#### For Heroku -
> **Linux:** `$ sudo pip install heroku`

> **Windows:** `> pip install heroku`

#### For APS -
> **Linux:** `$ sudo pip install apscheduler`

> **Windows:** `> pip install apscheduler`

## Getting Started:

### STEP 1 - We have to make an account in twilio:
1. Go to https://www.twilio.com and sign up and verify your account.
2. After that go to All Programs and Services > Programmable SMS > WhatsApp under WhatsApp.
3. Send the exact same message from the phone you want to get messages on to the exact number(ALL GIVEN).
4. You can now test the framework by going to appointment reminder and pressing make request after clicking reminder option.
5. Now on the right hand side under request select Python from drop-down menu and copy the authentication code and SID.
6. Now replace the asterics (*) with the `AUTH_CODE` and `SID` copied earlier.

Code in `automate.py` -
```python
from twilio.rest import Client 
# put your twilio account SID and auth_token below. 
account_sid = '*******************************' 
auth_token = '********************************' 
client = Client(account_sid, auth_token) 
# define a function eg. send_text
def send_text(): 
    message = client.messages.create( 
                              from_='whatsapp:+1TWILIO SAND BOX BOT PHONE NUMBER',  
                              body='YOUR MESSAGE',      
                              to='whatsapp:+91YOUR PHONE NUMBER' 
                          ) 
 
    print(message.sid)
```

### STEP 2 - We have to use interval function of Advance Python Scheduler:

Code in `clock.py` -
```python
from apscheduler.schedulers.blocking import BlockingScheduler
from automate import send_text
# Here send_text is the function you already created in automation.py

sched = BlockingScheduler()

# Schedule job_function to be called every two hours (set according to your need)
sched.add_job(send_text, 'interval', hours=2)

sched.start()
```

### STEP 3 - Setting-up Heroku:
1. We have to make an account on Heroku.
2. After successful login, inside the dashboard go to New > Create New App.
3. Give some cool name and press Create App.
4. After that you have to install Heroku CLI.
5. According to your OS consider this - https://devcenter.Heroku.Com/articles/heroku-cli.

You can install Heroku CLI with commands below -

> **Ubuntu (Linux):** `$ sudo snap install --classic heroku` (terminal)

> **Mac:** `$ brew tap heroku/brew && brew install heroku` (terminal)

> **Windows (64-bit):** https://cli-assets.Heroku.Com/heroku-x64.Exe (browser)

> **Windows (32-bit):** https://cli-assets.Heroku.Com/heroku-x86.Exe (browser)

6. After installing the Heroku CLI, log-in to your Heroku account and follow the prompts to create a new SSH public key.
7. Run `heroku login` command in your OS's respective terminal.

### Step 4 - Settinp-up Heroku Server:
- For the server side we need two things:
    1. Creating a list of dependencies (which is requirements.txt)
    2. Procfile

These two files are already creeated in the repo for you.

### Step 5 - Setting-up git:
1. Initialise the git in current directory by running - `git init`
2. Clone this repository
3. Use git to clone whatsapp-automatic-text's source code to your local machine.
```bash
$ heroku git:clone -a whatsapp-automatic-text
$ cd whatsapp-automatic-text
```
4. Make your own modifications to the code you just cloned and deploy them to Heroku using git.
```bash
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
---
### All Done !! Enjoy the power of automation !
### Give a :star: if you like my work.
