import os
import re
import sys

import pyperclip

_DSG_EXPR = "^([A-Z0-9.]+)([0-9]{4})"


def main() -> None:
    if len(sys.argv) == 1:
        input("There are no arguments!")
        return
    path = os.path.abspath(sys.argv[1])
    filename = os.path.basename(path)
    if not (match := re.match(_DSG_EXPR, filename, re.IGNORECASE)):
        input(f'"{filename}" is not match with\n{_DSG_EXPR}\n')
        return
    begin = match.group(1)
    number = int(match.group(2))
    dirname = os.path.dirname(path)
    _, ext = os.path.splitext(filename)
    ext = ext.lower()
    files = []
    for i in os.listdir(dirname):
        i = i.lower()
        if i.endswith(ext) and os.path.isfile(os.path.join(dirname, i)):
            files.append(i)
    next_dsg = ""
    is_free_num = False
    while not is_free_num:
        is_free_num = True
        number += 1
        next_dsg = f"{begin}{number:04}"
        next_re = re.compile(f"^{re.escape(next_dsg)}", re.IGNORECASE)
        for f in files:
            if next_re.match(f):
                is_free_num = False
                break
    pyperclip.copy(next_dsg)
    input(f"Next name: {next_dsg}")


if __name__ == "__main__":
    main()
