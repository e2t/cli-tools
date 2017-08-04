"""Реализация классической программы yes."""
import sys


def main() -> None:
    """Выполняется при запуске модуля."""
    args = sys.argv[1:]
    if args:
        text = ' '.join(args)
    else:
        text = 'y'
    try:
        while True:
            print(text)
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    main()
