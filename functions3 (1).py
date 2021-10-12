def Intinput(int1):
    try:
        int1 = int(int1)
        return int1
    except:
        print('Sorry, Not an Integer')
        int1 = 0
        return int1
length = input('Enter Value:')
length = Intinput(length)
width = input('Enter Value:')
width = Intinput(width)
