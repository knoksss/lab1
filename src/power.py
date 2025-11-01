from src.bracket import bracket_analize
from src.calculate import calcul
from src.errors import SymbolError
from src.errors import BracketError


def main_function(entrance_str):

    # проверяем, что в выражении есть знаки
    count_sign = 0
    for i in '-+*/^~%':
        if entrance_str.count(i) != 0:
            count_sign += 1
    if count_sign == 0:
        raise ValueError('Некорректно введено выражение: не содержит знаков')

    # проверяем, что в выражении нету
    # букв и что оно начинается с цифры
    for i in entrance_str:
        if not i.isdigit():
            if not (i in '-+/*~().%^ '):
                raise SymbolError("Неподдерживаемые символы")
            
    if entrance_str[0] not in '0123456789(':
        raise ValueError(
            "Некорректно введено выражение: начинается не с цифры")

    for i in '-+/*^~':
        if i + '))' in entrance_str:
            raise BracketError("Некорректно записано выражение со скобками")
    if '))' in entrance_str or '((' in entrance_str:
        raise BracketError("Некорректно записано выражение со скобками")

    brackets_anaziled_str = bracket_analize(entrance_str)
    result = calcul(brackets_anaziled_str)
    return result
