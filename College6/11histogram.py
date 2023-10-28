range_1_2, range_3_4, range_5_6, range_7_8, range_9_10, total = 0, 0, 0, 0, 0, 0

while True:
    user_input = int(input("Enter a number from 1 to 10 (or -1 to exit): "))

    if user_input == -1:
        break
    if 1 <= user_input <= 2:
        range_1_2 += 1
    elif 3 <= user_input <= 4:
        range_3_4 += 1
    elif 5 <= user_input <= 6:
        range_5_6 += 1
    elif 7 <= user_input <= 8:
        range_7_8 += 1
    elif 9 <= user_input <= 10:
        range_9_10 += 1
    else:
        print("Invalid input. Please enter a number between 1 and 10.")

    total += 1

percentage_1_2 = (range_1_2 / total) * 100
percentage_3_4 = (range_3_4 / total) * 100
percentage_5_6 = (range_5_6 / total) * 100
percentage_7_8 = (range_7_8 / total) * 100
percentage_9_10 = (range_9_10 / total) * 100

print("1 - 2:", '#' * range_1_2, f"{percentage_1_2:.2f}%")
print("3 - 4:", '#' * range_3_4, f"{percentage_3_4:.2f}%")
print("5 - 6:", '#' * range_5_6, f"{percentage_5_6:.2f}%")
print("7 - 8:", '#' * range_7_8, f"{percentage_7_8:.2f}%")
print("9 - 10:", '#' * range_9_10, f"{percentage_9_10:.2f}%")
