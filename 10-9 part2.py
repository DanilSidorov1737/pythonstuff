##    try:
##        Sum = 0
##        while True:
##            num1 = input("Enter a Number or q to quit:")
##            if num1 == "q" or num1 == "Q":
##                break
##            Sum = Sum + float(num1)
##        print(Sum)
##           
##    except:
##        print("try again")
##        counter = 0
##        while counter < 1000:
##            num1 = input("Enter a Number or q to quit:")
##            if num1 == "q" or num1 == "Q":
##                break
##            Sum = Sum + float(num1)
##            print(Sum)
##            counter += 1


while True:
    try:
        num1 = int(input("Enter a number or q to quiz: "))
        if num1 == "q" or num1 == "Q":
            break
        Sum = Sum + float(num1)
        print(Sum)
        else:
            print("This input is not in range.")

    except ValueError:
      print("Invalid Input")
      continue 
    
    
