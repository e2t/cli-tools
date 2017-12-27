"""Модуль для сортировки чертежей по каталогам."""
import re
import os
import sys
import shutil


DESIGNATION = r'[a-zA-Zа-яА-Я].*\d'
TYPE = r'СБ|МЧ|ВО|УЧ'
NAME = r'[a-zA-Zа-яА-Я].*?\S'
CHANGES = r'\(изм\.\d{2}\))'
EXTENSION = r'\.[^.]+'
SEP = r'[\s_]'

DRAWING = re.compile(
    f'^({DESIGNATION})'       # обозначение [1]
    f'{SEP}*({TYPE})?'        # тип чертежа [2]
    f'({SEP}+({NAME}))?'      # наименование [4]
    f'({SEP}+({CHANGES})?'    # номер изменения [5]
    f'{SEP}*({EXTENSION})$',  # расширение файла [6]
    re.IGNORECASE)


def main() -> None:
    files = sys.argv[1:]
    folder = ''
    for i in sorted(set([os.path.abspath(i) for i in files])):
        base_filename = os.path.basename(i)  # с расширением файла
        match = DRAWING.search(base_filename)
        if match and match.group(2):
            designation = match.group(1)
            name = match.group(4)
            if name:
                base_dirname = f'{designation} {name}'
            else:
                base_dirname = designation
            folder = os.path.join(os.path.dirname(i), base_dirname)
            if not os.path.exists(folder):
                os.makedirs(folder)
        if folder:
            shutil.move(i, os.path.join(folder, base_filename))


if __name__ == '__main__':
    main()
