def time():

    seconds = int(input("How many seconds would you like to convert to minutes?: "))

    if seconds > 60:
        minutes = seconds / 60
        print(minutes)
    elif seconds < 60:
        minutes1 = seconds / 60
        print(minutes1)

time()
