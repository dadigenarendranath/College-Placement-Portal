class PlacementDrive:
    """
    Represents a placement drive conducted by a company.
    """

    def __init__(self,
                 drive_id,
                 company_id,
                 drive_date,
                 venue,
                 status="Upcoming"):

        self.drive_id = drive_id
        self.company_id = company_id
        self.drive_date = drive_date
        self.venue = venue
        self.status = status

    # ---------- Display ----------

    def display(self):

        print("\n" + "=" * 50)
        print("         PLACEMENT DRIVE")
        print("=" * 50)

        print(f"Drive ID    : {self.drive_id}")
        print(f"Company ID  : {self.company_id}")
        print(f"Drive Date  : {self.drive_date}")
        print(f"Venue       : {self.venue}")
        print(f"Status      : {self.status}")

        print("=" * 50)

    # ---------- Update Status ----------

    def update_status(self, status):

        self.status = status

    # ---------- Convert Object to Dictionary ----------

    def to_dict(self):

        return {
            "drive_id": self.drive_id,
            "company_id": self.company_id,
            "drive_date": self.drive_date,
            "venue": self.venue,
            "status": self.status
        }