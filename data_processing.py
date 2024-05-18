# data_processing.py
import re
import regex_helper
from datetime import datetime, timedelta

def process_extracted_data(extracted_data):
    if "account" in extracted_data:
        extracted_data["account"] = regex_helper.extract_account_number(extracted_data["account"])

    if "amount" in extracted_data:
        extracted_data["amount"] = regex_helper.extract_amount(extracted_data["amount"])

    if "amount_in_words" in extracted_data:
        extracted_data["amount_in_words"] = regex_helper.process_amount_in_words(extracted_data["amount_in_words"])

    if "date" in extracted_data:
        extracted_data["date"] = regex_helper.extract_date(extracted_data["date"])
        extracted_data["validity"] = regex_helper.process_date_information(extracted_data["date"])



    if "ifsc" in extracted_data:
        extracted_data["ifsc"] = regex_helper.extract_ifsc(extracted_data["ifsc"])

    return extracted_data
