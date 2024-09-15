from random import randint

# Add numbers to the list of possible characters
characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
              "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

password = input("Password: ")
guess = ""

while guess != password:
    guess = ""
    for _ in range(len(password)):
        guess += characters[randint(0, len(characters)-1)]
    print(f"Trying guess: {guess}")

print("Password guessed!")
