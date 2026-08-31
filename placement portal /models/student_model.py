from models.person import Person


class Student(Person):

    def __init__(self, student_id, name, email, phone,
                 branch, cgpa, skills, password,
                 status="Not Placed"):

        super().__init__(name, email, password)

        self.student_id = student_id
        self.phone = phone
        self.branch = branch
        self.cgpa = float(cgpa)
        self.skills = skills
        self.status = status

    # ---------- Display ----------

    def display(self):

        print("\n" + "=" * 50)
        print("           STUDENT DETAILS")
        print("=" * 50)

        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.get_name()}")
        print(f"Email      : {self.get_email()}")
        print(f"Phone      : {self.phone}")
        print(f"Branch     : {self.branch}")
        print(f"CGPA       : {self.cgpa}")
        print(f"Skills     : {self.skills}")
        print(f"Status     : {self.status}")

        print("=" * 50)

    # ---------- Convert Object to Dictionary ----------

    def to_dict(self):

        return {
            "student_id": self.student_id,
            "name": self.get_name(),
            "email": self.get_email(),
            "phone": self.phone,
            "branch": self.branch,
            "cgpa": self.cgpa,
            "skills": self.skills,
            "password": self.get_password(),
            "status": self.status
        }

    # ---------- Update Student ----------

    def update_profile(self, phone, branch, cgpa, skills):

        self.phone = phone
        self.branch = branch
        self.cgpa = float(cgpa)
        self.skills = skills

    # ---------- Placement ----------

    def place_student(self):

        self.status = "Placed"

    # ---------- Eligibility ----------

    def is_eligible(self, required_cgpa):

        return self.cgpa >= float(required_cgpa)