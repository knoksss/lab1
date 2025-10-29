from calculate import calcul

def bracket_analize(entrance_str):

    symb = list(entrance_str)

    # проверяем корректность выражения: сбалансированы ли открывающиеся
    # и закрывающиеся скобки
    while '(' in symb:
        open = -1
        close = -1
        balance = 0
        for i in range(len(symb)):
            if symb[i] == '(':
                open = i
                balance = 1
                for j in range(i + 1, len(symb)):
                    if symb[j] == '(':
                        balance += 1
                    elif symb[j] == ')':
                        balance -= 1
                        if balance == 0:
                            close = j
                            break
                break

        # если не было надейдено ни одной ( или ни одной )
        if open == -1 or close == -1:
            raise ValueError(
                "Некорректно введено выражение: несбалансированные скобки")

        # срезом забираем выражение внутри скобок, чтобы посчитать его
        str_without = symb[open + 1:close]
        exp_w_brackets = ''.join(str_without)
        calc_str = calcul(exp_w_brackets)

        result = symb[:open] + list(str(calc_str)) + symb[close + 1:]
        symb = result
    return ''.join(symb)
