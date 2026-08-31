from auth import (
    admin_login,
    student_login,
    student_register
)

from student import StudentManager
from company import CompanyManager
from application import ApplicationManager
from placement import PlacementManager
from report import ReportManager

from utils import (
    clear_screen,
    pause,
    print_heading
)


student_manager = StudentManager()
company_manager = CompanyManager()
application_manager = ApplicationManager()
placement_manager = PlacementManager()
report_manager = ReportManager()


# ---------------------------------
# Report Menu
# ---------------------------------

def report_menu():

    while True:

        clear_screen()

        print_heading("REPORTS")

        print("1. Total Students")
        print("2. Total Companies")
        print("3. Total Applications")
        print("4. Placed Students")
        print("5. Unplaced Students")
        print("6. Highest Package")
        print("7. Lowest Package")
        print("8. Average CGPA")
        print("9. Branch Wise Students")
        print("10. Company Wise Applications")
        print("11. Eligible Students")
        print("12. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            report_manager.total_students()

        elif choice == "2":
            report_manager.total_companies()

        elif choice == "3":
            report_manager.total_applications()

        elif choice == "4":
            report_manager.placed_students()

        elif choice == "5":
            report_manager.unplaced_students()

        elif choice == "6":
            report_manager.highest_package()

        elif choice == "7":
            report_manager.lowest_package()

        elif choice == "8":
            report_manager.average_cgpa()

        elif choice == "9":
            report_manager.branch_wise_students()

        elif choice == "10":
            report_manager.company_wise_applications()

        elif choice == "11":
            report_manager.eligible_students()

        elif choice == "12":
            break

        else:
            print("Invalid Choice")

        pause()


# ---------------------------------
# Placement Menu
# ---------------------------------

def placement_menu():

    while True:

        clear_screen()

        print_heading("PLACEMENT DRIVES")

        print("1. Create Drive")
        print("2. View Drives")
        print("3. Search Drive")
        print("4. Update Drive Status")
        print("5. Delete Drive")
        print("6. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            placement_manager.create_drive()

        elif choice == "2":
            placement_manager.view_drives()

        elif choice == "3":
            placement_manager.search_drive()

        elif choice == "4":
            placement_manager.update_status()

        elif choice == "5":
            placement_manager.delete_drive()

        elif choice == "6":
            break

        else:
            print("Invalid Choice")

        pause()
# ============================================
# APPLICATION MANAGEMENT MENU
# ============================================

def application_menu():

    while True:

        clear_screen()

        print_heading("APPLICATION MANAGEMENT")

        print("1. View Applications")
        print("2. Update Application Result")
        print("3. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            application_manager.view_applications()

        elif choice == "2":

            application_manager.update_result()

        elif choice == "3":

            break

        else:

            print("\nInvalid Choice.")

        pause()


# ============================================
# PLACEMENT DRIVE MENU
# ============================================

def placement_menu():

    while True:

        clear_screen()

        print_heading("PLACEMENT DRIVE MANAGEMENT")

        print("1. Create Drive")
        print("2. View Drives")
        print("3. Search Drive")
        print("4. Update Drive Status")
        print("5. Delete Drive")
        print("6. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            placement_manager.create_drive()

        elif choice == "2":

            placement_manager.view_drives()

        elif choice == "3":

            placement_manager.search_drive()

        elif choice == "4":

            placement_manager.update_status()

        elif choice == "5":

            placement_manager.delete_drive()

        elif choice == "6":

            break

        else:

            print("\nInvalid Choice.")

        pause()
# ============================================
# STUDENT MANAGEMENT MENU
# ============================================

def student_menu():

    while True:

        clear_screen()

        print_heading("STUDENT MANAGEMENT")

        print("1. View Students")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            student_manager.view_students()

        elif choice == "2":

            student_manager.search_student()

        elif choice == "3":

            student_manager.update_student()

        elif choice == "4":

            student_manager.delete_student()

        elif choice == "5":

            break

        else:

            print("\nInvalid Choice.")

        pause()
def company_menu():

    while True:

        clear_screen()

        print_heading("COMPANY MANAGEMENT")

        print("1. Add Company")
        print("2. View Companies")
        print("3. Search Company")
        print("4. Update Company")
        print("5. Delete Company")
        print("6. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            company_manager.add_company()

        elif choice == "2":
            company_manager.view_companies()

        elif choice == "3":
            company_manager.search_company()

        elif choice == "4":
            company_manager.update_company()

        elif choice == "5":
            company_manager.delete_company()

        elif choice == "6":
            break

        else:
            print("Invalid Choice")

        pause()


# ============================================
# REPORT MENU
# ============================================

def report_menu():

    while True:

        clear_screen()

        print_heading("REPORTS")

        print("1. Total Students")
        print("2. Total Companies")
        print("3. Total Applications")
        print("4. Placed Students")
        print("5. Unplaced Students")
        print("6. Highest Package")
        print("7. Lowest Package")
        print("8. Average CGPA")
        print("9. Branch Wise Students")
        print("10. Company Wise Applications")
        print("11. Eligible Students")
        print("12. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            report_manager.total_students()

        elif choice == "2":

            report_manager.total_companies()

        elif choice == "3":

            report_manager.total_applications()

        elif choice == "4":

            report_manager.placed_students()

        elif choice == "5":

            report_manager.unplaced_students()

        elif choice == "6":

            report_manager.highest_package()

        elif choice == "7":

            report_manager.lowest_package()

        elif choice == "8":

            report_manager.average_cgpa()

        elif choice == "9":

            report_manager.branch_wise_students()

        elif choice == "10":

            report_manager.company_wise_applications()

        elif choice == "11":

            report_manager.eligible_students()

        elif choice == "12":

            break

        else:

            print("\nInvalid Choice.")

        pause()


# ============================================
# ADMIN DASHBOARD
# ============================================

def admin_dashboard():

    while True:

        clear_screen()

        print_heading("ADMIN DASHBOARD")

        print("1. Student Management")
        print("2. Company Management")
        print("3. Placement Drives")
        print("4. Applications")
        print("5. Reports")
        print("6. Logout")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            student_menu()

        elif choice == "2":

            company_menu()

        elif choice == "3":

            placement_menu()

        elif choice == "4":

            application_menu()

        elif choice == "5":

            report_menu()

        elif choice == "6":

            print("\nLogged Out Successfully.")
            break

        else:

            print("\nInvalid Choice.")

        pause()
# ============================================
# STUDENT DASHBOARD
# ============================================

def student_dashboard(student):

    while True:

        clear_screen()

        print_heading(f"Welcome {student['name']}")

        print("1. View Profile")
        print("2. Update Profile")
        print("3. View Companies")
        print("4. Apply for Company")
        print("5. My Applications")
        print("6. Logout")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            student_manager.view_profile(student)

        elif choice == "2":

            student_manager.update_profile(student)

            # Reload latest student information
            updated_student = student_manager.get_student_by_id(
                student["student_id"]
            )

            if updated_student:
                student = updated_student

        elif choice == "3":

            company_manager.view_companies()

        elif choice == "4":

            application_manager.apply_company(student)

        elif choice == "5":

            application_manager.my_applications(student)

        elif choice == "6":

            print("\nLogged Out Successfully.")
            break

        else:

            print("\nInvalid Choice.")

        pause()


# ============================================
# MAIN MENU
# ============================================

def main_menu():

    while True:

        clear_screen()

        print_heading("PLACEMENT PORTAL MANAGEMENT SYSTEM")

        print("1. Admin Login")
        print("2. Student Registration")
        print("3. Student Login")
        print("4. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            if admin_login():

                admin_dashboard()

        elif choice == "2":

            student_register()

            pause()

        elif choice == "3":

            student = student_login()

            if student:

                student_dashboard(student)

        elif choice == "4":

            print("\nThank You for Using Placement Portal.")
            print("Have a Nice Day!")

            break

        else:

            print("\nInvalid Choice.")

            pause()
# ============================================
# PROGRAM ENTRY POINT
# ============================================

if __name__ == "__main__":

    try:

        main_menu()

    except KeyboardInterrupt:

        print("\n\nProgram Interrupted by User.")

    except Exception as error:

        print("\nAn Unexpected Error Occurred.")
        print("Error :", error)

    finally:

        print("\nThank You for Using Placement Portal.")