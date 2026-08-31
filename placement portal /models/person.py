class Person:
    """
    Base class for Student and Admin
    """

    def __init__(self, name="", email="", password=""):
        self._name = name
        self._email = email
        self._password = password

    # Getters
    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    # Setters
    def set_name(self, name):
        self._name = name

    def set_email(self, email):
        self._email = email

    def set_password(self, password):
        self._password = password

    def display(self):
        print(f"Name : {self._name}")
        print(f"Email: {self._email}")