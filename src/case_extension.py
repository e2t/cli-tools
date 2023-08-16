import os
import sys
from argparse import ArgumentParser

# --up %P%S


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--up", action="store_true")
    parser.add_argument("filename", nargs="+")
    args = parser.parse_args()

    for i in sys.argv[1:]:
        path, ext = os.path.splitext(i)
        if not ext:
            continue
        newname = path + ext.upper() if args.up else ext.lower()
        os.rename(i, newname)


if __name__ == "__main__":
    main()
