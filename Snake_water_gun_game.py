import random

while True:
    computer = random.choice([-1, 0, 1])
    youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")

    yourDict = {"s": 1, "w": -1, "g": 0}
    reverse_dict = {1: "Snake", -1: "Water", 0: "Gun"}

    if youstr not in yourDict:
        print("Invalid input! Please enter s, w, or g.")
        continue

    you = yourDict[youstr]

    print(f"Your choice: {reverse_dict[you]}")
    print(f"Computer chose: {reverse_dict[computer]}")

    if computer == you:
        print("It's a Draw!\n")

    else:
        # Snake(1) drinks Water(-1)
        if you == 1 and computer == -1:
            print("Congratulations! You win!\n")
        elif you == -1 and computer == 1:
            print("You lose!\n")

        # Gun(0) kills Snake(1)
        elif you == 0 and computer == 1:
            print("Congratulations! You win!\n")
        elif you == 1 and computer == 0:
            print("You lose!\n")

        # Water(-1) damages Gun(0)
        elif you == -1 and computer == 0:
            print("Congratulations! You win!\n")
        elif you == 0 and computer == -1:
            print("You lose!\n")

        else:
            print("Unexpected condition!\n")
