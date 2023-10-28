side1 = float(input("Enter the first side of the triangle:"))
side2 = float(input("Enter the second side of the triangle:"))
side3 = float(input("Enter the third side of the triangle:"))

if side1 > 0 and side2 > 0 and side3 > 0:
    if side2 + side3 >= side1 and side1 + side2 >= side3 and side1 + side3 >= side2:
        print("The triangle with these sides is possible!")
    else:
        print("The triangle with these sides is not possible. Please Enter valid input!")
else:
    print("The triangle with these sides is not possible. Please Enter valid input!")
