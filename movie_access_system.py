# movie access system

def check_movie_access():
    try:
        age = int(input("Enter your age: "))
        parent = input("With parent? (yes/no): ")
    except:
        print("Invalid input")
        return

    if age >= 18:
        print("You can watch any movie")
    else:
        if parent.lower() == "yes":
            print("You can watch PG-13 movies")
        else:
            print("You can only watch G-rated movies")


check_movie_access()
