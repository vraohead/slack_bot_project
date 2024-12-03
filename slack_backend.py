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

