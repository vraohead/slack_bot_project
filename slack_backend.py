import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to send a modal to Slack using the trigger_id
def send_modal(trigger_id, user_id):
    url = 'https://slack.com/api/views.open'
    headers = {
        'Authorization': 'Bearer xoxb-your-slack-token',  # Use your Slack bot token here
        'Content-Type': 'application/json',
    }
    data = {
        "trigger_id": trigger_id,
        "view": {
            "type": "modal",
            "callback_id": "modal-identifier",
            "title": {
                "type": "plain_text",
                "text": "My Modal"
            },
            "blocks": [
                {
                    "type": "section",
                    "block_id": "section-identifier",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"Hello {user_id}, you triggered the command!"
                    }
                }
            ]
        }
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())  # For debugging

@app.route('/slash', methods=['POST'])
def slack_slash_command():
    # Get the data from the Slack request
    data = request.form
    print(f"Received data: {data}")  # For debugging

    # Call the send_modal function to trigger the modal
    send_modal(data.get('trigger_id'), data.get('user_id'))

    # Respond back to Slack (even though a modal will be triggered)
    response_text = f"Hello {data.get('user_name')}! You triggered the command: {data.get('command')}"
    return jsonify({
        "response_type": "ephemeral",  # This can still be a private message if needed
        "text": response_text
    })

if __name__ == "__main__":
    # Start the Flask server
    app.run(host='0.0.0.0', port=3000)
