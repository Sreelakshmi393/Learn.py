row=int(input("Enter number of rows : "))
for i in range(row):
    print("*"*(i+1))
for j in range(row):
    print("*"*(row-j-1))