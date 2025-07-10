def generate_conditional_odd_series(a):
    if a % 2 != 0:
        count=a
    else:
        count=a - 1
    result = [2 * i + 1 for i in range(count)]
    return result

a = int(input("Enter a number: "))
series = generate_conditional_odd_series(a)
print("Output:", ', '.join(map(str, series)))
