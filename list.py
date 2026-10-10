students = ["Mohamed", "Aminata", "Foday"]
print(students)

print("my best friend is{students[0]} ")
print("my best friend is{students[1]} ")
print("my best friend is{students[2]} ")

# git the index of an items in a list
print(students.index("Mohamed"))
print(students.index("Aminata"))
print(students.index("Foday"))
# know the number of items in a list
print(f"The total items in the list is : {len(students)}")

# Add items to a list 
students.append("Isatu")
print(students)
students += ["Kadiatu", "John", "Bintu"]