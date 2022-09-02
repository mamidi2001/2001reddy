#creating dog dictionary
dog=dict()
dog["Name"]="Tannie"
dog["Color"]="Black"
dog["Breed"]="Pomeranian"
dog["legs"]=4
dog["Age"]=12
print(" Dog dictionary is : ",dog)
print()

#creating student dictionary
student=dict()
student["first_name"]="Pranathi Reddy"
student["last_name"]="Mamidi"
student["Gender"]="Female"
student["Age"]=21
student["Martal status"]="single"
student["Skills"]=["python","Java","AWS"]
student["Country"]="India"
student["City"]="Nizamabad"
student["Address"]="street no 6"
print("Student dictionary is : ",student)


#length of student dictionary
print("length of student dictionary is : ",str(len(student)));

#value of student skills and datatype
print("student skills are : ",end='')
print(student["Skills"])
print("type of student skills is : ",type(student["Skills"]))

#modifying student skills
student["Skills"].append("Skill A")
student["Skills"].append("Skill B")
print("modified student skills : ",student["Skills"])

#getting dictionary keys as list
dog_keys=list(dog.keys())
print("dog dictionary keys : ",dog_keys)
student_keys=list(student.keys())
print("student dictionary keys : ",student_keys)
dog_values=list(dog.values())
print("dog dictionary values : ",dog_values)
student_values=list(student.values())
print("student dictionary values : ",student_values)
