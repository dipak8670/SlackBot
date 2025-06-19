from slack_sdk import WebClient
import os

client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
client.chat_postMessage(channel="#alerts", text=":fire: CPU usage crossed 90%!")
