students = []
def add_student(name, age, state, course):
               student = { 
                       "name": name,
                       "age": age,
                       "state": state,
                       "course": course
       }
       students.append(student)
       
def display_all():
       print("\n======= STUDENTS PROFILES=======")
       for student in students:
             print("Name:", student["name"])
             print("Age:", student["age"])
             print("State:", student["state"])
             print("Course:", student["course"])
       print("-------------------------------------------")
       print("Total Profiles:", len(students))
       
add_student("Edidiong", "18", "Akwa Ibom", "Software Engineering")     
add_student("Blessed", "19", "Akwa Ibom", "Mathematics Education")
add_student("Joel", "21", "Enugu", "ComputerbScience")
add_student("Goodness", "19", "Akwa Ibom", "Software Engineering")
add_student("Amaka","18", "Akwa Ibom", "English Education")      
add_student("Stephanie", "17","Oyo", "Nursing")

display_all()