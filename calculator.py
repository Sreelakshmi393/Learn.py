def calc():
    while True:
        print("Let's calculate whatever you want")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Percentage")
        print("6.Square root")
        print("7.Power")
        opt = input("Which operation do you want to perform? ")
        if opt == '1':
           n1 = int(input("Enter first number : "))
           n2 = int(input("Enter second number : "))
           result = n1 + n2
           print("The result is : ",result)
        elif opt == '2':
            n1 = int(input("Enter first number : "))
            n2 = int(input("Enter second number : "))
            result = n1 - n2
            print("The result is : ",result)
        elif opt == '3':
            n1 = int(input("Enter first number : "))
            n2 = int(input("Enter second number : "))
            result = n1 * n2
            print("The result is : ",result)
        elif opt == '4':
            n1 = int(input("Enter first number : "))
            n2 = int(input("Enter second number : "))
            result = n1 / n2
            print("The result is : ",result)  
        elif opt == '5':
            n1 = int(input("Enter first number : "))
            n2 = int(input("Enter the percentage without sign : "))
            result = (n1*n2)/100
            print("The result is : ",result)  
        elif opt == '6':
            n1 = int(input("Enter number : "))
            result = n1 ** 0.5
            print("The result is : ",result) 
        elif opt == '7':
            n1 = int(input("Enter first number : "))
            n2 = int(input("Enter second number : "))
            result = n1 ** n2
            print("The result is : ",result)   
        else:
            print("No operation available")
            break
        ch = input("Do you want to continue? Give 'Y' if you want otherwise give 'N'")
        if ch.lower == 'N':
            print("Thank you for using me....")
            break
calc()


        
            


    