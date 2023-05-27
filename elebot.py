import slack
import math
from flask import Flask
from slackeventsapi import SlackEventAdapter

SLACK_TOKEN = "xoxb-4910565592977-5006011642837-NT3OQCTu95vVnPA8GfJdZ5p1"
SIGNING_SECRET = "ab2046aff9b995288c65f1e98a712096"

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)
client = slack.WebClient(token=SLACK_TOKEN)

x = []
V1 = 0
V2 = 0
R1 = 0
R0 = 0
B = 0


@ slack_event_adapter.on('message')



def message(payload):
    print(payload)
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
 
    x = text.split(' ')
    
    global V1 
    global V2 
    global R1 
    global R0 
    global B 


    if text == "!elebot":
        client.chat_postMessage(channel = channel_id, text ="Please enter the input voltage (in volts) like so: V1 = <its value>")
        
    
    if x[0] == "V1":
        V1 = float(x[2])
        client.chat_postMessage(channel = channel_id, text ="Please enter the output voltage (in volts) like so: V2 = <its value>")

    if x[0] == "V2":
        V2 = float(x[2])
        client.chat_postMessage(channel = channel_id, text ="Please enter the resistance of the independent resistor (in ohms) like so: R1 = <its value>")

    if x[0] == "R1":
        R1 = float(x[2])
        client.chat_postMessage(channel = channel_id, text = "Please enter the standard resistance of dependent thermistor (in ohms) like so: R0 = <its value>")

    if x[0] == "R0":
        R0 = float(x[2])
        client.chat_postMessage(channel = channel_id, text = "Please Enter the temperature parameter like so: B = <its value>")

    if x[0] == "B":
        B = float(x[2])
        R2 = ((R1*V1)/V2)-R1
        Temp = 1/((1/25)+((1/B)*(math.log(abs(R2/R0)))))
        output = "The temperature of the resistor under these conditions is " + str(Temp) + " degrees"
        client.chat_postMessage(channel = channel_id, text = output)



if __name__ == "__main__":
    app.run(debug=True)