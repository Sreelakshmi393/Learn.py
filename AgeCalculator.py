from datetime import date
y = date.today().year
m = date.today().month
d = date.today().day

print("You want to calculate your age.......")
print("Wow....Come let's do it.......")
print(date.today())

year = int(input("Enter your birth year : "))
month = int(input("Enter your birth month : "))
day = int(input("Enter your birth day : "))

if day > d and month >= m:
    dd = (d + 30) - day
    mm = ((m - 1) + 12) - month
    yy = (y - 1) - year
    print("You are " + str(yy) + " Years " + str(mm) + " Months " + str(dd) + " Days old")
    
elif day > d and month < m:
    dd = (d + 30) - day
    mm = m - month
    yy = y - year
    print("You are " + str(yy) + " Years " + str(mm) + " Months " + str(dd) + " Days old")

elif day < d and month > m:
    dd = d - day
    mm = (m + 12) - month
    yy = (y - 1) - year
    print("You are " + str(yy) + " Years " + str(mm) + " Months " + str(dd) + " Days old")

else: 
    dd = d - day
    mm = m - month
    yy = y - year
    print("You are " + str(yy) + " Years " + str(mm) + " Months " + str(dd) + " Days old")