from data import (
    load_data,
    STUDENTS_FILE,
    COMPANIES_FILE,
    APPLICATIONS_FILE
)


class ReportManager:

    # -----------------------------------
    # Total Students
    # -----------------------------------

    def total_students(self):

        students = load_data(STUDENTS_FILE)

        print(f"\nTotal Students : {len(students)}")

    # -----------------------------------
    # Total Companies
    # -----------------------------------

    def total_companies(self):

        companies = load_data(COMPANIES_FILE)

        print(f"\nTotal Companies : {len(companies)}")

    # -----------------------------------
    # Total Applications
    # -----------------------------------

    def total_applications(self):

        applications = load_data(APPLICATIONS_FILE)

        print(f"\nTotal Applications : {len(applications)}")

    # -----------------------------------
    # Placed Students
    # -----------------------------------

    def placed_students(self):

        students = load_data(STUDENTS_FILE)

        placed = []

        for student in students:

            if student["status"] == "Placed":
                placed.append(student)

        print(f"\nPlaced Students : {len(placed)}")

        for student in placed:

            print(
                student["student_id"],
                student["name"]
            )

    # -----------------------------------
    # Unplaced Students
    # -----------------------------------

    def unplaced_students(self):

        students = load_data(STUDENTS_FILE)

        unplaced = []

        for student in students:

            if student["status"] != "Placed":
                unplaced.append(student)

        print(f"\nUnplaced Students : {len(unplaced)}")

        for student in unplaced:

            print(
                student["student_id"],
                student["name"]
            )

    # -----------------------------------
    # Highest Package
    # -----------------------------------

    def highest_package(self):

        companies = load_data(COMPANIES_FILE)

        if not companies:
            print("\nNo Companies Available.")
            return

        highest = max(
            companies,
            key=lambda company: float(company["package"])
        )

        print("\nHighest Package Company")

        print("-------------------------")

        print("Company :", highest["company_name"])
        print("Package :", highest["package"], "LPA")

    # -----------------------------------
    # Lowest Package
    # -----------------------------------

    def lowest_package(self):

        companies = load_data(COMPANIES_FILE)

        if not companies:
            print("\nNo Companies Available.")
            return

        lowest = min(
            companies,
            key=lambda company: float(company["package"])
        )

        print("\nLowest Package Company")

        print("-------------------------")

        print("Company :", lowest["company_name"])
        print("Package :", lowest["package"], "LPA")

    # -----------------------------------
    # Average CGPA
    # -----------------------------------

    def average_cgpa(self):

        students = load_data(STUDENTS_FILE)

        if not students:
            print("\nNo Students Available.")
            return

        total = 0

        for student in students:

            total += float(student["cgpa"])

        average = total / len(students)

        print(f"\nAverage CGPA : {average:.2f}")

    # -----------------------------------
    # Branch Wise Count
    # -----------------------------------

    def branch_wise_students(self):

        students = load_data(STUDENTS_FILE)

        branch_count = {}

        for student in students:

            branch = student["branch"]

            if branch not in branch_count:
                branch_count[branch] = 0

            branch_count[branch] += 1

        print("\nBranch Wise Students")

        print("-----------------------")

        for branch, count in branch_count.items():

            print(branch, ":", count)

    # -----------------------------------
    # Company Wise Applications
    # -----------------------------------

    def company_wise_applications(self):

        applications = load_data(APPLICATIONS_FILE)

        company_count = {}

        for app in applications:

            company = app["company_name"]

            if company not in company_count:
                company_count[company] = 0

            company_count[company] += 1

        print("\nCompany Wise Applications")

        print("--------------------------")

        for company, count in company_count.items():

            print(company, ":", count)

    # -----------------------------------
    # Eligible Students
    # -----------------------------------

    def eligible_students(self):

        companies = load_data(COMPANIES_FILE)

        students = load_data(STUDENTS_FILE)

        company_id = input("Enter Company ID : ").upper()

        company = None

        for comp in companies:

            if comp["company_id"] == company_id:
                company = comp
                break

        if company is None:

            print("\nCompany Not Found.")
            return

        print("\nEligible Students")

        print("---------------------")

        found = False

        for student in students:

            if float(student["cgpa"]) >= float(company["eligibility_cgpa"]):

                found = True

                print(
                    student["student_id"],
                    student["name"],
                    student["cgpa"]
                )

        if not found:

            print("No Eligible Students.")