from data import (
    load_data,
    save_data,
    append_data,
    APPLICATIONS_FILE
)

from models.application_model import Application
from utils import generate_id, display_records, find_record
from student import StudentManager
from company import CompanyManager


class ApplicationManager:

    FIELDNAMES = [
        "application_id",
        "student_id",
        "student_name",
        "company_id",
        "company_name",
        "status",
        "result"
    ]

    def __init__(self):

        self.student_manager = StudentManager()
        self.company_manager = CompanyManager()

    # ----------------------------------
    # Apply for Company
    # ----------------------------------

    def apply_company(self, student):

        companies = load_data("storage/companies.csv")
        applications = load_data(APPLICATIONS_FILE)

        if not companies:
            print("\nNo Companies Available.")
            return

        self.company_manager.view_companies()

        company_id = input("\nEnter Company ID : ").upper()

        company = self.company_manager.get_company_by_id(company_id)

        if company is None:
            print("\nCompany Not Found.")
            return

        # Already Applied?

        for app in applications:

            if (app["student_id"] == student["student_id"]
                    and app["company_id"] == company_id):

                print("\nAlready Applied.")
                return

        # Eligibility Check

        if float(student["cgpa"]) < float(company["eligibility_cgpa"]):

            print("\nYou are not eligible for this company.")
            return

        if int(company["openings"]) <= 0:

            print("\nNo Openings Available.")
            return

        application = Application(

            generate_id(applications, "APP"),

            student["student_id"],
            company_id
        )

        record = {
            "application_id": application.application_id,
            "student_id": student["student_id"],
            "student_name": student["name"],
            "company_id": company["company_id"],
            "company_name": company["company_name"],
            "status": "Applied",
            "result": "Pending"
        }

        append_data(
            APPLICATIONS_FILE,
            self.FIELDNAMES,
            record
        )

        print("\nApplication Submitted Successfully.")

    # ----------------------------------
    # View All Applications
    # ----------------------------------

    def view_applications(self):

        applications = load_data(APPLICATIONS_FILE)

        display_records(applications)

    # ----------------------------------
    # My Applications
    # ----------------------------------

    def my_applications(self, student):

        applications = load_data(APPLICATIONS_FILE)

        found = False

        for app in applications:

            if app["student_id"] == student["student_id"]:

                found = True

                print()

                for key, value in app.items():
                    print(f"{key:<20}: {value}")

                print("-" * 40)

        if not found:

            print("\nNo Applications Found.")

    # ----------------------------------
    # Update Result
    # ----------------------------------

    def update_result(self):

        applications = load_data(APPLICATIONS_FILE)

        app_id = input("Application ID : ").upper()

        application = find_record(
            applications,
            "application_id",
            app_id
        )

        if application is None:

            print("\nApplication Not Found.")
            return

        print("\n1. Shortlisted")
        print("2. Selected")
        print("3. Rejected")

        choice = input("Enter Choice : ")

        if choice == "1":

            application["status"] = "Shortlisted"

        elif choice == "2":

            application["status"] = "Selected"
            application["result"] = "Pass"

            self.student_manager.mark_as_placed(
                application["student_id"]
            )

            self.company_manager.reduce_opening(
                application["company_id"]
            )

        elif choice == "3":

            application["status"] = "Rejected"
            application["result"] = "Fail"

        else:

            print("Invalid Choice")
            return

        save_data(
            APPLICATIONS_FILE,
            self.FIELDNAMES,
            applications
        )

        print("\nApplication Updated Successfully.")