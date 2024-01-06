print("****************************************************************************************")
print("--------------------------------CALCULATOR PROGRAM--------------------------------------")
print("****************************************************************************************")
print()
ch='y'
while(ch.lower()=='y'):
    print("The operations of the calculatiors are,")
    print("ADDITION(1)")
    print("SUBTRACTION(2)")
    print("MULTIPLICATION(3)")
    print("DIVISION(4)")
    print("MODULO DIVISION(5)")
    print()
    print("Operations can choose with their number at their end...")
    print()
    n1=int(input("Enter the first number: "))
    n2=int(input("Enter the second number: "))
    choice=int(input("Enter the choice of operation: "))
    if choice==1:
        print("The addition of the given two numbers is : ",n1+n2)
    elif choice==2:
        print("The difference of the given two numbers is : ",n1-n2)
    elif choice==3:
        print("The multiplication of the given two numbers is : ",n1*n2)
    elif choice==4:
        print("The division of the given two numbers is : ",n1/n2)
    elif choice==5:
        print("The Modulo division of the given two numbers is : ",n1%n2)
    else:
        print("Given an valid choice of input..!")
    print()
    ch=input("Do you want to continue(y/n): ")
print("Thank you for using the Calculator :)")