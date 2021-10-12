try:
    grade = int(input("What is you grade? (0-2000): "))

    if grade < 1200:
        print("Sorry, but you failed.")
    elif grade >= 1200 and grade < 1400:
        print("you will need to retake the exam")
    elif grade >= 1400 and grade <= 2000:
        print("Congrats you passed")
except:
    print("Sorry this is not a valid grade")
