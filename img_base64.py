import base64

def base64_converter(processed_data):
    if "sign" in processed_data and processed_data["sign"]:
        sign_image_path = processed_data["sign"]
        with open(sign_image_path, "rb") as image_file:
            sign_image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
            processed_data["sign_image_base64"] = sign_image_base64
