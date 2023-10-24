import re


def validate_password(password: str):
    assert len(password) >= 8, 'Password must be at least 8 characters'
    return password


def validate_email_by_regex(email: str):
    assert re.match(r"[^@]+@[^@]+\.[^@]+", email), 'Invalid email'
    return email
