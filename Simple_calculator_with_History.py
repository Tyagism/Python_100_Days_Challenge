# Creating a Simple Calculator with Continous Operations in Python with history feature

def Options():
    print("Select Operations.\n","1. Addition\n", "2. Subtacation\n", "3. Multiplication\n",
           "4. Division\n", "5. Exit\n", "6. History\n", "7. Clear History\n", "8. Continue with Previous Result / Calculations\n")
    

Options()
history = []
num1 = float(input("\nEnter First Number : "))
num2 = float(input("\nEnter Second Number : "))
result = 0
while True:
    choice = input("\n Enter Choice(1/2/3/4/5/6/7/8): ")
    if choice in ('1','2','3','4'):
        if choice == '1':
            result = (num1 + num2)
            print(num1,"+",num2,"=",result)
            history.append(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = (num1 - num2)
            print(num1,"-",num2,"=",result)
            history.append(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = (num1 * num2)
            print(num1,"*",num2,"=",result)
            history.append(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = (num1 / num2)
            print(num1,"/",num2,"=",result)
            history.append(f"{num1} / {num2} = {result}")
        
        next_calculation = str(input("\nDo you want to continue with previous result? (y/n): "))

        if next_calculation.lower() == 'y' or 'yes':
            num1 = result
            num2 = float(input("Enter Second Number for next Calculation: "))
            Options()
        else:
            Options()
            num1 = float(input("Enter First Number : "))
            num2 = float(input("Enter Second Number : "))
    
    elif choice == '5':
        print("\nExiting the Calculator. Goodbye!")
        break
    elif choice == '6':
        print("\nCalculation History:")
        for record in history:
            print(record)
    elif choice == '7':
        history.clear()
        print("\nHistory Cleared.")
    elif choice == '8':
        if result != 0:
            num1 = result
            num2 = float(input("Enter Next Number: "))
        else:
            print("\nNo previous result found. Please perform a calculation first.")
            num1 = float(input("Enter First Number : "))
            num2 = float(input("Enter Second Number : "))
    else:
        print("\nInvalid Input :(")