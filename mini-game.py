secret_number = 7
guess = int(input("Guess the secret number (between 1 and 10): "))
while guess != secret_number:
    if guess < secret_number:
        print("Too Low! Try again.")
    else:
        print("Too High! Try again.")
    guess = int(input("Try Again: "))
print("You got the right number!")