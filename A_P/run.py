from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_hello():
    """Respond to incoming requests."""
    resp = VoiceResponse()
    msg = os.environ['TWL_VMESS']
    resp.say(msg*3)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
