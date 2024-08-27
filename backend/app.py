from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

# Display the home page of the API
@app.route("/", method=["GET"], strict_slashes=False)
def home():
    return jsonify({"message": "Welcome to AfyaSync core API"})

# run the Flask app in debug mode
if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True, host=host, port=port)
