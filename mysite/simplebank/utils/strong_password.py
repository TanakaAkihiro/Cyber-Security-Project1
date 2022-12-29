import re

def is_strong_password(password):
    conditions = [
        len(password) >= 8,
        re.search(r'[a-z]', password), 
        re.search(r'[A-Z]', password), 
        re.search(r'[0-9]', password), 
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    ]
    
    for condition in conditions:
        if not condition:
            return False

    return True
