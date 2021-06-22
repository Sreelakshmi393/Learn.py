name = input("Enter your name :")
age = input("Enter your age :")
designation = input("Enter your designaton :")
list = []
for i in range(3):
    skills = input("Enter your skills :")
    list.append(skills)
print("My name is",name)
print("I'm",age,"years old")
print("Currently I'm a",designation)
print("I'm skilled in")
print(*list, sep = ",")