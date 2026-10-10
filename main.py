students = ["Bai Inga", "Aminata", "Foday"]
print(students)

print("my best friend is{students[0]} ")
print("my best friend is{students[1]} ")
print("my best friend is{students[2]} ")

# git the index of an items in a list
print(students.index("Bai Inga"))
print(students.index("Aminata"))
print(students.index("Foday"))
# know the number of items in a list
print(f"The total items in the list is : {len(students)}")

# Add items to a list 
students.append("Isatu")
print(students)
students += ["Kadiatu", "John", "Bintu"]
print(students)
students.insert(4, "Donald")
print(students)


# extending a list
fruits = ["Apple", "Banana", "Mango"]
students.extend(fruits)
print(students)

# removing an items from a list 
fruits.remove("Mango")

students.pop()
students.pop()
thirditem = students.pop()
print(students)
print(thirditem)