import random

choices=["rock","paper","scissors"]
user_score=0
computer_score=0

while True:
    user=input("Enter rock,paper,scissors or quit:")
    if user=="quit":
        break
    if user not in choices:
        print("Invalid choice!Try again.")
        continue
    
    computer=random.choice(choices)
    print("Computer choice:",computer)
    
    if user==computer:
        print("It's a tie!")
    elif (user=="rock" and computer=="scissors") or \
         (user=="paper" and computer=="rock") or \
         (user=="scissors" and computer=="paper"):
        print("You win!")
        user_score+=1
    else:
        print("Computer wins!")
        computer_score+=1
    print("Score:")
    print(f"You:{user_score} and Computer:{computer_score}")
    print("-" * 50)

print("Final Score:")
print(f"You:{user_score} and Computer:{computer_score}")
print("Thank you for playing.")
