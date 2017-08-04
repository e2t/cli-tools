"""Программа для запуска выделенных PDF-файлов."""
import sys
import os
import re


def main() -> None:
    """Выполняется при запуске модуля."""
    pdf_pattern = re.compile(r'.*PDF', re.IGNORECASE)
    asm_pattern = re.compile(r'.*[0-9][ _]?(СБ|МЧ|ВО)[ _.].*', re.IGNORECASE)

    def is_assembly(name: str) -> bool:
        return asm_pattern.match(name) is not None

    def is_not_assembly(name: str) -> bool:
        return not is_assembly(name)

    comparing = is_not_assembly
    if sys.argv[1] == '1':
        comparing = is_assembly
    else:
        comparing = is_not_assembly

    def scan_dir(fso: str) -> None:
        if os.path.isdir(fso):
            for i in os.listdir(fso):
                scan_dir(fso + os.sep + i)
        elif pdf_pattern.match(fso) and comparing(os.path.basename(fso)):
            os.startfile(fso)  # maybe don't work with Linux

    for i in sys.argv[2:]:
        scan_dir(i)


if __name__ == '__main__':
    main()
