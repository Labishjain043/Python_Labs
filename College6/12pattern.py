N = int(input("Enter the value of N: "))

if N <= 0:
    print("Please enter a positive integer.")
else:
    print('+' + '/\\' * N + '+')
    for i in range(N):
        print('|' + ' ' * (2 * N - 1) + '|')
    print('+' + '/\\' * N + '+')
