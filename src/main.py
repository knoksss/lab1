
from power import main_function


def main() -> None:
    entrance_str = input('Введите выражение в обратной польской нотации: ')
    result = main_function(entrance_str)
    print('Посчитанное выражение:', result)


if __name__ == "__main__":
    main()
