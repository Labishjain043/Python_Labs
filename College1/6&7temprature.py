celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

kelvin = celsius + 273.15

print(celsius, "degrees Celsius is equal to,", fahrenheit, "degrees Fahrenheit.")
print(celsius, "degrees Celsius is equal to", kelvin, "Kelvin.\n")

if fahrenheit == celsius:
    print("Fahrenheit and Celsius both are equal at", celsius)
