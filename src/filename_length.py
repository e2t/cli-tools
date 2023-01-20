import os
import sys
from tkinter.messagebox import showinfo


def main() -> None:
    filename = os.path.abspath(sys.argv[1])
    showinfo('Длина имени файла', f'{filename}\nДлина {len(filename)} симв.')


if __name__ == '__main__':
    main()
