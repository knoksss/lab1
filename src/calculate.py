from src.str import Stack
from src.errors import CorrectionError


def calcul(entrance_str):
    mas = entrance_str.split()
    stack = Stack()
    
    for i in mas:
        try:
            # пытаемся преобразовать в число
            stack.push(float(i))
            continue  # если успешно, переходим к следующему i
        except ValueError:
            pass # если нет, то переходим дальше к проверке операций

        if i in ['+', '*', '-', '/', '//', '%', '^']: # проверяем, что входит в набор поддерживаемых операций
            if stack.size() < 2:
                raise CorrectionError("Некорректно введено выражение")
            
            number_2 = float(stack.pop())
            number_1 = float(stack.pop())
            
            if i == '+':
                stack.push(number_1 + number_2)
            elif i == '*':
                stack.push(number_1 * number_2)
            elif i == '−':
                stack.push(number_1 - number_2)
            elif i in ['/', '//', '%']:
                if number_2 == 0:
                    raise ZeroDivisionError("Деление на ноль")
                if i == '/':
                    stack.push(number_1 / number_2)
                elif i == '//':
                    stack.push(number_1 // number_2)
                else:
                    stack.push(number_1 % number_2)
            elif i == '^':
                stack.push(number_1 ** number_2)
                
        elif i == '~': # если унарная, то проверяем её отдельно
            if stack.size() < 1:
                raise CorrectionError("Некорректно ввеедено выражание")
            number = float(stack.pop())
            stack.push(-number)
            
    if stack.size() == 1:
        return float(stack.pop())
    else:
        raise CorrectionError("Некорректно введено выражение")