upper_bound_num = int(input('Enter an upper bound for a check: '))
deficient = 0
perfect = 0
abundant = 0

for num in range(1, upper_bound_num + 1):
    divisors = 0
    for i in range(1, num):
        if num % i == 0:
            divisors += i

    if divisors < num:
        deficient += 1
    elif divisors == num:
        perfect += 1
    else:
        abundant += 1

print(f"Between 1 and {upper_bound_num} there are")
print(f"{deficient } deficient numbers")
print(f"{ perfect} perfect numbers")
print(f"{abundant } abundant numbers")

