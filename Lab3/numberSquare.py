n = int(input("Enter the number: "))

for i in range(2 * n - 1):
    for j in range(2 * n - 1):
        x = max(abs(n - 1 - i), abs(n - 1 - j))
        print(x + 1, end=" ")
    print()