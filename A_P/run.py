from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = VoiceResponse()
    with open('msg.txt','r') as f:
        msg = f.read()
    resp.say(msg*3)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
