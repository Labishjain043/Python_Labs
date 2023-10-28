real1 = float(input("Enter the real part of the first complex number: "))
imaginary1 = float(input("Enter the imaginary part of the first complex number: "))
complex1 = complex(real1, imaginary1)

real2 = float(input("\nEnter the real part of the second complex number: "))
imaginary2 = float(input("Enter the imaginary part of the second complex number: "))
complex2 = complex(real2, imaginary2)

sum_result = complex1 + complex2
mul_result = complex1 * complex2

print("\nSum of the complex numbers:", sum_result)
print("Multiplication of the complex numbers:", mul_result)
