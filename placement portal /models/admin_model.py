from models.person import Person


class Admin(Person):

    def __init__(self, username, password):
        super().__init__(username, "", password)
        self.username = username

    # ---------- Display ----------

    def display(self):

        print("\n" + "=" * 40)
        print("         ADMIN DETAILS")
        print("=" * 40)
        print(f"Username : {self.username}")
        print("=" * 40)

    # ---------- Convert Object to Dictionary ----------

    def to_dict(self):

        return {
            "username": self.username,
            "password": self.get_password()
        }

    # ---------- Verify Password ----------

    def check_password(self, password):

        return self.get_password() == password

    # ---------- Change Password ----------

    def change_password(self, new_password):

        self.set_password(new_password)