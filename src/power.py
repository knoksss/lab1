from bracket import bracket_analize
from calculate import calcul


def main_function(entrance_str):

    st = entrance_str

    # проверяем, что в выражении есть знаки
    count_sign = 0
    for i in '-+*/^~':
        if st.count(i) != 0:
            count_sign += 1
    if count_sign == 0:
        raise ValueError("Некорректно введено выражение")

    # проверяем, что в выражении нету
    # букв и что оно начинается с цифры
    for i in 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm':
        while i in st:
            st = st.replace(i, '@')
    for i in 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
        while i in st:
            st = st.replace(i, '@')
    if st.count('@') != 0:
        raise ValueError("Неподдерживаемые символы: буквы")
    if entrance_str[0] not in '0123456789(':
        raise ValueError(
            "Некорректно введено выражение: начинается не с цифры")

    for i in '-+*/^~':
        entrance_str = entrance_str.replace(i, ' '+str(i))

    # убираем все пробелы
    while '  ' in entrance_str:
        entrance_str = entrance_str.replace('  ', ' ')
    for i in '-+/*^~':
        if i + '))' in st:
            raise ValueError("Некорректно введено выражение")
    if '))' in st or '((' in st:
        raise ValueError("Некорректно введено выражение")

    brackets_anaziled_str = bracket_analize(st)
    result = calcul(brackets_anaziled_str)
    return result
