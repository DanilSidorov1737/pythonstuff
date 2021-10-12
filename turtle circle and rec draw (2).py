shape = input('Specify whether you want to draw a rectangle, or circle: ')
width = int(input('Enter width of your shape: '))
length= int(input('Enter Length: '))

try:
    if shape == 'circle':
        import turtle
        turtle.bgcolor("Yellow")
        turtle.pencolor('Blue')
        turtle.circle(width)
except ValueError:
        print('Wrong')
        

        



    
