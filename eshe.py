result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a должно быть больше или равно b")
        if b > 100:
            raise IndexError("b не должно быть больше 100")
        return a / b
    except ValueError as ve:
        print(f"Ошибка типа ValueError: {ve}")
    except IndexError as ie:
        print(f"Ошибка типа IndexError: {ie}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    return None

data = {10: 2, 2: 5, "123": 4, 18: 0, "some_key": 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(result)
