def generate_odd_series(a):
    result = []
    for i in range(a):
        result.append(2 * i + 1)
    return result

a = int(input("Enter a number: "))
series = generate_odd_series(a)
print("Output:", ', '.join(map(str, series)))
