# animal personality quiz

def ask_questions():
    lion = 0
    eagle = 0
    dolphin = 0
    snake = 0

    # Q1
    print("Q1: What do you prefer?")
    print("1) Adventure  2) Learning  3) Fun  4) Power")
    ans = input("Enter choice: ")

    if ans == "1":
        lion += 1
    elif ans == "2":
        eagle += 1
    elif ans == "3":
        dolphin += 1
    elif ans == "4":
        snake += 1

    # Q2
    print("\nQ2: What is your strength?")
    print("1) Courage  2) Intelligence  3) Friendliness  4) Strategy")
    ans = input("Enter choice: ")

    if ans == "1":
        lion += 2
    elif ans == "2":
        eagle += 2
    elif ans == "3":
        dolphin += 2
    elif ans == "4":
        snake += 2

    # Q3
    print("\nQ3: Where would you like to be?")
    print("1) Jungle  2) Sky  3) Ocean  4) Desert")
    ans = input("Enter choice: ")

    if ans == "1":
        lion += 3
    elif ans == "2":
        eagle += 3
    elif ans == "3":
        dolphin += 3
    elif ans == "4":
        snake += 3

    return lion, eagle, dolphin, snake


def show_result(l, e, d, s):
    print("\nScores:")
    print("Lion:", l)
    print("Eagle:", e)
    print("Dolphin:", d)
    print("Snake:", s)

    if l >= e and l >= d and l >= s:
        print("You are a Lion 🦁 (Brave and strong)")
    elif e >= d and e >= s:
        print("You are an Eagle 🦅 (Smart and focused)")
    elif d >= s:
        print("You are a Dolphin 🐬 (Friendly and fun)")
    else:
        print("You are a Snake 🐍 (Calm and strategic)")


l, e, d, s = ask_questions()
show_result(l, e, d, s)
