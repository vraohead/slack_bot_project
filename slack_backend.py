import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_USER_TOKEN = os.getenv("SLACK_USER_TOKEN")

@app.route('/slash', methods=['POST'])
def slack_slash_command():
    # Get the data from the Slack request
    data = request.form

    # Debug log to check the received data
    print(f"Received data: {data}")

    # Send the pop-up dialog to Slack using the Slack API
    trigger_id = data.get('trigger_id')
    dialog_data = {
        "trigger_id": trigger_id,
        "dialog": {
            "callback_id": "error_dialog",
            "title": "Error Dialog",
            "submit_label": "Submit",
            "elements": [
                {
                    "label": "Error Details",
                    "type": "textarea",
                    "name": "error_details",
                    "placeholder": "Enter error details here"
                }
            ]
        }
    }

    response = requests.post(
        'https://slack.com/api/dialog.open',
        headers={'Authorization': f'Bearer {SLACK_BOT_TOKEN}'},
        data=dialog_data
    )

    # Example response message
    response_text = f"Hello {data.get('user_name')}! You triggered the command: {data.get('command')}"

    # Return a response to Slack
    return jsonify({
        "response_type": "in_channel",  # Can also be "ephemeral" for private messages
        "text": response_text
    })

if __name__ == "__main__":
    # Start the Flask server
    app.run(host='0.0.0.0', port=3000)
