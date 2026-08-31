🎓 Placement Portal Management System (CLI)

A Command Line Interface (CLI) based Placement Portal Management System developed using Python. This project simulates the placement process in colleges, allowing administrators to manage students, companies, placement drives, applications, and reports.

The project is built using Core Python concepts, Object-Oriented Programming (OOP), and CSV file handling without any external database or GUI.

⸻

📌 Features

👨‍💼 Admin

* Secure Admin Login
* Manage Students
    * View Students
    * Search Student
    * Update Student
    * Delete Student
* Manage Companies
    * Add Company
    * View Companies
    * Search Company
    * Update Company
    * Delete Company
* Manage Placement Drives
    * Create Drive
    * View Drives
    * Search Drive
    * Update Drive Status
    * Delete Drive
* Manage Applications
    * View Applications
    * Update Application Status
* Generate Reports
    * Total Students
    * Total Companies
    * Total Applications
    * Placed Students
    * Unplaced Students
    * Highest Package
    * Lowest Package
    * Average CGPA
    * Branch-wise Student Count
    * Company-wise Applications
    * Eligible Students

⸻

👨‍🎓 Student

* Student Registration
* Student Login
* View Profile
* Update Profile
* View Companies
* Apply for Company
* View My Applications
* Logout

⸻

🛠 Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* CSV File Handling
* Python Standard Library
* Command Line Interface (CLI)

⸻

📁 Project Structure

PlacementPortal/
│
├── main.py
├── auth.py
├── student.py
├── company.py
├── application.py
├── placement.py
├── report.py
├── validation.py
├── utils.py
├── data.py
│
├── models/
│   ├── person.py
│   ├── student_model.py
│   ├── admin_model.py
│   ├── company_model.py
│   ├── application_model.py
│   └── placement_model.py
│
├── storage/
│   ├── admins.csv
│   ├── students.csv
│   ├── companies.csv
│   ├── applications.csv
│   └── drives.csv
│
└── README.md

⸻

💡 Python Concepts Demonstrated

* Variables and Data Types
* Conditional Statements
* Loops
* Functions
* Modules
* Object-Oriented Programming
    * Classes & Objects
    * Inheritance
    * Encapsulation
    * Constructors
* Exception Handling
* File Handling (CSV)
* Lists
* Dictionaries
* Sets
* Lambda Functions
* map()
* filter()
* List Comprehensions

⸻

📂 CSV Storage

The project stores data in CSV files instead of using a database.

* admins.csv
* students.csv
* companies.csv
* applications.csv
* drives.csv

⸻

🚀 How to Run

1. Clone the repository:

git clone https://github.com/your-username/placement-portal.git

2. Navigate to the project folder:

cd placement-portal

3. Run the project:

python main.py

⸻

🔑 Default Admin Credentials

Username : admin
Password : admin123

Make sure storage/admins.csv exists with the default admin credentials.

⸻

📋 Sample Workflow

1. Login as Admin
2. Add Companies
3. Create Placement Drives
4. Register Students
5. Login as Student
6. Apply for Companies
7. Admin Updates Application Status
8. Generate Reports

⸻

🎯 Learning Outcomes

This project demonstrates how to:

* Design a modular Python application
* Build a menu-driven CLI application
* Apply Object-Oriented Programming principles
* Perform CRUD operations using CSV files
* Validate user input
* Organize code into reusable modules
* Manage data without a database

⸻

🔮 Future Improvements

* Password hashing
* Email notifications
* Search by skills
* Company eligibility filtering
* Export reports to Excel
* Admin dashboard statistics
* Student dashboard statistics
* Pagination for large datasets
* Logging system
* SQLite/MySQL integration
* GUI using Tkinter or PyQt
* Web version using Flask or Django

⸻

👨‍💻 Author

Narendranath Dadige

Python Developer | Aspiring Software Engineer

⸻

📜 License

This project is created for educational and learning purposes. You are free to use, modify, and extend it for personal or academic projects.