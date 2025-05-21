from flask import Flask, jsonify, render_template
from os import path
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/incidents')
def incidents():
    data_file = path.join(path.dirname(__file__), '..', 'data', 'sample_incidents.json')
    try:
        with open(data_file, 'r') as f:
            incidents = json.load(f)
    except Exception:
        incidents = []
    # In a real scenario, you would classify the incidents here!
    return jsonify(incidents)

if __name__ == '__main__':
    app.run(debug=True)
