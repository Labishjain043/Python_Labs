input_list = input("Enter a list of strings separated by spaces: ").split()

uppercase_strings = [s.upper() if s[0].islower() else s for s in input_list]

print("Strings converted to uppercase if first character is lowercase:", uppercase_strings)
