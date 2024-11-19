from random import randint
name=input("Enter your name : ")
num=int(input("Guess the number from 1 to 100 : "))
check=True
count=1
guess=randint(1,100)
while check:
    if num==guess:
        print(f"\nHurrey {name} took {count} times to guess")
        check=False
    elif num<guess:
        num=int(input("Please choose a larger number : "))
    else:
        num=int(input("Please choose a smaller number : "))
    count+=1
