"""Программа для запуска выделенных PDF-файлов."""
import os
import re
import sys
import argparse
import sort_drawings


PDF_PATTERN = re.compile(r'.*PDF$', re.IGNORECASE)
ASM_PATTERN = re.compile(fr'.*({sort_drawings.TYPE}).+', re.IGNORECASE)


def is_assembly(name: str) -> bool:
    return ASM_PATTERN.match(name) is not None


def is_not_assembly(name: str) -> bool:
    return not is_assembly(name)


def main() -> None:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--assembly', action='store_const', const=True,
                            help='открывать сборки вместо деталей')
    arg_parser.add_argument('files', nargs='+')
    args = arg_parser.parse_args()

    if args.assembly:
        is_proper = is_assembly
    else:
        is_proper = is_not_assembly

    def scan_dir(fso: str) -> None:
        if os.path.isdir(fso):
            for i in os.listdir(fso):
                scan_dir(os.path.join(fso, i))
        elif PDF_PATTERN.match(fso) and is_proper(os.path.basename(fso)):
            os.startfile(fso)  # maybe don't work with Linux

    for i in args.files:
        if os.path.exists(i):
            scan_dir(i)
        else:
            print(f'File not found "{i}"', file=sys.stderr)


if __name__ == '__main__':
    main()
