import json

# Function to print student list
def print_students(students):
    for s in students:
        print(f"{s['L_Name']}, {s['F_Name']} : ID = {s['Student_ID']} , Email = {s['Email']}")

# Load JSON file into list
with open('Student.json', 'r') as file:
    student_list = json.load(file)

# Output original list
print("\n--- Original Student List ---")
print_students(student_list)

# Add YOUR student (CHANGE THIS TO YOUR INFO)
new_student = {
    "F_Name": "Sebastian",
    "L_Name": "Siqueiros",
    "Student_ID": 293020,
    "Email": "seb.siqueiros@gmail.com"
}

student_list.append(new_student)

# Output updated list
print("\n--- Updated Student List ---")
print_students(student_list)

# Write updated list back to JSON file
with open('Student.json', 'w') as file:
    json.dump(student_list, file, indent=4)

print("\nStudent.json file has been updated.")
