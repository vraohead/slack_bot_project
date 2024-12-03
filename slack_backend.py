<<<<<<< HEAD
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/slash', methods=['POST'])
def slack_slash_command():
    # Get the data from the Slack request
    data = request.form

    # Example: Respond with a simple message
    response_text = f"Hello! You triggered the command: {data.get('command')}"

    # Return a response to Slack with response_type set to 'ephemeral'
    return jsonify({
        "response_type": "ephemeral",  # This makes the response private to the user
        "text": response_text
    })

if __name__ == "__main__":
    # Start the Flask server
    app.run(host='0.0.0.0', port=3000)
=======
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/slash', methods=['POST'])
def slack_slash_command():
    data = request.form
    response_text = f"Hello! You triggered the command: {data.get('command')}"
    return jsonify({
        "response_type": "in_channel",
        "text": response_text
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))  # Use Render's port or default to 3000
    app.run(host='0.0.0.0', port=port)

>>>>>>> 22281af46ae602ac961ea00040b302279abac906
