L = float(input("Enter the Length of Plot (in meters): "))
W = float(input("Enter the Width of the Plot (in meters): "))

Area_of_plot = L * W

if L < 0 and W < 0:
    print("Enter Valid Input!")
else:
    print("The Area of the required Plot is: ", Area_of_plot)
