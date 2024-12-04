import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import requests

# Load environment variables
load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")

app = Flask(__name__)

@app.route("/slash", methods=["POST"])
def handle_slash_command():
    data = request.form
    user_id = data.get("user_id")
    command = data.get("command")
    
    if command == "/error":
        response_url = data.get("response_url")
        message = f"Hello <@{user_id}>! You triggered the command: {command}"
        
        # Respond to Slack
        requests.post(response_url, json={
            "text": message,
        })
        return jsonify({"response_type": "ephemeral", "text": "Processing your request..."}), 200

    return jsonify({"text": "Command not recognized."}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
