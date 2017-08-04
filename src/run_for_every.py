"""
Рекурсивный запуск указанного процесса для каждого из указанных файлов.

Программа принимает в качестве аргументов путь к процессу, его параметры и
список файлов. Затем процесс запускается с указанными параметрами + имя одного
из файлов. Запуск может производиться последовательно или параллельно,
т.е. ожидая завершения предыдущего процесса или все одновременно.
"""
import os
import sys
from subprocess import Popen


def main() -> None:
    """Выполняется при запуске модуля."""
    len_argv = len(sys.argv)
    if len_argv < 5:
        exit(1)
    separator = '--'
    if separator not in sys.argv:
        exit(1)
    separator_index = sys.argv.index(separator)
    if separator_index < 3:
        exit(1)
    need_wait = sys.argv[1] == 'wait'
    cmd = sys.argv[2:separator_index] + ['']
    files_number = len_argv - separator_index - 1

    def percents(index: int) -> str:
        return '%3d%%' % (100 * (index + 1) / files_number)

    for index, filename in enumerate(sys.argv[separator_index + 1:]):
        print(percents(index), os.path.basename(filename))
        cmd[-1] = filename
        proc = Popen(cmd)
        if need_wait:
            proc.wait()


if __name__ == '__main__':
    main()
