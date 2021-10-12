length = int(input('What is the length of the room'))
width = int(input('What is the width of the room'))
height = int(input('What is the height of the room'))

side12 = (length * height) * 2
side34 = (width * height) * 2

sqft = side12 + side34
paint = sqft/400

print("The ammount of paint you need is",paint,"gallons.")
