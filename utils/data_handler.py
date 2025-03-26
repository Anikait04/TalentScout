# utils/data_handler.py
import re
import json
import os
from datetime import datetime

def validate_email(email):
    """Validate email format"""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone number format"""
    # Basic validation - can be enhanced based on requirements
    pattern = r'^\+?[0-9]{10,15}$'
    return re.match(pattern, phone) is not None

def save_candidate_data(candidate_data):
    """Save candidate data securely"""
    # In a real application, this would use proper encryption and database storage
    # For this demo, we'll use a simple JSON file with timestamp
    
    os.makedirs("data", exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/candidate_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(candidate_data, f, indent=4)
    
    return filename
