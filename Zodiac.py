Year = int(input('Enter a year: '))
Zodiac = Year % 12
if Zodiac == 0:
    print('monkey')
elif Zodiac == 1:
    print('rooster')
elif Zodiac == 2:
    print('dog')
elif Zodiac == 3:
    print('pig')
elif Zodiac == 4:
    print('rat')
elif Zodiac == 5:
    print('ox')
elif Zodiac == 6:
    print('tiger')
elif Zodiac == 7:
    print('rabbit')
elif Zodiac == 8:
    print('dragon')
elif Zodiac == 9:
    print('snake')
elif Zodiac == 10:
    print('horse')
else:
    print('Goat')
