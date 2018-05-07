import datetime
import traceback

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
phone_no = "XXXXXXXXXXXX"
client = Client(account_sid, auth_token)

def call_them(start_time, call_list, interval=300, times=5):
    global phone_no
    for t in range(times):
        try:
            for i in call_list:
                call = client.calls.create(
                    to=i,
                    from_=phone_no,
                    url=URL
                )
                print(call.sid, datetime.datetime.now())
            time.sleep(interval)
        except:
            print(traceback.format_exc())


if __name__ == '__main__':
    with open('url.txt','r') as g:
        URL = g.read()
    
    GROUP = input('Group: ')
    INTERVAL = int(input('Interval (s): '))
    TIMES = int(input('Times (s):'))

    with open('groups/' + GROUP + '.txt') as f:
        text = f.read()
    call_list = text.split('\n')

    call_them(time.time(), call_list, interval=INTERVAL, times=TIMES)
