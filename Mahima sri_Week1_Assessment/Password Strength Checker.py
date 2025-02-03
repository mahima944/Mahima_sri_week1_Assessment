import re

def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return bool(re.search(r'[A-Z]', password))

def check_lowercase(password):
    return bool(re.search(r'[a-z]', password))

def check_digit(password):
    return bool(re.search(r'\d', password))

def check_special_character(password):
    return bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

def password_strength_checker(password):
    criteria = {
        "Length": check_length(password),
        "Uppercase": check_uppercase(password),
        "Lowercase": check_lowercase(password),
        "Digit": check_digit(password),
        "Special Character": check_special_character(password)
    }

    if all(criteria.values()):
        return "Strong password"
    else:
        weak_criteria = [key for key, value in criteria.items() if not value]
        return f"Weak password. Missing criteria: {', '.join(weak_criteria)}"


password = input("Enter a password to check its strength: ")
result = password_strength_checker(password)
print(result)

