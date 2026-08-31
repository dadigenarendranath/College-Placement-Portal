class Application:
    """
    Represents a student's application to a company.
    """

    def __init__(self,
                 application_id,
                 student_id,
                 company_id,
                 status="Applied",
                 result="Pending"):

        self.application_id = application_id
        self.student_id = student_id
        self.company_id = company_id
        self.status = status
        self.result = result

    # ---------- Display ----------

    def display(self):

        print("\n" + "=" * 50)
        print("         APPLICATION DETAILS")
        print("=" * 50)

        print(f"Application ID : {self.application_id}")
        print(f"Student ID     : {self.student_id}")
        print(f"Company ID     : {self.company_id}")
        print(f"Status         : {self.status}")
        print(f"Result         : {self.result}")

        print("=" * 50)

    # ---------- Update Status ----------

    def update_status(self, status):

        self.status = status

    # ---------- Update Result ----------

    def update_result(self, result):

        self.result = result

    # ---------- Convert Object to Dictionary ----------

    def to_dict(self):

        return {
            "application_id": self.application_id,
            "student_id": self.student_id,
            "company_id": self.company_id,
            "status": self.status,
            "result": self.result
        }