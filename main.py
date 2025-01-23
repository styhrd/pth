questions = ["What is My Name? ",
             "What is my Team? ",
             "Who is my favorite Player? "]

options = (("A. Miguel","B. Juan","C. Aklas"),
           ("A. Dallas", "B. Celtics", "C. Wolves"),
           ("A. Kobe", "B. Jordan", "C. Ant"))

answers=("A","C","C")
guesses=[]
score = 0 
question_num = 0

for question in questions:
    print("**********************")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter Your Guess: ")
    guesses.append(guess)
    if guess == answers[question_num]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    question_num +=1


print (f"Total Score: {score}")