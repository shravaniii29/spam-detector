# app.py — Flask API

import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('model/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

label_map = {0: 'normal', 1: 'spam'}

@app.route('/')
def home():
    return jsonify({
        "message": "Spam Detector API running",
        "usage": "POST /predict with JSON {text}"
    })

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "Missing text"}), 400

    text = data['text']
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]

    return jsonify({
        "input": text,
        "prediction": label_map[pred]
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)