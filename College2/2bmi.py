weight = float(input("Enter your weight in Kilograms: "))
height = float(input("Enter your height in meters: "))

# First part of the problem

bmi = weight/height ** 2

if weight > 0 and height > 0:
    print("Your Body Mass Index(BMI) is: ", bmi)
else:
    print("Please Enter a valid input!")

# Second part of the problem

weight = float(input("Enter your weight in Pounds: "))
height = float(input("Enter your height in inches: "))

weight = weight * 0.453592
height = height * 0.0254

bmi = weight/height**2

if weight > 0 and height > 0:
    print("Your Body Mass Index(BMI) is: ", bmi)
else:
    print("Please Enter a valid input!")
