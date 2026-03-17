#Student Course MAnagement System

#use of => list, tuple, set, dictionary
#info=> student name, course details, unqniue skill, student information

#student name=> list
#course details=> tuple
#unique skill=> set
#student information=> dictionary

#user input through => if else,
#add student => display them => add skills => show skills => add course details => show course details

def add_student_name():
    student_name=[]
    sN=input("Enter student name: ")
    student_name.append(sN)
    return student_name

def add_course_details():
    course_details=()
    course_name=input("Enter course name: ")
    course_details=course_details+(course_name,)
    return course_details

def add_unique_skill():
    unique_skill=set()
    skill=input("Enter unique skill: ")
    unique_skill.add(skill)
    return unique_skill

def add_student_info(student_name):
    student_info={}
    student_info["Name"]=student_name
    student_info["Age"]=int(input("Enter student age: "))
    return student_info

def display_student_info(student_name, course_details, unique_skill, student_info):
    print("Student Name:", student_name)
    print("Course Details:", course_details)
    print("Unique Skills:", unique_skill)
    print("Student Information:", student_info)

#main function to run the program
def main():
    while True:
        print("1. Add Student Name")
        print("2. Add Course Details")
        print("3. Add Unique Skill")
        print("4. Add Student Information")
        print("5. Display Student Information")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_name = add_student_name()
        elif choice == '2':
            course_details = add_course_details()
        elif choice == '3':
            unique_skill = add_unique_skill()
        elif choice == '4':
            student_info = add_student_info(student_name)
        elif choice == '5':
            display_student_info(student_name, course_details, unique_skill, student_info)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
