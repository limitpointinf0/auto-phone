# auto_phone
Use Twilio to call all members on a calling list.


Step 1: modify call.py with necessary Twilio credentials

Step 2: create a calling list separated by a new line including country code

Step 3: run start.sh to create server and tunnel IP by ngrok

Step 4: run call.sh. It will ask you for the group name.
        For example you have have a text file called family.txt, the group name would be family
        It will then proceed to ask you for the amount of times to call everyone on the list
        and the pause time between iteration.
