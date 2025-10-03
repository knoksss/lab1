
def power_function(entrance_str):

    st = entrance_str

    # проверяем, что в выражении
    # нету букв
    while ')' in entrance_str:
        entrance_str = entrance_str.replace(')', '')

    while '(' in entrance_str:
        entrance_str = entrance_str.replace('(', '')

    for i in 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm':
        while i in st:
            st = st.replace(i, '@')
    for i in 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
        while i in st:
            st = st.replace(i, '@')
    if st.count('@') != 0:
        raise ValueError("Неподдерживаемые символы")
    if entrance_str[0] not in '0123456789':
        raise ValueError("Некорректно введено выражение")

    for i in '-+*/^':
        entrance_str = entrance_str.replace(i, ' '+str(i))

    # убираем все пробелы
    while '  ' in entrance_str:
        entrance_str = entrance_str.replace('  ', ' ')
    for i in '-+/*^':
        if i + '))' in entrance_str:
            raise ValueError("Некорректно введено выражение")

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

    print(mas)

    # анализируем выражение, чтобы
    # получить ответ(считаем)
    for i in mas:
        print(i)
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
        else:
            if i in '<>,?/!`@";:[]{}=_&%#№':
                raise ValueError("Неподдерживаемая операция")
            else:
                push(a, i)

    if len(a) == 1:
        answer = peek(a)
        return answer
    else:
        raise ValueError("Некорректно введено выражение")
