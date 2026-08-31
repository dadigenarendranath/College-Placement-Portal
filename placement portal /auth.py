from data import (
    load_data,
    append_data,
    STUDENTS_FILE,
    ADMINS_FILE
)

from models.student_model import Student

from validation import (
    validate_name,
    validate_email,
    validate_phone,
    validate_password,
    validate_branch,
    validate_cgpa
)

from utils import generate_id


# ----------------------------------------
# Admin Login
# ----------------------------------------

def admin_login():

    username = input("Username : ")
    password = input("Password : ")

    admins = load_data(ADMINS_FILE)

    for admin in admins:

        if admin["username"] == username and admin["password"] == password:
            print("\nLogin Successful")
            return True

    print("\nInvalid Username or Password")
    return False


# ----------------------------------------
# Student Registration
# ----------------------------------------

def student_register():

    students = load_data(STUDENTS_FILE)

    student_id = generate_id(students, "STU")

    print("\n===== Student Registration =====")

    name = input("Name : ")

    if not validate_name(name):
        print("Invalid Name")
        return

    email = input("Email : ")

    if not validate_email(email):
        print("Invalid Email")
        return

    # Duplicate Email Check
    for student in students:

        if student["email"] == email:
            print("Email Already Exists")
            return

    phone = input("Phone : ")

    if not validate_phone(phone):
        print("Invalid Phone Number")
        return

    branch = input("Branch : ").upper()

    if not validate_branch(branch):
        print("Invalid Branch")
        return

    cgpa = input("CGPA : ")

    if not validate_cgpa(cgpa):
        print("Invalid CGPA")
        return

    skills = input("Skills (comma separated): ")

    password = input("Password : ")

    if not validate_password(password):
        print("Password must contain at least 6 characters.")
        return

    student = Student(
        student_id,
        name,
        email,
        phone,
        branch,
        cgpa,
        skills,
        password
    )

    fieldnames = [
        "student_id",
        "name",
        "email",
        "phone",
        "branch",
        "cgpa",
        "skills",
        "password",
        "status"
    ]

    append_data(
        STUDENTS_FILE,
        fieldnames,
        student.to_dict()
    )

    print("\nRegistration Successful")
    print("Student ID :", student_id)


# ----------------------------------------
# Student Login
# ----------------------------------------

def student_login():

    email = input("Email : ")
    password = input("Password : ")

    students = load_data(STUDENTS_FILE)

    for student in students:

        if student["email"] == email and student["password"] == password:

            print("\nLogin Successful")
            return student

    print("\nInvalid Email or Password")
    return None