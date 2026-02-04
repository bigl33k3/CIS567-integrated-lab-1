start = int(input())
end = int(input())

if end < start:
    print("Second integer can't be less than the first.")
else:
    value = start
    while value <= end:
        print(value, end=' ')
        value += 5
    print()
