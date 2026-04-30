# roller coaster entry system

def check_ride():
    try:
        height = int(input("Enter your height (cm): "))
        credits = int(input("Enter your credits: "))
    except:
        print("Invalid input")
        return

    if height < 137:
        print("Sorry, not enough height")
    elif credits < 10:
        print("Not enough credits")
    else:
        print("Enjoy your ride!")


check_ride()
