import datetime
import traceback
from twilio.rest import Client
from send_waves import *
import os

def get_group(group):
    with open('groups/%s.txt' % group) as f:
        text = f.read()
    rows = text.split('\n')
    call_list = [r.split('\t') for r in rows]
    return call_list

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--group', help='name of group found in groups directory')
    parser.add_argument('-u', '--url', help='url to message')
    args = parser.parse_args()
    
    client = Client(os.environ['TWL_SID'], os.environ['TWL_TOKEN'])
    call_list = get_group(args.group)
    
    for c in call_list:
        phone = phoneCall(c[1], c[0], os.environ['TWL_PHONE'], args.url, client)
