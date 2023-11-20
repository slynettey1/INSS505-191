import random

number1 =int(input('Enter a number:'))
if number1 % 3==0 and number1 % 5 ==0:
    print(number1,'tic tac')
elif number1 % 3==0:
    print(number1, 'tic')
elif number1 % 5==0:
    print(number1, 'tac')
#step6
a=1
while a<= 20:
    print(a)
    a+=1
#step7
while a<=20:
    if a % 3==0 and a %5 ==0:
      print(a, 'tic tac')
    elif a % 3==0:
      print(a,'tic')
    elif a % 5==0:
      print (a,'tac')
    else:
      print(a)
    a += 1
    # step 8
ramdom_number = random.randint(1,90)
#step 9
count = 0
while count< 6:
    user_digit = int(input("Please enter a value:"))
    if user_digit >0:
        break
    else:
        print("The value entered is not correct. Please reenter")
        count+= 2
#step 10
if count <5:
    random_number = random.randint(1,user_digit)
    print("Random number generated:", random_number)
else:
    print("No valid input after 5 attempts")


