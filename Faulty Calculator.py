'''
Design a calculator Which will correctly solve all the Operations except the following Ones:
45*3=555   , 56+9=77  , 56/2=4
'''

def calculator():
    operator= input("Enter your arithmetic operator (+,-,*,/,%):")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the Second nuber: "))

    add = '+'
    sub = '-'
    mul = '*'
    div = '/'
    mod = '%'

    if operator == add:
        if num1==56 and num2==9 or num1==9 and num2==56:
            print(f"Result of {num1}+{num2} is 77")
        else:
            print(f"Result of {num1}+{num2} = ",num1+num2)

    elif operator==sub:
        print(f"Result of {num1}-{num2} = ", num1-num2)

    elif operator==mul:
        if num1==45 and num2==3 or num1==3 and num2==45:
            print(f"Result of {num1}*{num2} is 555")
        else:
            print(f"Result of {num1}*{num2} = ",num1*num2)


    elif operator==div:
        if num1==56 and num2==2 or num1==2 and num2==56:
            print(f"Result of {num1}/{num2} is 4")
        else:
            print(f"Result of {num1}/{num2} = ",num1/num2)

    elif operator==mod:
        print(f"Result of {num1}%{num2} = ",num1%num2)

    else:
        print("Enter a valid input to Perform ...!")

    again()

def again():
    cal_again = input("\n Do you want to calculate again .? \nplease type y or YES  or n for NO \n")
    if cal_again=='y':
        calculator()
    elif cal_again=='n':
        print("Thank you . See you later")
    else: again()

calculator()

