side1 = float(input('Side one value: '))
side2 = float(input('Side two value: '))
height = float(input("Height of trapezoid: "))

area = ((side1 + side2) / 2) * height
if side1 >= 0 and side2 >= 0 and height >= 0:
    print("Area is: ", area)
else:
    print("Please Enter a Valid Input!")
