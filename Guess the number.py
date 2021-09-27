Hidden = 18
for i in range(0,9):
     if i >9:
         print("GAme Over !!!!")
         break
     else:
         print("Guess and Enter any number : ")
         num = int(input())
         if num == Hidden:
             print("Congratulation !!! YOU WON THE GAME.")
             print("You have taken total" , 9-i, "guesses")
             break
         elif num >=100:
             print("Your number is too Greater than the Hidden number . Please try below 100 ")
             print("Number of guesses left = ", 9 - i)
         elif num >= 10 and num <= 20:
             print("Your are near to the Hidden Number.")
             print("Number of guesses left = ", 9 - i)
         elif num > Hidden and num < 100:
             print("Your number is greater than the Hidden Number.")
             print("Number of guesses left = ", 9 - i)
         elif num < Hidden:
             print("Your number is less than the Hidden Number.")
             print("Number of guesses left = ", 9 - i)

     continue
