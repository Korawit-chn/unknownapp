#!/usr/bin/env python3
"""
Course Enrollment System (Python Login/Menu Replica)

This script recreates the login/menu flow and options from Main.java:
- Login as Student / Login as Admin / Exit
- Student menu options 1-7
- Admin menu options 1-10
"""

from __future__ import annotations


ADMIN_PASSWORD = "admin123"
SEPARATOR = "=" * 70
THIN_SEP = "-" * 70


class EnrollmentCLI:
    def run(self) -> None:
        self.print_banner()
        self.init_data()

        quit_app = False
        while not quit_app:
            quit_app = self.login_menu()

    def print_banner(self) -> None:
        print(SEPARATOR)
        print("       COURSE ENROLLMENT SYSTEM")
        print(SEPARATOR)

    def init_data(self) -> None:
        print("[INFO] Python demo mode: using in-memory placeholders.")

    def login_menu(self) -> bool:
        print()
        print(SEPARATOR)
        print("  LOGIN")
        print(SEPARATOR)
        print("  [1] Login as Student")
        print("  [2] Login as Admin")
        print("  [3] Exit")
        print(THIN_SEP)
        choice = input("  Select option: ").strip()

        if choice == "1":
            self.student_login()
        elif choice == "2":
            self.admin_login()
        elif choice == "3":
            self.save_and_exit()
            return True
        else:
            print("  [!] Invalid option. Please enter 1, 2, or 3.")
        return False

    def student_login(self) -> None:
        print()
        print("  --- Student Login ---")
        print("  Enter your Student ID (or 'new' to create a new profile): ")
        student_id = input("  > ").strip()

        if student_id.lower() == "new":
            self.create_student_profile()
            return

        if not student_id:
            print("  [!] Student ID not found. Type 'new' to create a new profile.")
            return

        print(f"  Welcome, {student_id}!")
        self.student_menu(student_id)

    def admin_login(self) -> None:
        print()
        print("  --- Admin Login ---")
        pwd = input("  Password: ").strip()
        if pwd != ADMIN_PASSWORD:
            print("  [!] Incorrect password.")
            return
        print("  Welcome, Administrator!")
        self.admin_menu()

    def student_menu(self, student_id: str) -> None:
        logout = False
        while not logout:
            print()
            print(SEPARATOR)
            print(f"  STUDENT MENU  -  {student_id} [{student_id}]")
            print(SEPARATOR)
            print("  [1] View Course Catalog")
            print("  [2] Register for a Course")
            print("  [3] Drop a Course")
            print("  [4] View My Schedule")
            print("  [5] Billing Summary")
            print("  [6] Edit My Profile")
            print("  [7] Logout and Save")
            print(THIN_SEP)
            choice = input("  Select option: ").strip()

            if choice == "1":
                print("  [INFO] View Course Catalog (placeholder)")
            elif choice == "2":
                print("  [INFO] Register for a Course (placeholder)")
            elif choice == "3":
                print("  [INFO] Drop a Course (placeholder)")
            elif choice == "4":
                print("  [INFO] View My Schedule (placeholder)")
            elif choice == "5":
                print("  [INFO] Billing Summary (placeholder)")
            elif choice == "6":
                print("  [INFO] Edit My Profile (placeholder)")
            elif choice == "7":
                self.save_data()
                logout = True
            else:
                print("  [!] Invalid option.")

    def create_student_profile(self) -> None:
        print()
        print("  --- Create New Student Profile ---")
        student_id = input("  Student ID: ").strip()
        if not student_id:
            print("  [!] Student ID cannot be empty.")
            return

        full_name = input("  Full Name : ").strip()
        if not full_name:
            print("  [!] Name cannot be empty.")
            return

        major = input("  Major     : ").strip() or "Undeclared"
        print(f"  [✓] New student profile created: {student_id} | {full_name} | {major}")
        self.student_menu(student_id)

    def admin_menu(self) -> None:
        logout = False
        while not logout:
            print()
            print(SEPARATOR)
            print("  ADMIN MENU")
            print(SEPARATOR)
            print("  [1]  View Course Catalog")
            print("  [2]  View Class Roster")
            print("  [3]  View All Students")
            print("  [4]  Add New Student")
            print("  [5]  Edit Student Profile")
            print("  [6]  Add New Course")
            print("  [7]  Edit Course")
            print("  [8]  View Student Schedule")
            print("  [9]  Billing Summary (any student)")
            print("  [10] Logout and Save")
            print(THIN_SEP)
            choice = input("  Select option: ").strip()

            if choice == "1":
                print("  [INFO] View Course Catalog (placeholder)")
            elif choice == "2":
                print("  [INFO] View Class Roster (placeholder)")
            elif choice == "3":
                print("  [INFO] View All Students (placeholder)")
            elif choice == "4":
                print("  [INFO] Add New Student (placeholder)")
            elif choice == "5":
                print("  [INFO] Edit Student Profile (placeholder)")
            elif choice == "6":
                print("  [INFO] Add New Course (placeholder)")
            elif choice == "7":
                print("  [INFO] Edit Course (placeholder)")
            elif choice == "8":
                print("  [INFO] View Student Schedule (placeholder)")
            elif choice == "9":
                print("  [INFO] Billing Summary (any student) (placeholder)")
            elif choice == "10":
                self.save_data()
                logout = True
            else:
                print("  [!] Invalid option.")

    def save_data(self) -> None:
        print("  [✓] Data saved successfully.")

    def save_and_exit(self) -> None:
        self.save_data()
        print()
        print("  Thank you for using the Course Enrollment System. Goodbye!")
        print(SEPARATOR)


def main() -> None:
    EnrollmentCLI().run()


if __name__ == "__main__":
    main()
