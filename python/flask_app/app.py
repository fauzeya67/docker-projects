from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route for the website
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint
@app.route('/api/status', methods=['GET'])
def api_status():
    return jsonify({"message": "Server is up and running!", "status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
