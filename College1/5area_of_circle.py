Radius = int(input("Enter radius of circle (between 1 to 100): "))
Area = 22/7 * Radius**2

if 1 <= Radius <= 100:
    print("The Area of the required circle with radius", Radius, "is: ", Area)
else:
    print("This Program calculates Area of circles with '1 <= radius <= 100'")
