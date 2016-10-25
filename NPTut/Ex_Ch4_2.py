print("The High/Low Game!!")
val = 23752
guess = 0
count = 0
while guess != val:
    guess = float(input("What is your guess: "))
    if guess == val and count == 0:
        print("Amazing!! You got it on the first try!!")
        print(" Go to Vegas immediately")
    elif guess == val:
        print("Thats right, you got it in ",count," tries")
    elif guess<val:
        print("Too low.")
        print(" You're on try number ",count)
        count=count+1
    elif guess>val:
        print("Too high.")
        print(" You're on try number ",count)
        count=count+1
    else:
        print("You should never get here.")
        count=count+1
        
