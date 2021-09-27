try:
    a= int(input("Enter the no. of Rows : "))
    b= int(input("Enter the pattern(0 or 1): "))
    if b==0:
        count = 0
        while(count<=a):
            print("* " * count, end="")
            print("\n", end="")
            count = count+1

    elif b==1:
        count = a
        while(count!=0):
            print("* " * count, end="")
            print("\n", end="")
            count = count-1

    else:
        print("Invalid Input..!!!")

except Exception as e :
    print("Invalid Input  !!!!")
