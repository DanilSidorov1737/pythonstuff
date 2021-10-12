height = float(input('What is your height? (meters) '))
weight = int(input('What is your weight? (kg) '))

a = weight
b = height **2
BMI = a / b

if (BMI < 18.5):
    print('This is considered Underweight.')
elif (BMI > 18.5 and BMI < 25):
    print("This is considered Normal Weight")
elif (BMI > 25 and BMI <30):
    print('This is considered overweight')
elif(BMI > 30):
    print('This is considered Obese')


print('Your BMI is',BMI)
