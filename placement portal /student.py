from data import load_data, save_data, append_data, STUDENTS_FILE
from models.student_model import Student
from utils import display_records, find_record


class StudentManager:

    FIELDNAMES = [
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

    # -------------------------
    # View All Students
    # -------------------------

    def view_students(self):

        students = load_data(STUDENTS_FILE)

        if not students:
            print("\nNo Students Found.")
            return

        display_records(students)

    # -------------------------
    # Search Student
    # -------------------------

    def search_student(self):

        student_id = input("Enter Student ID : ")

        students = load_data(STUDENTS_FILE)

        student = find_record(
            students,
            "student_id",
            student_id
        )

        if student:
            print()

            for key, value in student.items():
                print(f"{key:<15}: {value}")

        else:
            print("\nStudent Not Found.")

    # -------------------------
    # Update Student
    # -------------------------

    def update_student(self):

        student_id = input("Enter Student ID : ")

        students = load_data(STUDENTS_FILE)

        student = find_record(
            students,
            "student_id",
            student_id
        )

        if student is None:
            print("\nStudent Not Found.")
            return

        print("\nLeave blank to keep existing value.\n")

        name = input(f"Name ({student['name']}) : ")
        phone = input(f"Phone ({student['phone']}) : ")
        branch = input(f"Branch ({student['branch']}) : ")
        cgpa = input(f"CGPA ({student['cgpa']}) : ")
        skills = input(f"Skills ({student['skills']}) : ")

        if name:
            student["name"] = name

        if phone:
            student["phone"] = phone

        if branch:
            student["branch"] = branch

        if cgpa:
            student["cgpa"] = cgpa

        if skills:
            student["skills"] = skills

        save_data(
            STUDENTS_FILE,
            self.FIELDNAMES,
            students
        )

        print("\nStudent Updated Successfully.")

    # -------------------------
    # Delete Student
    # -------------------------

    def delete_student(self):

        student_id = input("Enter Student ID : ")

        students = load_data(STUDENTS_FILE)

        student = find_record(
            students,
            "student_id",
            student_id
        )

        if student is None:
            print("\nStudent Not Found.")
            return

        students.remove(student)

        save_data(
            STUDENTS_FILE,
            self.FIELDNAMES,
            students
        )

        print("\nStudent Deleted Successfully.")

    # -------------------------
    # View Student Profile
    # -------------------------

    def view_profile(self, student):

        print("\n========== PROFILE ==========\n")

        for key, value in student.items():
            print(f"{key:<15}: {value}")

    # -------------------------
    # Update Own Profile
    # -------------------------

    def update_profile(self, logged_student):

        students = load_data(STUDENTS_FILE)

        student = find_record(
            students,
            "student_id",
            logged_student["student_id"]
        )

        if student is None:
            return

        phone = input(f"Phone ({student['phone']}) : ")
        skills = input(f"Skills ({student['skills']}) : ")

        if phone:
            student["phone"] = phone

        if skills:
            student["skills"] = skills

        save_data(
            STUDENTS_FILE,
            self.FIELDNAMES,
            students
        )

        print("\nProfile Updated Successfully.")
# ---------------------------------
# Get Student By ID
# ---------------------------------

    def get_student_by_id(self, student_id):

      students = load_data(STUDENTS_FILE)

      return find_record(
        students,
        "student_id",
        student_id
       ) 


# ---------------------------------
# Mark Student as Placed
# ---------------------------------

    def mark_as_placed(self, student_id):

        students = load_data(STUDENTS_FILE)

        student = find_record(
        students,
        "student_id",
        student_id
    )

        if student:

            student["status"] = "Placed"

        save_data(
            STUDENTS_FILE,
            self.FIELDNAMES,
            students
        )

        return True

        return False