#### Filipe Carvalho Silva, 2024

import joblib
from flask import Flask, request, jsonify
import cv2
import base64
import numpy as np
import matplotlib.pyplot as plt
import os
os.listdir()
model = joblib.load('svc_classifier.pkl')

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    json_rec = request.get_json()
    print(json_rec)
    number = json_rec['number']

    result = {'return': number}

    return jsonify(result)

def decode_img(img_str):
    jpg_original = base64.b64decode(img_str)
    jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
    img = cv2.imdecode(jpg_as_np, flags=1)
    return img

@app.route('/predict', methods=['POST'])
def predict():
    img_json = request.get_json()
    img_str = img_json['image']
    img = decode_img(img_str)

    img_flat=[img.flatten()] 

    probability = model.predict_proba(img_flat)
    categories = ['airplane','automobile']
    result = {}

    for ind, val in enumerate(categories): 
        result[val+' prob'] = f'{round(probability[0][ind]*100, 2)}%'
    result['prediction'] = categories[model.predict(img_flat)[0]]

    return jsonify(result)

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)