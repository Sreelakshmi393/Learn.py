weight = int(input("Enter your weight : "))
unit = input("Unit in which you entered the weight [(L)bs or (K)g ]: ")
if unit.upper() == "L":
    converted = weight*0.45
    print(f"You are {converted} kilograms")
else:
    converted = weight/0.45
    print(f"You are {converted} pounds")