import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import requests

# Load environment variables from .env file
load_dotenv()

# Get the Slack bot token from the environment
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

app = Flask(__name__)

@app.route('/slash', methods=['POST'])
def slack_slash_command():
    data = request.form

    # Responding to the /error command
    response_text = f"Hello {data.get('user_name')}! You triggered the command: /error"
    
    # Send the response to Slack
    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    response = {
        "response_type": "in_channel",  # Make this "ephemeral" for private messages
        "text": response_text
    }

    # Post the message to Slack
    slack_api_url = "https://slack.com/api/chat.postMessage"
    payload = {
        "channel": data.get("channel_id"),
        "text": response_text
    }
    requests.post(slack_api_url, headers=headers, json=payload)

    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
