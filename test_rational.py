from rational import Rational, RationalList, RationalError, RationalValueError

def test():
    output = []

    # Додаємо коректний об'єкт
    try:
        r1 = Rational(1, 2)
        output.append(f"Додаємо {r1} до списку: OK")
    except Exception as e:
        output.append(f"Додаємо 1/2 до списку: Виняток: {e}")

    # Додаємо об'єкт з нульовим знаменником
    try:
        r2 = Rational(3, 0)
        output.append(f"Додаємо {r2} до списку: OK")
    except RationalError as e:
        output.append(f"Додаємо 3/0 до списку: Виняток: {e}")

    # Додаємо некоректний тип у список
    rl = RationalList()
    try:
        rl.add(r1)
        output.append(f"Додаємо {r1} до RationalList: OK")
    except RationalValueError as e:
        output.append(f"Додаємо {r1} до RationalList: Виняток: {e}")

    try:
        rl.add("abc")
        output.append(f"Додаємо 'abc' до RationalList: OK")
    except RationalValueError as e:
        output.append(f"Додаємо 'abc' до RationalList: Виняток: {e}")

    # Арифметичні операції з некоректним типом
    try:
        r3 = r1 + 5
        output.append("Додаємо 5 до Rational: OK")
    except RationalValueError as e:
        output.append(f"Додаємо 5 до Rational: Виняток: {e}")

    # Ділення на нуль
    try:
        r4 = Rational(1, 2) / Rational(0, 1)
        output.append("Ділимо на 0/1: OK")
    except RationalError as e:
        output.append(f"Ділимо на 0/1: Виняток: {e}")

    # Вивід списку
    output.append(f"Список: {rl}")

    return output

if __name__ == "__main__":
    results = test()
    for line in results:
        print(line)