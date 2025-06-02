pattern = int(input("Enter the size of the pattern:"))
num = 0
is_true = True
while is_true:
    num += 1
    for x in range(pattern):
        print('*', end="")
    if num == pattern:
        is_true = False
    print()
