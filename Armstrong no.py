'''
A positive integer is called an  Armstrong numbr of order n if
abcd.... = a^n + b^n + c^n + d^n + ....

For Example:
153 = 1*1*1 + 5*5*5 + 3*3*3   // 153 is an  Armstorng number.
'''

num1 = 0
num2 = 10000

print("Armstrong Numbers are : ")
for number in range(num1,num2+1):
    num_length = len(str(number))
    sum = 0
    for digit in range(0, num_length):
        sum = sum + int(str(number)[digit])**num_length

    if sum == number:
        print(sum, end=", ")
