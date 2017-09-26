import twilio
from twilio.rest import TwilioRestClient
# Find these values at https://twilio.com/user/account
account_sid = ""
auth_token = ""
client = TwilioRestClient(account_sid,auth_token) 
msg=str(input())
client.messages.create(
    to="", 
    from_="",
    body=msg), 
 )
 print("done")
