# auto_phone
Use Twilio to call all members on a calling list.


Step 1: Create a settings.py file containing the following with Twilio credentials filled in:

TEST = {
	'SID':"xxxxxxxxxxxxxxxxxxxxxxxx",
	'ATOKEN':"xxxxxxxxxxxxxxxxxxxxxxxx",
	'PHONE':"+xxxxxxxxx"
}

REAL = {
	'SID':"xxxxxxxxxxxxxxxxxxxxxxxx",
	'ATOKEN':"xxxxxxxxxxxxxxxxxxxxxxxx",
	'PHONE':"+xxxxxxxxx"
}

MESSAGE = {
	'SAY':"Message goes here. "
}

Step 2: Run run.py

Step 3: In a separate terminal run the command "ngrok http 5000" 

Step 4: Run get_tun.py

Step 5: Run call.py