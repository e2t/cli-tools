"""
Рекурсивный запуск указанного процесса для каждого из указанных файлов.

Программа принимает в качестве аргументов путь к процессу, его параметры и
список файлов. Затем процесс запускается с указанными параметрами + имя одного
из файлов. Запуск может производиться последовательно или параллельно,
т.е. ожидая завершения предыдущего процесса или все одновременно.
"""
import os
import subprocess
import argparse


SEPARATOR = '--'
USAGE = '%(prog)s [-h] [--wait] -- program [options] -- file [file ...]'


def main() -> None:
    arg_parser = argparse.ArgumentParser(usage=USAGE)
    arg_parser.add_argument('--wait', action='store_const', const=True,
                            help='ожидать завершения каждого процесса')
    arg_parser.add_argument('argv', nargs='+')
    args = arg_parser.parse_args()

    if len(args.argv) < 3:
        exit(1)
    if SEPARATOR not in args.argv:
        exit(1)
    separator_index = args.argv.index(SEPARATOR)
    if separator_index < 1:
        exit(1)
    cmd = args.argv[:separator_index] + ['']
    files = args.argv[separator_index + 1:]
    files_number = len(files)

    def percents(index: int) -> str:
        return '%3d%%' % (100 * (index + 1) / files_number)

    for index, filename in enumerate(files):
        print(percents(index), os.path.basename(filename))
        cmd[-1] = filename
        proc = subprocess.Popen(cmd)
        if args.wait:
            proc.wait()


if __name__ == '__main__':
    main()
