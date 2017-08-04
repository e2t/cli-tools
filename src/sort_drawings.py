"""Модуль для сортировки чертежей по каталогам."""
import re
import os
import sys
import shutil


def main() -> None:
    """Выполняется при запуске модуля."""
    changes = r' \(изм\.[0-9]{2}\)'
    asm_pattern = re.compile(
        '(?P<sign>.*[0-9])[ _]?(СБ|МЧ|ВО|УЧ)'
        '([ _](?P<name>((?!{0}).)*)({0})?)?[!.]+'.format(changes), re.I)
    folder = ''
    for i in sorted(set([os.path.abspath(i) for i in sys.argv[1:]])):
        basename = os.path.basename(i)  # with extension
        assembly = asm_pattern.search(basename)
        if assembly is not None:
            folder = os.path.join(os.path.dirname(i), assembly.group('sign'))
            name = assembly.group('name').rstrip()
            if name:
                folder = '{0} {1}'.format(folder, name)
            if not os.path.exists(folder):
                os.makedirs(folder)
        if folder:
            shutil.move(i, os.path.join(folder, basename))


if __name__ == '__main__':
    main()
