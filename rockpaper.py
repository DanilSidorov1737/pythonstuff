import random

def Game():
    try:
        Num1 = int(input("Choose 1 - Rock | 2 - Paper | 3 - Scissors: "))
        if Num1 >= 1 and Num1 <= 3:
            print('Get Ready and ....')
        else:
            print("Wrong Numbers")
        Num2 = (random.randint(1,3))
        

        if Num1 == 1 and Num2 == 3:
            print('Scissors \n You Win')
        elif Num1 == 2 and Num2 == 1:
            print('Rock \n You Win')
        elif Num1 == 3 and Num2 == 2:
            print('Paper \n You Win')
        elif Num1 == Num2:
            print("Tie Game")
        else:
            print("Sorry You lose")
        
        
    except:
        print("Sorry That's Not an Integer")
            

Game()
            
