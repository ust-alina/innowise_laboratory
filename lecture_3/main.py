students = []

choice: str = ""


#Check student exist
def checkstudent(name: str):
    name = name.strip().lower()
    for student in students:
        if student["name"] == name:
            return True
    return False


#Add new student p.1
def studentname(name: str):
    name = name.strip().lower()
    if checkstudent(name) == True:
        print("The student already exist.")
        return
    newstudent = {"name": name, "grades": []}
    students.append(newstudent)
 
#Add student grades p.2
def studentgrades(name: str):
     if not students:
        print("No students.")
        return
     
     grade: str = ""
     for student in students:
        if student["name"] == name.lower():
            while True:
                grade = input("Enter a grade (or 'done' to finish): ")
                if grade.lower() == 'done':
                    break
                if grade.isdigit():
                    grade_num = int(grade)
                    if 0 <= grade_num <= 100:
                        student["grades"].append(grade_num)
                    else:
                        print("Grade must be between 0 and 100.")
                else:
                    print("Invalid input. Please enter a number.")
            return
    

#Show report of students average p.3    
def showreport():
    if not students:
        print("No students to show.")
        return

    print("--- Student Report ---")

    averages = []  

    for student in students:
        grades = student["grades"]

        try:
            average = sum(grades) / len(grades)   
            print(f"{student['name'].title()}'s average grade is {round(average,1)}")
            averages.append(average)

        except ZeroDivisionError:
          
            print(f"{student['name'].title()}'s average grade is N/A")
          
            continue

    print("--------------------------")

    if not averages:
        print("No students with grades to calculate statistics.")
        return

    print(f"Max Average: {round(max(averages),1)}")
    print(f"Min Average: {round(min(averages),1)}")
    print(f"Overall Average: {round(sum(averages) / len(averages),1)}")



#Show top student p.4
def showtopstudent(): 
    students_with_grades = [s for s in students if s["grades"]]
    if not students_with_grades:
        print("No students with grades to determine top student.")
        return

    if not students:
        print("No students in the system.")
        return
    
    top_student = max(
        students,
        key=lambda s: (sum(s["grades"]) / len(s["grades"])) if s["grades"] else 0
    )
    
    average = (sum(top_student["grades"]) / len(top_student["grades"])) if top_student["grades"] else 0
  
    
    print(f"The student with the highest average is {top_student['name'].title()} with a grade of {round(average,1)}") 
    

# Main Loop
valid_choices = {"1", "2", "3", "4", "5"}

while True:
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Show report")
    print("4. Find top student")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice not in valid_choices:
        print("Invalid choice. Please enter a number from 1 to 5.")
        continue

    if choice == "1":
        name = input("Enter student name: ")
        studentname(name)
    
    elif choice == "2":
        if not students:
            print("No students.")
            continue
        
        name = input("Enter student name: ")
        if checkstudent(name):
            studentgrades(name)
        else:
            print("Student not found")
    
    elif choice == "3":
        showreport()
    
    elif choice == "4":
        showtopstudent()
    
    elif choice == "5":
        print("Exiting program...")
        break