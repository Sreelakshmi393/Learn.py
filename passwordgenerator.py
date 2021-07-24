import string
import random
def script():
    print("Welcome to Inovus Password Generator")
    print("Select the type of password required")
    print("1)Standard")
    print("2)Secure")
    print("3)Extreme")
    type = 1
    type = 2
    type = 3
    print("Which type of password do you want?")
    type = input("")
    if __name__== "__main__":
            if type == "1":
                plen = int(input("Enter password length\n"))
                s1 = string.ascii_lowercase
                # print(s1)
                s2 = string.ascii_uppercase
                # print(s2)
                s = []
                s.extend(list(s1))
                s.extend(list(s2))
                # print(s)
                random.shuffle(s)
                # print(s)
                password = "INO_"
                print(password+("".join(s[0:plen])))
            elif type == "2":
                plen = int(input("Enter password length\n"))
                s1 = string.ascii_lowercase
                # print(s1)
                s2 = string.ascii_uppercase
                # print(s2)
                s3 = string.digits
                s = []
                s.extend(list(s1))
                s.extend(list(s2))
                s.extend(list(s3))
                # print(s)
                random.shuffle(s)
                # print(s)
                password = "INO_"
                print(password+("".join(s[0:plen])))
            elif type == "3":
                plen = int(input("Enter password length\n"))
                s1 = string.ascii_lowercase
                # print(s1)
                s2 = string.ascii_uppercase
                # print(s2)
                s3 = string.digits
                # print(s3)
                s4 = string.punctuation
                # print(s4)
                s = []
                s.extend(list(s1))
                s.extend(list(s2))
                s.extend(list(s3))
                s.extend(list(s4))
                # print(s)
                random.shuffle(s)
                # print(s)
                password = "INO_"
                print(password+("".join(s[0:plen])))
            else:
                print("Oops!Invalid input. Try again")
            restart = input("Do you want to continue?If yes type 'Y' if not type 'N'\n")
            if restart == "y" or restart == "Y":
                     script()
            if restart == "n" or restart == "N":
                    print("Thank you for using. Come again")
script()
            
#print(password+("".join(s[0:plen])))



       
       



   
