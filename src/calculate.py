def calcul(entrance_str):

    mas = entrance_str.split()

    # стек
    a = []

    def peek(a):  # выбираем последний элемент
        return a[-1]

    def push(a, x):  # добавляем элемент
        a.append(x)

    def pop(a):  # удаляем элемент
        del a[-1]

    # функции подсчёта

    def plus(a):  # сложение
        x = float(peek(a))
        pop(a)
        y = float(peek(a))
        pop(a)
        push(a, x + y)

    def umno(a):  # умножение
        x = float(peek(a))
        pop(a)
        y = float(peek(a))
        pop(a)
        push(a, x * y)

    def minus(a):  # вычитание
        x = float(peek(a))
        pop(a)
        y = float(peek(a))
        pop(a)
        push(a, y - x)

    def deli(a):  # деление
        x = float(peek(a))
        pop(a)
        y = float(peek(a))
        if x == 0:  # вывод ошибки "деление на ноль"
            raise ZeroDivisionError("Делитель не может быть равен нулю")
        pop(a)
        push(a, y / x)

    def step(a):  # возведение в степень
        x = float(peek(a))
        pop(a)
        y = float(peek(a))
        pop(a)
        push(a, y ** x)

    def unmin(a):  # унарный минус
        x = float(peek(a))
        pop(a)
        push(a, -x)

    # анализируем выражение, чтобы
    # получить ответ(считаем)
    for i in mas:
        if i == '+':
            if len(a) < 2:
                raise ValueError("Некорректно введено выражение")
            plus(a)
        elif i == '*':
            if len(a) < 2:
                raise ValueError("Некорректно введено выражение")
            umno(a)
        elif i == '−':
            if len(a) < 2:
                raise ValueError("Некорректно введено выражение")
            minus(a)
        elif i == '/':
            if len(a) < 2:
                raise ValueError("Некорректно введено выражение")
            deli(a)
        elif i == '^':
            if len(a) < 2:
                raise ValueError("Некорректно введено выражение")
            step(a)
        elif i == '~':
            if len(a) < 2:
                raise ValueError("Некорректно введено выражение")
            unmin(a)
        else:
            if i in '<>,?/!`@";:[]{}=_&%#№':
                raise ValueError("Неподдерживаемая операция")
            else:
                push(a, i)

    if len(a) == 1:
        result = peek(a)
        return result
    else:
        raise ValueError("Некорректно введено выражение")
