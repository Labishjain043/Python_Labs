N = int(input("Enter a positive integer N: "))

divisible_count = 0
non_divisible_count = 0

num = int(input("Enter a number (Write -999 to stop): "))

while num != -999:
    if num % N == 0:
        divisible_count += 1
    else:
        non_divisible_count += 1
    num = int(input("Enter a number (Write -999 to stop): "))

print("Count of numbers divisible by", N, ":", divisible_count)
print("Count of numbers not divisible by", N, ":", non_divisible_count)
