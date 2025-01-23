import random 


number = random.randint(1,100)
num = 0 
print("********************")
print("ENTER NUM FROM 1 - 100")


while True:
    guess = int(input("Enter Guess:"))

    if guess>100 or guess <1:
        print("Between 1 to 100 only!!")
    elif guess>number:
        print("Too High!")
        num += 1
    elif guess<number:
        print("Too Low")
        num +=1
    else:
        print(f"You are Correct!")
        break

print(f"Game over. It took you {num} guesses")

5
