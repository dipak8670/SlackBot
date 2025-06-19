import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient
from dotenv import load_dotenv
load_dotenv()
# Initializes your app with your bot token
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
# Your command keyword
EXAMPLE_COMMAND = "do"
ALERT_COMMAND = "alert"
# Initialize web client (sending alerts)
client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
# Handle direct mentions (app_mention events)
@app.event("app_mention")
def handle_app_mention(event, say):
    user = event.get("user")
    text = event.get("text", "").lower()
    if ALERT_COMMAND in text:
        try:
            say(f"<@{user}> Sending Alerts...")
            client.chat_postMessage(channel="#alerts", text=":fire: CPU usage crossed 90%!")
            say(f"<@{user}> Alerts Sent! :+1:")
        except Exception as e:
            say(f"<@{user}> :-1: Unable to send alerts due to error:{e}")
    elif EXAMPLE_COMMAND in text:
        say(f"<@{user}> Sure... write some more code then I can do that!")
    else:
        say(f"<@{user}> Not sure what you mean. Try *{EXAMPLE_COMMAND}*.")
# Start the Socket Mode app
if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()