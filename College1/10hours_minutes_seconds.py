# Input a number of seconds
seconds = int(input("Enter the number of seconds (1 to 86400): "))

# Check for valid input range
if 1 <= seconds <= 86400:
    # Calculate hours, minutes, and seconds
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    # Display the result
    print(" Hours   : ", hours, "\n Minutes : ", minutes, "\n Seconds : ", seconds)
else:
    print("Invalid input: Please enter a number between 1 and 86400.")
