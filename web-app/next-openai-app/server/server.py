from flask import Flask, jsonify
from flask_cors import CORS

# app instance
app = Flask(__name__)
CORS(app)


# /api/text
@app.route("/api/text", methods=['GET'])
def return_summary(summary):
    print("trying to return your summary...")
    with app.app_context():
        if summary != "":
            return jsonify({
                'message': summary,
            })

if __name__ == "__main__":
    app.run(debug=True, port=8080)

