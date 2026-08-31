import csv
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STORAGE = os.path.join(BASE_DIR, "storage")

STUDENTS_FILE = os.path.join(STORAGE, "students.csv")
COMPANIES_FILE = os.path.join(STORAGE, "companies.csv")
APPLICATIONS_FILE = os.path.join(STORAGE, "applications.csv")
DRIVES_FILE = os.path.join(STORAGE, "drives.csv")
ADMINS_FILE = os.path.join(STORAGE, "admins.csv")


def load_data(filename):
    """
    Reads all records from a CSV file.
    Returns a list of dictionaries.
    """
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []


def save_data(filename, fieldnames, data):
    """
    Writes all records to a CSV file.
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def append_data(filename, fieldnames, record):
    """
    Adds a single record to a CSV file.
    """
    file_exists = os.path.exists(filename)
    file_empty = (not file_exists) or os.path.getsize(filename) == 0

    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file_empty:
            writer.writeheader()

        writer.writerow(record)

import csv
import os


def initialize_admin():

    if not os.path.exists(ADMINS_FILE):

        with open(ADMINS_FILE, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow(["username", "password"])
            writer.writerow(["admin", "admin123"])
initialize_admin()