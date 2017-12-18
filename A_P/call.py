# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "XXXXXXXXXXXXXXXXXX"
auth_token = "XXXXXXXXXXXXXXXXXX"
client = Client(account_sid, auth_token)

with open('url.txt','r') as g:
    URL = g.read()
GROUP=input('Group: ')

with open('groups/' + GROUP + '.txt') as f:
    text = f.read()
call_list = text.split('\n')
for i in call_list:
    call = client.calls.create(
        to=i,
        from_="+1XXXXXXXXXX",
        url=URL
    )
    print(call.sid)
