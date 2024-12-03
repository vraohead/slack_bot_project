from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/slash', methods=['POST'])
def slack_slash_command():
    # Get the data from the Slack request
    data = request.form

    # Example: Respond with a simple message
    response_text = f"Hello! You triggered the command: {data.get('command')}"

    # Return a response to Slack
    return jsonify({
        "response_type": "in_channel",  # Can also be "ephemeral" for private messages
        "text": response_text
    })

if __name__ == "__main__":
    # Start the Flask server
    app.run(host='0.0.0.0', port=3000)
