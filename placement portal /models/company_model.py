class Company:

    def __init__(self, company_id, company_name, role,
                 package, eligibility_cgpa,
                 location, openings):

        self.company_id = company_id
        self.company_name = company_name
        self.role = role
        self.package = float(package)
        self.eligibility_cgpa = float(eligibility_cgpa)
        self.location = location
        self.openings = int(openings)

    # ---------- Display ----------

    def display(self):

        print("\n" + "=" * 50)
        print("            COMPANY DETAILS")
        print("=" * 50)

        print(f"Company ID      : {self.company_id}")
        print(f"Company Name    : {self.company_name}")
        print(f"Role            : {self.role}")
        print(f"Package         : {self.package} LPA")
        print(f"Minimum CGPA    : {self.eligibility_cgpa}")
        print(f"Location        : {self.location}")
        print(f"Openings        : {self.openings}")

        print("=" * 50)

    # ---------- Convert Object to Dictionary ----------

    def to_dict(self):

        return {
            "company_id": self.company_id,
            "company_name": self.company_name,
            "role": self.role,
            "package": self.package,
            "eligibility_cgpa": self.eligibility_cgpa,
            "location": self.location,
            "openings": self.openings
        }

    # ---------- Check Student Eligibility ----------

    def is_eligible(self, student_cgpa):

        return float(student_cgpa) >= self.eligibility_cgpa

    # ---------- Reduce Vacancy ----------

    def reduce_opening(self):

        if self.openings > 0:
            self.openings -= 1

    # ---------- Vacancy Available ----------

    def has_openings(self):

        return self.openings > 0