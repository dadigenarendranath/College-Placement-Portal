from data import (
    load_data,
    save_data,
    append_data,
    COMPANIES_FILE
)

from models.company_model import Company

from utils import (
    display_records,
    generate_id,
    find_record
)

from validation import (
    validate_cgpa,
    validate_package,
    validate_openings
)


class CompanyManager:

    FIELDNAMES = [
        "company_id",
        "company_name",
        "role",
        "package",
        "eligibility_cgpa",
        "location",
        "openings"
    ]

    # ---------------------------------
    # Add Company
    # ---------------------------------

    def add_company(self):

        companies = load_data(COMPANIES_FILE)

        company_id = generate_id(companies, "COM")

        print("\n========== Add Company ==========")

        company_name = input("Company Name : ").strip()
        role = input("Role          : ").strip()

        package = input("Package (LPA) : ")
        if not validate_package(package):
            print("Invalid Package")
            return

        eligibility = input("Minimum CGPA  : ")
        if not validate_cgpa(eligibility):
            print("Invalid CGPA")
            return

        location = input("Location      : ").strip()

        openings = input("Openings      : ")
        if not validate_openings(openings):
            print("Invalid Openings")
            return

        company = Company(
            company_id,
            company_name,
            role,
            package,
            eligibility,
            location,
            openings
        )

        append_data(
            COMPANIES_FILE,
            self.FIELDNAMES,
            company.to_dict()
        )

        print("\nCompany Added Successfully.")
        print("Company ID :", company_id)

    # ---------------------------------
    # View Companies
    # ---------------------------------

    def view_companies(self):

        companies = load_data(COMPANIES_FILE)

        if not companies:
            print("\nNo Companies Available.")
            return

        display_records(companies)

    # ---------------------------------
    # Search Company
    # ---------------------------------

    def search_company(self):

        company_id = input("Enter Company ID : ")

        companies = load_data(COMPANIES_FILE)

        company = find_record(
            companies,
            "company_id",
            company_id
        )

        if company:

            print()

            for key, value in company.items():
                print(f"{key:<20}: {value}")

        else:
            print("\nCompany Not Found.")

    # ---------------------------------
    # Update Company
    # ---------------------------------

    def update_company(self):

        company_id = input("Enter Company ID : ")

        companies = load_data(COMPANIES_FILE)

        company = find_record(
            companies,
            "company_id",
            company_id
        )

        if company is None:
            print("\nCompany Not Found.")
            return

        print("\nLeave blank to keep old value.\n")

        role = input(f"Role ({company['role']}) : ")
        package = input(f"Package ({company['package']}) : ")
        cgpa = input(f"CGPA ({company['eligibility_cgpa']}) : ")
        location = input(f"Location ({company['location']}) : ")
        openings = input(f"Openings ({company['openings']}) : ")

        if role:
            company["role"] = role

        if package:
            if validate_package(package):
                company["package"] = package

        if cgpa:
            if validate_cgpa(cgpa):
                company["eligibility_cgpa"] = cgpa

        if location:
            company["location"] = location

        if openings:
            if validate_openings(openings):
                company["openings"] = openings

        save_data(
            COMPANIES_FILE,
            self.FIELDNAMES,
            companies
        )

        print("\nCompany Updated Successfully.")

    # ---------------------------------
    # Delete Company
    # ---------------------------------

    def delete_company(self):

        company_id = input("Enter Company ID : ")

        companies = load_data(COMPANIES_FILE)

        company = find_record(
            companies,
            "company_id",
            company_id
        )

        if company is None:
            print("\nCompany Not Found.")
            return

        companies.remove(company)

        save_data(
            COMPANIES_FILE,
            self.FIELDNAMES,
            companies
        )

        print("\nCompany Deleted Successfully.")

# ---------------------------------
# Get Company By ID
# ---------------------------------

    def get_company_by_id(self, company_id):

       companies = load_data(COMPANIES_FILE)

       return find_record(
        companies,
        "company_id",
        company_id
        )


# ---------------------------------
# Reduce Opening
# ---------------------------------

    def reduce_opening(self, company_id):

        companies = load_data(COMPANIES_FILE)

        company = find_record(
        companies,
        "company_id",
        company_id
    )

        if company:

            openings = int(company["openings"])

        if openings > 0:

            company["openings"] = str(openings - 1)

            save_data(
                COMPANIES_FILE,
                self.FIELDNAMES,
                companies
            )

            return True

        return False

