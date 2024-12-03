from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)

@app.route('/slash', methods=['POST'])
def slack_slash_command():
    # Log the incoming request data for debugging purposes
    data = request.form
    app.logger.debug("Received data: %s", data)

    # Check if the necessary fields are present in the request
    if 'command' not in data:
        return jsonify({
            "response_type": "ephemeral",  # Private response
            "text": "Error: No command found in the request"
        })

    # Example: Respond with a simple message
    response_text = f"Hello! You triggered the command: {data.get('command')}"

    # Return a response to Slack
    return jsonify({
        "response_type": "in_channel",  # Visible in the channel
        "text": response_text
    })

if __name__ == "__main__":
    # Start the Flask server on all IPs (needed for Render)
    app.run(host='0.0.0.0', port=3000)
