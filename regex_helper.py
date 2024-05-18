import re
from datetime import datetime, timedelta
def extract_account_number(account):
    match = re.search(r'\b(\d{11})\b', account)
    return match.group(1) if match else None

def extract_amount(amount):
    return "".join(filter(str.isdigit, amount)) if amount else None

def process_amount_in_words(amount_in_words):
    if "only" in amount_in_words.lower():
        only_index = amount_in_words.lower().find("only")
        return amount_in_words[:only_index + len("Only")].strip() if only_index != -1 else amount_in_words.strip()
    return amount_in_words.strip()

def extract_date(date):
    date_match = re.search(r'\b(\d{2}\d{2}\d{4})\b', date)
    return date_match.group(1) if date_match else None

def process_date_information(date_str):
    def days_from_current_date(date_str):
        if date_str:
            date_format = "%d%m%Y"
            today = datetime.now().date()
            extracted_date = datetime.strptime(date_str, date_format).date()

            if extracted_date >= today:
                return (extracted_date - today).days
            else:
                return "expired"
        return None

    if date_str:
        date_match = re.search(r'\b(\d{2}\d{2}\d{4})\b', date_str)
        extracted_date_str = date_match.group(1) if date_match else None

        if extracted_date_str:
            date_format = "%d%m%Y"
            today = datetime.now().date()
            extracted_date = datetime.strptime(extracted_date_str, date_format).date()
            days_difference = (extracted_date - today).days

            is_within_90_days = 0 <= days_difference <= 90
            days_from_current = days_difference if is_within_90_days else "expired"
            days_since_expiry = None if is_within_90_days else abs(days_difference)

            return {
                "is_within_90_days": is_within_90_days,
                "days_from_current": days_from_current,
                "days_since_expiry": days_since_expiry
            }

    return {
        "is_within_90_days": None,
        "days_from_current": None,
        "days_since_expiry": None
    }
def extract_ifsc(ifsc):
    ifsc_match = re.search(r'[A-Za-z]{4}\d{6}', ifsc)
    return ifsc_match.group() if ifsc_match else None
