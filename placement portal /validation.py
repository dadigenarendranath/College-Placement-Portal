import re


# ---------------------------------
# Name Validation
# ---------------------------------

def validate_name(name):

    if len(name.strip()) < 3:
        return False

    return all(ch.isalpha() or ch.isspace() for ch in name)


# ---------------------------------
# Email Validation
# ---------------------------------

def validate_email(email):

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    return bool(re.match(pattern, email))


# ---------------------------------
# Phone Validation
# ---------------------------------

def validate_phone(phone):

    return phone.isdigit() and len(phone) == 10


# ---------------------------------
# Password Validation
# ---------------------------------

def validate_password(password):

    return len(password) >= 6


# ---------------------------------
# Branch Validation
# ---------------------------------

def validate_branch(branch):

    branches = [
        "CSE",
        "IT",
        "ECE",
        "EEE",
        "MECH",
        "CIVIL",
        "AIML",
        "DS"
    ]

    return branch.upper() in branches


# ---------------------------------
# CGPA Validation
# ---------------------------------

def validate_cgpa(cgpa):

    try:
        cgpa = float(cgpa)
        return 0 <= cgpa <= 10

    except ValueError:
        return False


# ---------------------------------
# Package Validation
# ---------------------------------

def validate_package(package):

    try:
        return float(package) > 0

    except ValueError:
        return False


# ---------------------------------
# Openings Validation
# ---------------------------------

def validate_openings(openings):

    return openings.isdigit() and int(openings) > 0


# ---------------------------------
# Date Validation
# Format: DD-MM-YYYY
# ---------------------------------

def validate_date(date):

    pattern = r'^\d{2}-\d{2}-\d{4}$'

    return bool(re.match(pattern, date))


# ---------------------------------
# Menu Choice Validation
# ---------------------------------

def validate_choice(choice, minimum, maximum):

    if not choice.isdigit():
        return False

    choice = int(choice)

    return minimum <= choice <= maximum
import re

def validate_skills(skills):

    skills = skills.strip()

    if skills == "":
        return False

    pattern = r'^[A-Za-z0-9+#,\s]+$'

    return bool(re.fullmatch(pattern, skills))