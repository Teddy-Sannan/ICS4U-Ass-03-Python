import random


def main():
    numbers = []

    try:
        for number in range(0, 250):
            integer = random.randint(0, 100)
            numbers.append(integer)

        guess = int(input("Enter your guess: "))

        for guesses in numbers:
            if guesses == guess:
                print("You got it!")

        print("Sorry you didnt get it")

    except ValueError:
        print("")
        print("Invalid Input")


if __name__ == "__main__":
    main()
    