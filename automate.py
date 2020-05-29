# you have to install twilio first on your machine.
# sudo pip install twilio (run this in terminal)(don't put sudo if using windows powershell)


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