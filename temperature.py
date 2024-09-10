def c_to_f(c: int | float | list) -> int|float|list:
    if isinstance(c, (int, float)):
        result = c * 9/5 + 32
    elif isinstance(c, list):
        result = []
        for i in c:
            result.append(i * 9/5 + 32)
    else:
        raise ValueError("Not number")

    return result

c = [1,2,3,4,5,6]
result = c_to_f(c)
if isinstance(result, (int, float)):
    print(f'{c} degrees celcius is equal to {result} f')
else:
    for i in range(len(c)):
        print(f'{c[i]} degrees celcius is equal to {result[i]} f')