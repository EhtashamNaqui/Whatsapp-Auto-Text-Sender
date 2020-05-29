# Whatsapp-Auto-Text-Sender
This Repository will help you to automate a text message to a specific phone number at a specific time duraction.
###### prerequisites:
## All the files in this repository except _pycache_ 
# copy them to a folder and open VS Code or any other IDE in that folder.
## twilio (https://www.twilio.com)

## advance python scheduler (https://apscheduler.readthedocs.io/en/stable/)
## install guide (https://apscheduler.readthedocs.io/en/stable/userguide.html)

## heroku (https://www.heroku.com)


you have to install heroku 
use terminal/powershell
linux : $ sudo pip install heroku
windows : $ pip install heroku


you have to install advance python scheduler 
$ pip install apscheduler

(If you don’t have pip installed, you can easily install it by downloading and running get-pip.py.
If, for some reason, pip won’t work, you can manually download the APScheduler distribution from PyPI, extract and then install it:
$ python setup.py install)

### Method
###### STEP 1 - we have to make an accont in twilio 
go to www.twilio.com and sign up and verify your account.
after that go to all program and services>programmable SMS>WhatsApp
under WhatsApp
# send the exact same message from the phone you want to get messages on to the exact number(ALL GIVEN)
YOU CAN NOW TEST THE FRAMEWORK BY GOING TO APPOINTMENT REMINDER AND PRESSING MAKE REQUEST
AFTER CLICKING REMINDER OPTION
# NOW ON THE RIGHT HAND SIDE UNDER REQUEST SELECT PYTHON FROM THE DROP DOWN MENU AND COPY THE AUTHENTICATION CODE AND SID. 

# NOW PUT THE AUTH_CODE AND SID COPIED EARLIER INSTEAD OF ASTERICS (*)

# NOTE - THIS IS THE EXACT SAME CODE USED IN AUTOMATE.PY
{(((((((
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
))))))))}



###### STEP 2
we have to use interval function of advance python scheduler

# NOTE - THIS IS THE EXACT SAME CODE USED IN CLOCK.PY

https://apscheduler.readthedocs.io/en/stable/modules/triggers/interval.html#module-apscheduler.triggers.interval
[
# EXAMPLE below is the code used in clock.py :
from apscheduler.schedulers.blocking import BlockingScheduler
from automate import send_text
# Here send_text is the function you already created in automation.py



sched = BlockingScheduler()

# Schedule job_function to be called every two hours (set according to your need)
sched.add_job(send_text, 'interval', hours=2)

sched.start()
]

## STEP 3
WE HAVE TO MAKE AN ACCOUNT ON HEROKU
AFTER SUCCESSFUL LOGIN 
IN SIDE THE DASH BOARD GO TO NEW>CREATE NEW APP 
GIVE SOME NAME AND PRESS CREATE APP
AFTER THAT YOU HAVE TO INSTALL HEROKU CLI
ACCORDING TO YOUR OS CONSIDER THIS - https://devcenter.heroku.com/articles/heroku-cli
UBUNTU - $ sudo snap install --classic heroku (TERMINAL)
MAC - $ brew tap heroku/brew && brew install heroku (TERMINAL)
WINDOWS 64BIT - https://cli-assets.heroku.com/heroku-x64.exe (BROWSER)
WINDOWS 32BIT - https://cli-assets.heroku.com/heroku-x86.exe (BROWSER)

# after installing the Heroku CLI
log in to your Heroku account and follow the prompts to create a new SSH public key.

$ heroku login
###### step 4
# for the server side we need two things :- 1. creating list of dependencies (which is requirements.txt) 2. Procfile

###### step 5 
initialise the git by
$ git init
Clone the repository
Use Git to clone whatsapp-automatic-text's source code to your local machine.

$ heroku git:clone -a whatsapp-automatic-text
$ cd whatsapp-automatic-text
Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

$ git add .
$ git commit -am "make it better"
$ git push heroku master

#AFTER PUSHING 
