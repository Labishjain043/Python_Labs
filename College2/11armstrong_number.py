number = int(input("Enter a 3-digit number: "))

if number < 100 or number > 999:
    print("Please enter a valid 3-digit number.")
else:
    original_number = number
    sum_of_cubes = 0

    while number > 0:
        digit = number % 10
        sum_of_cubes += digit ** 3
        number //= 10

    if sum_of_cubes == original_number:
        print(original_number, "is an Armstrong number.")
    else:
        print(original_number, "is not an Armstrong number.")
