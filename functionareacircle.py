def circle():
    try:
        radius = int(input('Enter Radius:'))
        area = 3.14 * radius **2
        return area
    except:
        print('Sorry, Not an Integer!')
        radius = 0
        return radius

print(circle())

    


