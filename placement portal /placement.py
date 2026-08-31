from data import (
    load_data,
    save_data,
    append_data,
    DRIVES_FILE
)

from models.placement_model import PlacementDrive

from company import CompanyManager

from utils import (
    generate_id,
    display_records,
    find_record
)

from validation import validate_date


class PlacementManager:

    FIELDNAMES = [
        "drive_id",
        "company_id",
        "drive_date",
        "venue",
        "status"
    ]

    def __init__(self):

        self.company_manager = CompanyManager()

    # ----------------------------------
    # Create Placement Drive
    # ----------------------------------

    def create_drive(self):

        company_id = input("Enter Company ID : ").upper()

        company = self.company_manager.get_company_by_id(company_id)

        if company is None:

            print("\nCompany Not Found.")
            return

        drives = load_data(DRIVES_FILE)

        drive_id = generate_id(drives, "DRV")

        drive_date = input("Drive Date (DD-MM-YYYY): ")

        if not validate_date(drive_date):

            print("Invalid Date")
            return

        venue = input("Venue : ")

        drive = PlacementDrive(
            drive_id,
            company_id,
            drive_date,
            venue
        )

        append_data(
            DRIVES_FILE,
            self.FIELDNAMES,
            drive.to_dict()
        )

        print("\nPlacement Drive Created Successfully.")
        print("Drive ID :", drive_id)

    # ----------------------------------
    # View Drives
    # ----------------------------------

    def view_drives(self):

        drives = load_data(DRIVES_FILE)

        if not drives:

            print("\nNo Placement Drives Available.")
            return

        display_records(drives)

    # ----------------------------------
    # Search Drive
    # ----------------------------------

    def search_drive(self):

        drive_id = input("Enter Drive ID : ").upper()

        drives = load_data(DRIVES_FILE)

        drive = find_record(
            drives,
            "drive_id",
            drive_id
        )

        if drive:

            print()

            for key, value in drive.items():

                print(f"{key:<15}: {value}")

        else:

            print("\nDrive Not Found.")

    # ----------------------------------
    # Update Drive Status
    # ----------------------------------

    def update_status(self):

        drives = load_data(DRIVES_FILE)

        drive_id = input("Enter Drive ID : ").upper()

        drive = find_record(
            drives,
            "drive_id",
            drive_id
        )

        if drive is None:

            print("\nDrive Not Found.")
            return

        print("\n1. Upcoming")
        print("2. Ongoing")
        print("3. Completed")

        choice = input("Enter Choice : ")

        if choice == "1":

            drive["status"] = "Upcoming"

        elif choice == "2":

            drive["status"] = "Ongoing"

        elif choice == "3":

            drive["status"] = "Completed"

        else:

            print("Invalid Choice")
            return

        save_data(
            DRIVES_FILE,
            self.FIELDNAMES,
            drives
        )

        print("\nDrive Status Updated Successfully.")

    # ----------------------------------
    # Delete Drive
    # ----------------------------------

    def delete_drive(self):

        drives = load_data(DRIVES_FILE)

        drive_id = input("Enter Drive ID : ").upper()

        drive = find_record(
            drives,
            "drive_id",
            drive_id
        )

        if drive is None:

            print("\nDrive Not Found.")
            return

        drives.remove(drive)

        save_data(
            DRIVES_FILE,
            self.FIELDNAMES,
            drives
        )

        print("\nDrive Deleted Successfully.")