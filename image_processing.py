# image_processing.py
from ultralytics import YOLO
import easyocr
import os
import json

# Load YOLO model once
model = YOLO("best.pt")

def extract_and_save_text(image_path):
    image_name, _ = os.path.splitext(os.path.basename(image_path))
    output_dir = "output"  # Adjust if needed
    image_folder = os.path.join(output_dir, image_name)

    model.predict(source=image_path, project=image_folder, show=True, save=True, conf=0.5, save_crop=True)

    extracted_data = {}
    crop_folders = ["account", "amount", "amount_in_words", "date", "ifsc", "name", "sign"]

    for crop_folder in crop_folders:
        crop_path = os.path.join(image_folder, "predict", "crops", crop_folder, image_name + ".jpg")

        if crop_folder == "sign":
            extracted_data["is_signature"] = os.path.exists(crop_path)
        else:
            if os.path.exists(crop_path):
                reader = easyocr.Reader(['en'])
                result = reader.readtext(crop_path)
                text = " ".join([line[1] for line in result])
                extracted_data[crop_folder] = text
            else:
                extracted_data[crop_folder] = None

    
    output_dir = "output"  # Adjust if needed
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define the path for the JSON file
    json_file_path = os.path.join(output_dir, "processed_data.json")

    # Write processed data to the JSON file
    with open(json_file_path, "w") as json_file:
        json.dump(extracted_data, json_file, indent=4)

    return extracted_data
