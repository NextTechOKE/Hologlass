from flask import Flask, jsonify
from flask_cors import CORS

# app instance
app = Flask(__name__)
CORS(app)

summary = ""

def set_summary(text):
    global summary
    summary = text

# /api/text
@app.route("/api/text", methods=['GET'])
def return_summary():
    return jsonify({
        'message': summary,
    })

if __name__ == "__main__":
    app.run(debug=True, port=8080)

