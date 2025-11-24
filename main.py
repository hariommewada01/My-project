import pandas as pd
import os

# File name where we will store student records
FILE = "students.csv"

# If the file does not exist, then create an empty file with proper columns
if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["Roll", "Name", "M1", "M2", "M3", "Total", "Percentage", "Grade"])
    df.to_csv(FILE, index=False)


# This function returns grade based on percentage marks
def give_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


# Add student details into file
def add_student():
    print("\nEnter Student Details:")
    roll = input("Roll Number: ")
    name = input("Name: ")
    m1 = float(input("Marks in Subject 1: "))
    m2 = float(input("Marks in Subject 2: "))
    m3 = float(input("Marks in Subject 3: "))

    total = m1 + m2 + m3
    percentage = total / 3
    grade = give_grade(percentage)

    data = pd.read_csv(FILE)
    data.loc[len(data)] = [roll, name, m1, m2, m3, total, percentage, grade]
    data.to_csv(FILE, index=False)

    print("\n✔ Student Record Added Successfully!\n")


# Show all stored records
def show_records():
    data = pd.read_csv(FILE)
    print("\n--- All Records ---")
    print(data.to_string(index=False))
    print()


# Main Menu for user
while True:
    print("\n===== Student Result Management System =====")
    print("1. Add Student Record")
    print("2. View All Records")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_records()
    elif choice == "3":
        print("\nThank You for Using the System!")
        break
    else:
        print("\nInvalid Input! Please try again.\n")
