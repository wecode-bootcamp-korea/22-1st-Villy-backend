import re

def validate_name(name):
    result = re.match(
        r'[a-zA-Z0-9가-힇]',
        name
    )
    return result

def validate_mobile(mobile):
    result = re.match(
        r'^01[0|1|2|7|8|9]-[0-9]{3,4}-[0-9]{4}$',
        mobile
    )
    return result

def validate_email(email):
    result = re.match(
        r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        email
    )
    return result

def validate_password(password):
    result = re.match(
        r'^(?=.*\d)(?=.*[a-z])(?=.*[!@#$%^&*_(.,)?])[a-zA-Z\d!@#$-_+.,%^&*()?]{6,20}$',
        password
    )
    return result
