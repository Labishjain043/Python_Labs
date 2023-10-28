def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def solve_quadratic():
    discriminant = b * b - 4 * a * c

    if discriminant > 0:
        sqrt_discriminant = discriminant ** 0.5
        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root1 = -b / (2 * a)
        return root1
    else:
        real_part = -b / (2 * a)
        imaginary_part = (-discriminant) ** 0.5 / (2 * a)
        return complex(real_part, imaginary_part), complex(real_part, -imaginary_part)


a_input = input("Enter the coefficient a: ")
b_input = input("Enter the coefficient b: ")
c_input = input("Enter the coefficient c: ")

if is_float(a_input) and is_float(b_input) and is_float(c_input):
    a = float(a_input)
    b = float(b_input)
    c = float(c_input)

    if a == 0:
        print("Coefficient 'a' cannot be zero. It's not a quadratic equation.")
    else:
        roots = solve_quadratic()
        print("Solutions:")
        for root in roots:
            if isinstance(root, complex):
                print("Complex root:", "{:.2f} + {:.2f}i".format(root.real, root.imag))
            else:
                print("Real root:", "{:.2f}".format(root))
else:
    print("Invalid input. Please enter valid coefficients (numbers).")
