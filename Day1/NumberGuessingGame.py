import random

secret_num=random.randint(1, 10)

while True:
    guess=int(input("Guess the number(1-10):"))

    if guess<secret_num:
        print("The guessed number is less than the secret number.")
    elif guess > secret_num:
        print("The guessed number is greater than the secret number.")
    else:
        print("Correct!You guessed secret number.")
        break

