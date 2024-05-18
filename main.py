# app.py
import os
from flask import Flask, request, jsonify
from ultralytics import YOLO
import easyocr
from img_base64 import base64_converter
from image_processing import extract_and_save_text
from data_processing import process_extracted_data
from flask_cors import CORS 
import json 

app = Flask(__name__)
model = YOLO("best.pt")  # Load YOLO model once
CORS(app)

@app.route('/processed_data')
def get_processed_data():
  # Read data from processed_data.json file (replace with your logic)
  with open('processed_data.json', 'r') as f:
    data = json.load(f)
  return jsonify(data)

@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        image = request.files['img']
        image_path = os.path.join('temp', image.filename)
        image.save(image_path)

        extracted_data = extract_and_save_text(image_path)
        processed_data = process_extracted_data(extracted_data)

        # Include the image in the response as a Base64-encoded string for the "sign" folder
        # base64_converter(processed_data)

        return jsonify({"success": True, "data": processed_data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run()